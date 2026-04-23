---
title: Influence-Based Network-Oblivious Community Detection
date: '2013-01-01'
publishDate: 2019-09-07 09:18:44.871284+00:00
authors:
- Nicola Barbieri
- Francesco Bonchi
- Giuseppe Manco
publication_types:
- '1'
abstract: 'How can we detect communities when the social graphs is not available? We tackle this problem by modeling social contagion from a log of user activity, that is a dataset of tuples (u, i, t) recording the fact that user u "adopted" item i at time t. This is the only input to our problem. We propose a stochastic framework which assumes that item adoptions are governed by un underlying diffusion process over the unobserved social network, and that such diffusion model is based on community-level influence. By fitting the model parameters to the user activity log, we learn the community membership and the level of influence of each user in each community. This allows to identify for each community the "key" users, i.e., the leaders which are most likely to influence the rest of the community to adopt a certain item. The general framework can be instantiated with different diffusion models. In this paper we define two models: the extension to the community level of the classic (discrete
  time) Independent Cascade model, and a model that focuses on the time delay between adoptions. To the best of our knowledge, this is the first work studying community detection without the network.'
publication: '*2013 IEEE 13th International Conference on Data Mining, Dallas, TX, USA, December 7-10, 2013*'
url_pdf: https://doi.org/10.1109/ICDM.2013.164
doi: 10.1109/icdm.2013.164
url_code: https://github.com/gmanco/cwn
url_slides: https://www.slideshare.net/NicolaBarbieri/icdm-2013-barbieri
tags:
- Social Influence
- Information Diffusion
- Social Network Analysis
- Community Detection
- Temporal Point Processes
- Generative Models
featured: false
---
