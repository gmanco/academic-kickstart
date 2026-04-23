---
title: Unmasking Conversational Bias in AI Multiagent Systems
date: '2025-01-01'
publishDate: '2026-04-23T15:56:31Z'
authors:
- Erica Coppolillo
- Giuseppe Manco
- Luca Maria Aiello
publication_types:
- '2'
abstract: Detecting biases in the outputs produced by generative models is essential to reduce the potential risks associated with their application in critical settings. However, the majority of existing methodologies for identifying biases in generated text consider the models in isolation and neglect their contextual applications. Specifically, the biases that may arise in multi-agent systems involving generative models remain under-researched. To address this gap, we present a framework designed to quantify biases within multi-agent systems of conversational Large Language Models (LLMs). Our approach involves simulating small echo chambers, where pairs of LLMs, initialized with aligned perspectives on a polarizing topic, engage in discussions. Contrary to expectations, we observe significant shifts in the stance expressed in the generated messages, particularly within echo chambers where all agents initially express conservative viewpoints, in line with the well-documented political
  bias of many LLMs toward liberal positions. Crucially, the bias observed in the echo-chamber experiment remains undetected by current state-of-the-art bias detection methods that rely on questionnaires. This highlights a critical need for the development of a more sophisticated toolkit for bias detection and mitigation for AI multi-agent systems. The code to perform the experiments is publicly available at https://anonymous.4open.science/r/LLMsConversationalBias-7725.
publication: '*CoRR*'
url_pdf: https://doi.org/10.48550/arXiv.2501.14844
doi: 10.48550/arxiv.2501.14844
featured: false
---
