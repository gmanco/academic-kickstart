---
title: 'Relevance meets Diversity: A User-Centric Framework for Knowledge Exploration through Recommendations'
date: '2024-01-01'
publishDate: '2026-04-23T15:56:36Z'
authors:
- Erica Coppolillo
- Giuseppe Manco
- Aristides Gionis
publication_types:
- '2'
abstract: Providing recommendations that are both relevant and diverse is a key consideration of modern recommender systems. Optimizing both of these measures presents a fundamental trade-off, as higher diversity typically comes at the cost of relevance, resulting in lower user engagement. Existing recommendation algorithms try to resolve this trade-off by combining the two measures, relevance and diversity, into one aim and then seeking recommendations that optimize the combined objective, for a given number of items to recommend. Traditional approaches, however, do not consider the user interaction with the recommended items. In this paper, we put the user at the central stage, and build on the interplay between relevance, diversity, and user behavior. In contrast to applications where the goal is solely to maximize engagement, we focus on scenarios aiming at maximizing the total amount of knowledge encountered by the user. We use diversity as a surrogate of the amount of knowledge obtained
  by the user while interacting with the system, and we seek to maximize diversity. We propose a probabilistic user-behavior model in which users keep interacting with the recommender system as long as they receive relevant recommendations, but they may stop if the relevance of the recommended items drops. Thus, for a recommender system to achieve a high-diversity measure, it will need to produce recommendations that are both relevant and diverse. Finally, we propose a novel recommendation strategy that combines relevance and diversity by a copula function. We conduct an extensive evaluation of the proposed methodology over multiple datasets, and we show that our strategy outperforms several state-of-the-art competitors. Our implementation is publicly available at https://github.com/EricaCoppolillo/EXPLORE.
publication: '*CoRR*'
url_pdf: https://doi.org/10.48550/arXiv.2408.03772
doi: 10.48550/arxiv.2408.03772
featured: false
---
