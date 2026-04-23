#!/usr/bin/env python3
"""
Sync publications for Hugo Academic site from DBLP.

Features:
- Fetch BibTeX bibliography from DBLP person PID
- Create/update `content/publication/<slug>/index.md`
- Create/update `content/publication/<slug>/cite.bib`
- Preserve custom editorial fields in existing front matter
- Fill abstract from DBLP BibTeX `abstract` or OpenAlex (via DOI)
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from typing import Dict, List, Optional, Set, Tuple

import yaml
from pybtex.database.input import bibtex


USER_AGENT = "gmanco-hugo-publication-sync/1.0 (+https://gmanco.github.io)"
PRESERVE_FIELDS = {
    "url_code",
    "url_dataset",
    "url_project",
    "url_slides",
    "url_video",
    "image",
    "projects",
}


def http_get_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def http_get_json(url: str, timeout: int = 30) -> dict:
    return json.loads(http_get_text(url, timeout=timeout))


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def clean_bibtex_markup(text: str) -> str:
    """Remove common BibTeX markup artifacts from user-facing strings."""
    t = normalize_text(text)
    t = t.replace("\\{", "{").replace("\\}", "}")
    t = t.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_").replace("\\#", "#")
    t = t.replace("{", "").replace("}", "")
    return normalize_text(t)


def normalize_doi(doi: str) -> str:
    doi = normalize_text(doi).lower()
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)


def strip_html_tags(text: str) -> str:
    t = re.sub(r"<[^>]+>", " ", text or "")
    return normalize_text(html.unescape(t))


def slugify(text: str) -> str:
    text = normalize_text(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "publication"


def normalize_title_for_match(title: str) -> str:
    text = normalize_text(title).lower()
    text = re.sub(r"[{}\"']", "", text)
    text = re.sub(r"[^a-z0-9 ]+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_dblp_pid_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path or ""
    marker = "/pid/"
    idx = path.find(marker)
    if idx == -1:
        return ""
    pid = path[idx + len(marker) :].strip("/")
    pid = re.sub(r"\.(html|xml|bib|rdf|nt|rss)$", "", pid, flags=re.IGNORECASE)
    return pid


def infer_dblp_pid(author_name: str) -> str:
    query = urllib.parse.quote(author_name)
    search_url = f"https://dblp.org/search/author/api?q={query}&format=json"
    data = http_get_json(search_url)
    hits = data.get("result", {}).get("hits", {}).get("hit", [])
    if isinstance(hits, dict):
        hits = [hits]
    if not hits:
        raise RuntimeError(f"No DBLP author hits for '{author_name}'")
    first_url = hits[0].get("info", {}).get("url", "")
    pid = parse_dblp_pid_from_url(first_url)
    if not pid:
        raise RuntimeError("Unable to infer DBLP PID from search response")
    return pid


def fetch_dblp_bibtex(pid: str) -> str:
    pid_quoted = urllib.parse.quote(pid, safe="/")
    bib_url = f"https://dblp.org/pid/{pid_quoted}.bib"
    try:
        return http_get_text(bib_url)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"DBLP export failed ({exc.code}) for {bib_url}") from exc


def split_bib_entries(blob: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    parts = re.split(r"(?=@[a-zA-Z]+\s*{)", blob.strip())
    for part in parts:
        entry = part.strip()
        if not entry.startswith("@"):
            continue
        m = re.match(r"@[a-zA-Z]+\s*{\s*([^,]+)\s*,", entry, flags=re.DOTALL)
        if not m:
            continue
        out[m.group(1).strip()] = entry
    return out


def openalex_abstract_from_doi(doi: str, mailto: str = "") -> str:
    doi = normalize_doi(doi)
    if not doi:
        return ""
    encoded = urllib.parse.quote(f"https://doi.org/{doi}", safe="")
    url = f"https://api.openalex.org/works/{encoded}"
    if mailto:
        url += f"?mailto={urllib.parse.quote(mailto)}"
    data = http_get_json(url)
    inv = data.get("abstract_inverted_index", {})
    if not isinstance(inv, dict) or not inv:
        return ""

    max_pos = -1
    for positions in inv.values():
        if isinstance(positions, list) and positions:
            max_pos = max(max_pos, max(positions))
    if max_pos < 0:
        return ""
    words = [""] * (max_pos + 1)
    for token, positions in inv.items():
        if not isinstance(positions, list):
            continue
        for pos in positions:
            if isinstance(pos, int) and 0 <= pos <= max_pos:
                words[pos] = token
    return normalize_text(" ".join(w for w in words if w))


def openalex_abstract_from_title(title: str, mailto: str = "") -> str:
    q = normalize_text(title)
    if not q:
        return ""
    url = f"https://api.openalex.org/works?search={urllib.parse.quote(q)}&per-page=3"
    if mailto:
        url += f"&mailto={urllib.parse.quote(mailto)}"
    data = http_get_json(url)
    results = data.get("results", [])
    for it in results:
        abs_inv = it.get("abstract_inverted_index", {})
        txt = openalex_inverted_index_to_text(abs_inv)
        if txt:
            return txt
    return ""


def crossref_abstract_from_doi(doi: str) -> str:
    doi = normalize_doi(doi)
    if not doi:
        return ""
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    data = http_get_json(url)
    abs_html = data.get("message", {}).get("abstract", "")
    return strip_html_tags(abs_html)


def semantic_scholar_abstract_from_doi(doi: str) -> str:
    doi = normalize_doi(doi)
    if not doi:
        return ""
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/"
        + urllib.parse.quote(f"DOI:{doi}", safe="")
        + "?fields=title,abstract"
    )
    data = http_get_json(url)
    return normalize_text(data.get("abstract", ""))


def semantic_scholar_abstract_from_title(title: str) -> str:
    q = normalize_text(title)
    if not q:
        return ""
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={urllib.parse.quote(q)}&limit=1&fields=title,abstract"
    )
    data = http_get_json(url)
    rows = data.get("data", [])
    if rows:
        return normalize_text(rows[0].get("abstract", ""))
    return ""


def arxiv_abstract_from_title(title: str) -> str:
    q = normalize_text(title)
    if not q:
        return ""
    url = (
        "https://export.arxiv.org/api/query"
        f"?search_query=all:{urllib.parse.quote(q)}&start=0&max_results=5"
    )
    xml = http_get_text(url, timeout=45)
    entries = re.findall(r"<entry>(.*?)</entry>", xml, flags=re.DOTALL | re.IGNORECASE)
    want = normalize_title_for_match(q)
    best = ""
    for ent in entries:
        t_m = re.search(r"<title>(.*?)</title>", ent, flags=re.DOTALL | re.IGNORECASE)
        s_m = re.search(r"<summary>(.*?)</summary>", ent, flags=re.DOTALL | re.IGNORECASE)
        if not t_m or not s_m:
            continue
        t = normalize_text(html.unescape(t_m.group(1)))
        s = normalize_text(html.unescape(s_m.group(1)))
        if not s:
            continue
        tn = normalize_title_for_match(t)
        if tn == want:
            return s
        if want and tn and (want in tn or tn in want):
            best = s
    return best


def pdf_abstract_from_url(url: str) -> str:
    if not url:
        return ""
    try:
        from pypdf import PdfReader
    except Exception:
        return ""

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=45) as resp:
        content = resp.read()
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as tmp:
        tmp.write(content)
        tmp.flush()
        reader = PdfReader(tmp.name)
        text_parts = []
        for page in reader.pages[:3]:
            try:
                text_parts.append(page.extract_text() or "")
            except Exception:
                continue
        text = normalize_text(" ".join(text_parts))

    # Heuristic extraction between "abstract" and next section marker.
    m = re.search(
        r"\babstract\b[:\s-]*(.+?)(?:\bkeywords?\b|\bintroduction\b|\b1[\.\s]+introduction\b)",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if m:
        return normalize_text(m.group(1))
    return ""


def webpage_abstract(url: str) -> str:
    if not url:
        return ""
    try:
        html_text = http_get_text(url, timeout=45)
    except Exception:
        return ""

    # Common metadata names used by publisher pages.
    meta_patterns = [
        r'<meta[^>]+name=["\']citation_abstract["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+name=["\']dc\.description["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']+)["\']',
    ]
    for pat in meta_patterns:
        m = re.search(pat, html_text, flags=re.IGNORECASE | re.DOTALL)
        if m:
            val = strip_html_tags(m.group(1))
            if len(val) > 40:
                return val

    # Generic structural fallback.
    sec = re.search(r'abstract[^<]{0,30}</[^>]+>\s*<[^>]*>(.*?)</[^>]+>', html_text, flags=re.IGNORECASE | re.DOTALL)
    if sec:
        val = strip_html_tags(sec.group(1))
        if len(val) > 40:
            return val
    return ""


def resolve_abstract(
    *,
    title: str,
    doi: str,
    url: str,
    mailto: str,
) -> str:
    if doi:
        try:
            a = openalex_abstract_from_doi(doi, mailto=mailto)
            if a:
                return a
        except Exception:
            pass
        try:
            a = crossref_abstract_from_doi(doi)
            if a:
                return a
        except Exception:
            pass
        try:
            a = semantic_scholar_abstract_from_doi(doi)
            if a:
                return a
        except Exception:
            pass
        try:
            a = webpage_abstract(f"https://doi.org/{normalize_doi(doi)}")
            if a:
                return a
        except Exception:
            pass
    try:
        a = openalex_abstract_from_title(title, mailto=mailto)
        if a:
            return a
    except Exception:
        pass
    try:
        a = semantic_scholar_abstract_from_title(title)
        if a:
            return a
    except Exception:
        pass
    try:
        a = arxiv_abstract_from_title(title)
        if a:
            return a
    except Exception:
        pass
    if url:
        try:
            a = webpage_abstract(url)
            if a:
                return a
        except Exception:
            pass
    # Last fallback: try direct PDF extraction.
    if url and (url.lower().endswith(".pdf") or "arxiv.org/pdf/" in url.lower()):
        try:
            a = pdf_abstract_from_url(url)
            if a:
                return a
        except Exception:
            pass
    return ""


def read_existing_front_matter(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def write_front_matter(path: str, data: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    yaml_body = yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=False,
        default_flow_style=False,
        width=1000,
    ).strip()
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml_body)
        f.write("\n---\n")


def infer_pub_type(entry_type: str) -> str:
    et = (entry_type or "").lower()
    if et in {"inproceedings", "proceedings"}:
        return "1"  # conference paper
    if et in {"article"}:
        return "2"  # journal article
    if et in {"book", "inbook", "incollection"}:
        return "6"  # book section
    return "5"  # other


def infer_publication_text(fields: dict, entry_type: str) -> str:
    et = (entry_type or "").lower()
    if et in {"inproceedings", "proceedings"} and fields.get("booktitle"):
        return f"*{clean_bibtex_markup(fields['booktitle'])}*"
    if fields.get("journal"):
        return f"*{clean_bibtex_markup(fields['journal'])}*"
    if fields.get("booktitle"):
        return f"*{clean_bibtex_markup(fields['booktitle'])}*"
    if fields.get("publisher"):
        return f"*{clean_bibtex_markup(fields['publisher'])}*"
    return "*Publication venue*"


def infer_venue_plain(fields: dict, entry_type: str) -> str:
    et = (entry_type or "").lower()
    if et in {"inproceedings", "proceedings"} and fields.get("booktitle"):
        return clean_bibtex_markup(fields["booktitle"])
    if fields.get("journal"):
        return clean_bibtex_markup(fields["journal"])
    if fields.get("booktitle"):
        return clean_bibtex_markup(fields["booktitle"])
    if fields.get("publisher"):
        return clean_bibtex_markup(fields["publisher"])
    return ""


def parse_authors(persons) -> List[str]:
    names: List[str] = []
    for author in persons.get("author", []):
        parts = []
        if author.first_names:
            parts.extend(author.first_names)
        if author.middle_names:
            parts.extend(author.middle_names)
        if author.last_names:
            parts.extend(author.last_names)
        full = normalize_text(" ".join(parts))
        if full:
            names.append(full)
    return names


def parse_date(fields: dict) -> str:
    year = normalize_text(fields.get("year", "")) or "1900"
    month_raw = normalize_text(fields.get("month", "1")).lower()
    day_raw = normalize_text(fields.get("day", "1"))

    month_map = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }
    try:
        month = int(month_raw)
    except Exception:
        month = month_map.get(month_raw[:3], 1)
    try:
        day = int(day_raw)
    except Exception:
        day = 1
    month = max(1, min(month, 12))
    day = max(1, min(day, 28))
    return f"{year}-{month:02d}-{day:02d}"


def existing_publication_maps(
    pub_root: str,
) -> Tuple[Dict[str, Set[str]], Dict[str, str], Dict[str, dict], Set[str]]:
    doi_map: Dict[str, Set[str]] = {}
    title_map: Dict[str, str] = {}
    front_map: Dict[str, dict] = {}
    ambiguous_doi: Set[str] = set()
    if not os.path.isdir(pub_root):
        return doi_map, title_map, front_map, ambiguous_doi
    for slug in os.listdir(pub_root):
        index_path = os.path.join(pub_root, slug, "index.md")
        if not os.path.exists(index_path):
            continue
        front = read_existing_front_matter(index_path)
        front_map[slug] = front
        doi = normalize_doi(front.get("doi", ""))
        title = normalize_title_for_match(front.get("title", ""))
        if doi:
            doi_map.setdefault(doi, set()).add(slug)
        if title:
            title_map[title] = slug
    for doi, slugs in doi_map.items():
        if len(slugs) > 1:
            ambiguous_doi.add(doi)
    return doi_map, title_map, front_map, ambiguous_doi


def choose_slug(
    title: str,
    authors: List[str],
    year: str,
    doi: str,
    doi_map: Dict[str, Set[str]],
    ambiguous_doi: Set[str],
    title_map: Dict[str, str],
    used: set,
) -> str:
    doi_key = normalize_doi(doi)
    title_key = normalize_title_for_match(title)
    if doi_key and doi_key in doi_map and doi_key not in ambiguous_doi:
        only = list(doi_map[doi_key])
        if len(only) == 1:
            return only[0]
    if title_key and title_key in title_map:
        return title_map[title_key]

    last = "paper"
    if authors:
        last = slugify(authors[0].split()[-1])
    base = f"{last}-{year}"
    slug = base
    counter = 1
    while slug in used:
        counter += 1
        slug = f"{base}-{counter}"
    return slug


def build_front_matter(existing: dict, computed: dict) -> dict:
    out: Dict[str, object] = {}
    key_order = [
        "title",
        "date",
        "publishDate",
        "authors",
        "publication_types",
        "abstract",
        "featured",
        "publication",
        "url_pdf",
        "url_code",
        "url_dataset",
        "url_project",
        "url_slides",
        "url_video",
        "doi",
        "image",
        "tags",
    ]

    for k in key_order:
        if k in computed:
            out[k] = computed[k]

    for k in PRESERVE_FIELDS:
        if k in existing and existing[k] not in [None, "", [], {}]:
            out[k] = existing[k]

    if "tags" in existing and existing["tags"]:
        out["tags"] = existing["tags"]
    elif "tags" in computed and computed["tags"]:
        out["tags"] = computed["tags"]

    if "publishDate" in existing and existing["publishDate"]:
        out["publishDate"] = existing["publishDate"]

    if "featured" not in out:
        out["featured"] = bool(existing.get("featured", False))

    # Keep any additional custom keys not explicitly managed.
    for k, v in existing.items():
        if k not in out:
            out[k] = v

    return out


def is_high_impact_candidate(
    *,
    title: str,
    authors: List[str],
    year: int,
    venue_text: str,
    slug: str,
    policy: dict,
) -> bool:
    if not policy.get("enabled", True):
        return False

    disabled = set(policy.get("disabled_image_slugs", []))
    if slug in disabled:
        return False

    pinned = set(policy.get("pinned_slugs", []))
    if slug in pinned:
        return True

    last_n = int(policy.get("last_n_years", 3))
    current_year = dt.datetime.utcnow().year
    min_year = current_year - (last_n - 1)
    if year < min_year:
        return False

    required_author = normalize_text(policy.get("require_author_name", ""))
    if required_author:
        names = [normalize_text(a).lower() for a in authors]
        if required_author.lower() not in names:
            return False

    title_norm = normalize_text(title).lower()
    venue_norm = normalize_text(venue_text).lower()

    excluded_venue_keywords = [normalize_text(v).lower() for v in policy.get("excluded_venue_keywords", [])]
    for kw in excluded_venue_keywords:
        if kw and kw in venue_norm:
            return False

    excluded_title_keywords = [normalize_text(v).lower() for v in policy.get("excluded_title_keywords", [])]
    for kw in excluded_title_keywords:
        if kw and kw in title_norm:
            return False

    venue_keywords = [normalize_text(v).lower() for v in policy.get("high_impact_venue_keywords", [])]
    for kw in venue_keywords:
        if kw and kw in venue_norm:
            return True

    return False


def publication_has_featured_image(folder: str, front: dict) -> bool:
    candidates = [
        "featured.png",
        "featured.jpg",
        "featured.jpeg",
        "featured.webp",
    ]
    for name in candidates:
        if os.path.exists(os.path.join(folder, name)):
            return True
    img = front.get("image")
    if isinstance(img, dict):
        cap = normalize_text(img.get("caption", ""))
        if "featured" in cap.lower():
            return True
    return False


def abstract_keywords(text: str, k: int = 6) -> List[str]:
    stop = {
        "the", "and", "for", "with", "from", "that", "this", "are", "was", "were", "into", "their",
        "have", "has", "had", "using", "used", "use", "over", "under", "between", "within", "across",
        "through", "based", "towards", "toward", "paper", "approach", "method", "methods", "results",
        "model", "models", "data", "analysis", "study", "proposed", "show", "shows", "our", "we", "to",
        "of", "in", "on", "a", "an", "by", "as", "is", "be", "or", "it", "at"
    }
    words = re.findall(r"[A-Za-z][A-Za-z\\-]{3,}", normalize_text(text).lower())
    freq: Dict[str, int] = {}
    for w in words:
        if w in stop:
            continue
        freq[w] = freq.get(w, 0) + 1
    best = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]
    return [w for w, _ in best]


def ensure_featured_png(repo_root: str, folder: str, title: str, venue: str, year: int, abstract: str) -> str:
    """Create a unique raster featured image from title + abstract + venue."""
    os.makedirs(folder, exist_ok=True)
    out = os.path.join(folder, "featured.png")
    try:
        from PIL import Image, ImageDraw, ImageFont

        w, h = 1200, 630
        im = Image.new("RGB", (w, h), (15, 35, 58))
        draw = ImageDraw.Draw(im)

        # Hash-derived accent and geometry from abstract content.
        seed = abs(hash((title, venue, year, abstract[:300]))) % 255
        accent = (40 + seed % 140, 90 + (seed * 3) % 120, 120 + (seed * 5) % 100)
        accent2 = (40 + (seed * 7) % 130, 80 + (seed * 11) % 120, 110 + (seed * 13) % 120)
        draw.rectangle([0, 0, w, h], fill=(12, 28, 48))
        draw.rectangle([0, 0, w, 160], fill=accent)
        for i in range(0, w, 80):
            y0 = 160 + ((i + seed) % 70)
            draw.line([(i, y0), (i + 220, y0 + 120)], fill=accent2, width=2)
        draw.rectangle([36, 176, w - 36, h - 36], outline=(220, 235, 255), width=2)

        font_title = ImageFont.load_default()
        font_meta = ImageFont.load_default()

        def wrap(text: str, max_chars: int) -> List[str]:
            words = normalize_text(text).split(" ")
            lines: List[str] = []
            cur = []
            for wd in words:
                nxt = (" ".join(cur + [wd])).strip()
                if len(nxt) <= max_chars:
                    cur.append(wd)
                else:
                    if cur:
                        lines.append(" ".join(cur))
                    cur = [wd]
            if cur:
                lines.append(" ".join(cur))
            return lines

        kw = abstract_keywords(abstract, k=6)
        draw.text((58, 30), f"Featured Publication · {year}", fill=(255, 255, 255), font=font_meta)
        y = 206
        for line in wrap(title, 48)[:6]:
            draw.text((70, y), line, fill=(240, 247, 255), font=font_title)
            y += 26

        # Abstract-driven summary snippet.
        snippet = normalize_text(abstract)[:330]
        if len(normalize_text(abstract)) > 330:
            snippet += "..."
        y += 10
        for line in wrap(snippet, 86)[:4]:
            draw.text((70, y), line, fill=(201, 220, 236), font=font_meta)
            y += 22

        # Key topics extracted from abstract.
        y = min(y + 16, h - 120)
        if kw:
            draw.text((70, y), "Keywords:", fill=(190, 255, 222), font=font_meta)
            x = 170
            for token in kw:
                label = f"[{token}]"
                draw.text((x, y), label, fill=(190, 255, 222), font=font_meta)
                x += max(70, 12 + len(label) * 7)
                if x > w - 220:
                    y += 24
                    x = 170

        y = min(y + 34, h - 90)
        for line in wrap(venue, 72)[:3]:
            draw.text((70, y), line, fill=(201, 255, 228), font=font_meta)
            y += 24

        im.save(out, format="PNG")
    except Exception:
        # Safe fallback if Pillow is unavailable.
        candidates = [
            os.path.join(repo_root, "static", "img", "icon-512.png"),
            os.path.join(repo_root, "content", "publication", "manco-2021", "featured.png"),
        ]
        src = ""
        for c in candidates:
            if os.path.exists(c):
                src = c
                break
        if not src:
            raise RuntimeError("No source PNG available to generate featured image")
        with open(src, "rb") as rf, open(out, "wb") as wf:
            wf.write(rf.read())
    return out


def clear_featured_files(folder: str) -> None:
    for name in ["featured.png", "featured.jpg", "featured.jpeg", "featured.webp", "featured.svg"]:
        p = os.path.join(folder, name)
        if os.path.exists(p):
            os.remove(p)


def apply_user_featured_image(folder: str, source_path: str) -> bool:
    src = os.path.expanduser(source_path.strip())
    if not os.path.isabs(src):
        src = os.path.abspath(src)
    if not os.path.exists(src) or not os.path.isfile(src):
        print(f"[WARN] Image path not found: {src}")
        return False

    ext = os.path.splitext(src)[1].lower()
    allowed = {".png", ".jpg", ".jpeg", ".webp"}
    clear_featured_files(folder)

    if ext in allowed:
        dst = os.path.join(folder, f"featured{ext}")
        shutil.copyfile(src, dst)
        return True

    # Try conversion to PNG via Pillow for non-standard formats.
    try:
        from PIL import Image

        dst = os.path.join(folder, "featured.png")
        with Image.open(src) as im:
            im.convert("RGB").save(dst, format="PNG")
        return True
    except Exception:
        print(f"[WARN] Unsupported image extension ({ext}) and conversion failed.")
        return False


def review_featured_image_interactive(slug: str, title: str, folder: str) -> str:
    """
    Returns one of:
    - keep
    - replaced
    - removed
    """
    print("\n[IMAGE REVIEW]")
    print(f"  slug : {slug}")
    print(f"  title: {title}")
    print("  Actions: [Enter] keep generated image, [p] provide image path, [r] remove image and exclude permanently")
    while True:
        choice = input("  Your choice [Enter/p/r]: ").strip().lower()
        if choice == "":
            return "keep"
        if choice == "p":
            img = input("  Absolute (or relative) image path: ").strip()
            if apply_user_featured_image(folder, img):
                return "replaced"
            continue
        if choice == "r":
            clear_featured_files(folder)
            return "removed"
        print("  Invalid option. Use Enter, p, or r.")


def save_config_json(path: str, config: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
        f.write("\n")


def sync(config: dict, config_path: str = "") -> int:
    repo_root = os.path.abspath(config.get("repo_root", "."))
    pub_root = config.get("output_dir", "content/publication")
    author_name = config.get("author_name", "Giuseppe Manco")
    dblp_cfg = config.get("dblp", {})
    enrich_cfg = config.get("abstract_enrichment", {})

    pid = normalize_text(dblp_cfg.get("pid", ""))
    if not pid:
        pid = infer_dblp_pid(author_name)
        print(f"[INFO] DBLP PID inferred: {pid}")

    bib_blob = fetch_dblp_bibtex(pid)
    raw_by_key = split_bib_entries(bib_blob)

    parser = bibtex.Parser()
    bib_data = parser.parse_string(bib_blob)

    filters = config.get("filters", {})
    min_year = int(filters.get("min_year", 1900))
    allowed_types = {
        str(x).lower() for x in filters.get("allowed_entry_types", ["article", "inproceedings", "proceedings"])
    }

    doi_map, title_map, front_map, ambiguous_doi = existing_publication_maps(pub_root)
    used_slugs = set(front_map.keys())
    featured_policy = config.get("featured_policy", {})
    disabled_slugs = set(featured_policy.get("disabled_image_slugs", []))
    interactive_images = bool(featured_policy.get("interactive_image_review", False)) and sys.stdin.isatty()
    config_touched = False

    # Build a global title -> abstract cache from all DBLP entries (including preprints).
    title_abstract_cache: Dict[str, str] = {}
    for _k, e in bib_data.entries.items():
        t = clean_bibtex_markup(e.fields.get("title", ""))
        a = normalize_text(e.fields.get("abstract", ""))
        if t and a:
            nk = normalize_title_for_match(t)
            if nk and nk not in title_abstract_cache:
                title_abstract_cache[nk] = a

    created = 0
    updated = 0
    skipped = 0
    abstract_added = 0
    processed_slugs: Set[str] = set()

    selected: Dict[str, Tuple[str, object]] = {}
    for key, entry in bib_data.entries.items():
        et = (entry.type or "").lower()
        if allowed_types and et not in allowed_types:
            skipped += 1
            continue
        year_raw = normalize_text(entry.fields.get("year", "0"))
        try:
            if int(year_raw) < min_year:
                skipped += 1
                continue
        except Exception:
            skipped += 1
            continue

        title = clean_bibtex_markup(entry.fields.get("title", ""))
        doi = normalize_doi(entry.fields.get("doi", ""))
        dedupe_key = f"doi:{doi}" if doi else f"title:{normalize_title_for_match(title)}"
        if dedupe_key in {"title:"}:
            skipped += 1
            continue
        score = 2 if doi else 1
        prev = selected.get(dedupe_key)
        if prev is None or score > prev[0]:
            selected[dedupe_key] = (score, key)

    for _, (_, key) in selected.items():
        entry = bib_data.entries[key]
        fields = entry.fields
        title = clean_bibtex_markup(fields.get("title", ""))
        if not title:
            skipped += 1
            continue
        authors = parse_authors(entry.persons)
        if not authors:
            skipped += 1
            continue

        entry_type = entry.type
        date = parse_date(fields)
        year = date[:4]
        doi = normalize_doi(fields.get("doi", ""))
        url = normalize_text(fields.get("url", ""))
        abstract = normalize_text(fields.get("abstract", ""))
        if not abstract:
            abstract = title_abstract_cache.get(normalize_title_for_match(title), "")
        if not abstract and doi and enrich_cfg.get("enabled", True):
            try:
                abstract = openalex_abstract_from_doi(doi, enrich_cfg.get("mailto", ""))
                if abstract:
                    abstract_added += 1
            except Exception:
                pass

        pub_text = infer_publication_text(fields, entry_type)
        venue_plain = infer_venue_plain(fields, entry_type)
        pub_type = infer_pub_type(entry_type)
        keywords = normalize_text(fields.get("keywords", ""))
        tags = [normalize_text(x) for x in re.split(r"[;,]", keywords) if normalize_text(x)]

        slug = choose_slug(
            title=title,
            authors=authors,
            year=year,
            doi=doi,
            doi_map=doi_map,
            ambiguous_doi=ambiguous_doi,
            title_map=title_map,
            used=used_slugs,
        )
        used_slugs.add(slug)

        folder = os.path.join(pub_root, slug)
        index_path = os.path.join(folder, "index.md")
        cite_path = os.path.join(folder, "cite.bib")

        existing_front = read_existing_front_matter(index_path)
        now_iso = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

        computed_front = {
            "title": title,
            "date": date,
            "publishDate": now_iso,
            "authors": authors,
            "publication_types": [pub_type],
            "abstract": abstract,
            "publication": pub_text,
            "url_pdf": url,
            "doi": doi,
            "tags": tags,
        }

        # Remove empty keys to keep front matter tidy.
        computed_front = {k: v for k, v in computed_front.items() if v not in [None, "", [], {}]}
        merged = build_front_matter(existing_front, computed_front)
        try:
            y = int(year)
        except Exception:
            y = 1900
        has_abs = bool(normalize_text(str(merged.get("abstract", ""))))
        has_img = publication_has_featured_image(folder, merged)
        candidate = is_high_impact_candidate(
            title=title,
            authors=authors,
            year=y,
            venue_text=venue_plain,
            slug=slug,
            policy=featured_policy,
        )
        if candidate and not has_abs and featured_policy.get("enforce_featured_abstract_retrieval", True):
            resolved = resolve_abstract(
                title=title,
                doi=doi,
                url=url,
                mailto=enrich_cfg.get("mailto", ""),
            )
            if resolved:
                merged["abstract"] = resolved
                has_abs = True
        force_regen = featured_policy.get("regenerate_featured_images", False)
        generated_now = False
        if candidate and (force_regen or (not has_img and featured_policy.get("auto_generate_missing_featured_images", False))):
            ensure_featured_png(repo_root, folder, title, venue_plain, y, str(merged.get("abstract", "")))
            has_img = publication_has_featured_image(folder, merged)
            generated_now = True

        if candidate and interactive_images and (generated_now or has_img):
            decision = review_featured_image_interactive(slug, title, folder)
            if decision == "removed":
                disabled_slugs.add(slug)
                has_img = False
                candidate = False
                config_touched = True
            elif decision == "replaced":
                has_img = publication_has_featured_image(folder, merged)

        merged["featured"] = bool(candidate and has_abs and has_img)

        os.makedirs(folder, exist_ok=True)
        write_front_matter(index_path, merged)
        processed_slugs.add(slug)

        raw_bib = raw_by_key.get(key, "")
        if raw_bib:
            with open(cite_path, "w", encoding="utf-8") as f:
                f.write(raw_bib.strip() + "\n")

        if existing_front:
            updated += 1
        else:
            created += 1

    # Enforce featured policy on existing publication pages not touched by this run.
    for slug, existing_front in front_map.items():
        if slug in processed_slugs:
            continue
        index_path = os.path.join(pub_root, slug, "index.md")
        if not os.path.exists(index_path):
            continue
        date_val = normalize_text(existing_front.get("date", ""))
        try:
            year_val = int(date_val[:4])
        except Exception:
            year_val = 1900
        venue_val = normalize_text(existing_front.get("publication", ""))
        title_val = normalize_text(existing_front.get("title", ""))
        authors_val = existing_front.get("authors", []) or []
        if isinstance(authors_val, str):
            authors_val = [authors_val]
        has_abs = bool(normalize_text(str(existing_front.get("abstract", ""))))
        folder = os.path.join(pub_root, slug)
        has_img = publication_has_featured_image(folder, existing_front)
        candidate = is_high_impact_candidate(
            title=title_val,
            authors=authors_val,
            year=year_val,
            venue_text=venue_val,
            slug=slug,
            policy=featured_policy,
        )
        if candidate and not has_abs and featured_policy.get("enforce_featured_abstract_retrieval", True):
            doi_val = normalize_doi(existing_front.get("doi", ""))
            url_val = normalize_text(existing_front.get("url_pdf", ""))
            resolved = resolve_abstract(
                title=title_val,
                doi=doi_val,
                url=url_val,
                mailto=enrich_cfg.get("mailto", ""),
            )
            if resolved:
                existing_front["abstract"] = resolved
                has_abs = True
        force_regen = featured_policy.get("regenerate_featured_images", False)
        generated_now = False
        if candidate and (force_regen or (not has_img and featured_policy.get("auto_generate_missing_featured_images", False))):
            ensure_featured_png(repo_root, folder, title_val, venue_val, year_val, str(existing_front.get("abstract", "")))
            has_img = publication_has_featured_image(folder, existing_front)
            generated_now = True

        if candidate and interactive_images and (generated_now or has_img):
            decision = review_featured_image_interactive(slug, title_val, folder)
            if decision == "removed":
                disabled_slugs.add(slug)
                has_img = False
                candidate = False
                config_touched = True
            elif decision == "replaced":
                has_img = publication_has_featured_image(folder, existing_front)

        featured_val = bool(candidate and has_abs and has_img)
        if bool(existing_front.get("featured", False)) != featured_val:
            existing_front["featured"] = featured_val
            write_front_matter(index_path, existing_front)

    if featured_policy.get("disabled_image_slugs", []) != sorted(disabled_slugs):
        featured_policy["disabled_image_slugs"] = sorted(disabled_slugs)
        config_touched = True
    if config_touched and config_path:
        save_config_json(config_path, config)
        print(f"[INFO] Config updated with disabled slugs in {config_path}")

    print(f"[INFO] Publications processed. Created: {created}, Updated: {updated}, Skipped: {skipped}")
    print(f"[INFO] Abstracts added from OpenAlex: {abstract_added}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Hugo Academic publications from DBLP")
    parser.add_argument(
        "--config",
        default="scripts/publications_sync.json",
        help="Path to sync config JSON",
    )
    args = parser.parse_args()

    if not os.path.exists(args.config):
        print(
            f"Config not found: {args.config}\n"
            "Create it from scripts/publications_sync.example.json"
        )
        return 1
    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)
    return sync(config, config_path=args.config)


if __name__ == "__main__":
    raise SystemExit(main())
