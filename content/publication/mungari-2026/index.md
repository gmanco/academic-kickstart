---
title: 'ARES: Anomaly Recognition Model For Edge Streams'
date: '2026-01-01'
publishDate: '2026-04-23T15:56:27Z'
authors:
- Simone Mungari
- Albert Bifet
- Giuseppe Manco
- Bernhard Pfahringer
publication_types:
- '1'
publication: '*Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1, KDD 2026, Jeju Island, Korea, August 9-13, 2026*'
url_pdf: https://doi.org/10.1145/3770854.3780242
doi: 10.1145/3770854.3780242
featured: true
abstract: Many real-world scenarios involving streaming information can be represented as temporal graphs, where data flows through dynamic changes in edges over time. Anomaly detection in this context has the objective of identifying unusual temporal connections within the graph structure. Detecting edge anomalies in real time is crucial for mitigating potential risks. Unlike traditional anomaly detection, this task is particularly challenging due to concept drifts, large data volumes, and the need for real-time response. To face these challenges, we introduce ARES, an unsupervised anomaly detection framework for edge streams. ARES combines Graph Neural Networks (GNNs) for feature extraction with Half-Space Trees (HST) for anomaly scoring. GNNs capture both spike and burst anomalous behaviors within streams by embedding node and edge properties in a latent space, while HST partitions this space to isolate anomalies efficiently. ARES operates in an unsupervised way without the need for prior
  data labeling. To further validate its detection capabilities, we additionally incorporate a simple yet effective supervised thresholding mechanism. This approach leverages statistical dispersion among anomaly scores to determine the optimal threshold using a minimal set of labeled data, ensuring adaptability across different domains. We validate ARES through extensive evaluations across several real-world cyber-attack scenarios, comparing its performance against existing methods while analyzing its space and time complexity. The code used to perform the experiments is publicly available at https://github.com/AnomalyRecognitionModelForEdgeStreams/ARES.
---
