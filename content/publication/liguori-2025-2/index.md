---
title: 'Breaking domain barriers: mixture of experts for cross-domain fake news detection'
date: '2025-01-01'
publishDate: '2026-04-23T15:56:29Z'
authors:
- Angelica Liguori
- Francesco Sergio Pisani
- Carmela Comito
- Massimo Guarascio
- Giuseppe Manco
publication_types:
- '2'
abstract: Social media have become a key tool for rapidly spreading information worldwide, amplifying the risks of misinformation and fake news. This is also intensified by the fact that fake news covers a wide range of topics across multiple domains. Machine learning, particularly language models, offers a promising solution for detecting fake news. However, a major limitation of existing methods is their inability to classify instances from new or unseen domains. To tackle this issue, we introduce MERMAID, a mixture of experts approach that leverages the knowledge from different specialized models to classify examples from unknown domains. Each expert is initially trained on a specific known domain and then fine-tuned using data from other known domains. A model merging procedure is then applied to combine related experts, reducing the number of models required for predicting instances from unknown domains. In addition, our approach can effectively be used in few-shot learning scenarios,
  where a small amount of data from the target/unknown domain is available during training. Experiments on five benchmark datasets demonstrate the effectiveness of our method in both zero-shot and few-shot learning settings.
publication: '*Mach. Learn.*'
url_pdf: https://doi.org/10.1007/s10994-025-06827-9
doi: 10.1007/s10994-025-06827-9
featured: false
---
