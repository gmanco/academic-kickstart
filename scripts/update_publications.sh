#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required."
  exit 1
fi

if ! python3 -c "import pybtex, yaml" >/dev/null 2>&1; then
  echo "Missing python dependencies. Install once with:"
  echo "python3 -m pip install pybtex pyyaml"
  exit 1
fi

cd "${repo_root}"
python3 scripts/sync_publications.py --config scripts/publications_sync.json

echo "Publication sync completed."
