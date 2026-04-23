---
title: An incremental clustering scheme for data de-duplication
date: '2010-01-01'
publishDate: 2019-09-07 09:18:44.878072+00:00
authors:
- Gianni Costa
- Giuseppe Manco
- Riccardo Ortale
publication_types:
- '2'
publication: '*Data Min. Knowl. Discov.*'
url_pdf: https://doi.org/10.1007/s10618-009-0155-0
doi: 10.1007/s10618-009-0155-0
tags:
- Clustering
- Indexing
- Hashing
- similarity measures
- Entity resolution
- Deduplication
featured: false
abstract: 'We propose an incremental technique for discovering duplicates in large databases of textual sequences, i.e., syntactically different tuples, that refer to the same real-world entity. The problem is approached from a clustering perspective: given a set of tuples, the objective is to partition them into groups of duplicate tuples. Each newly arrived tuple is assigned to an appropriate cluster via nearest-neighbor classification. This is achieved by means of a suitable hash-based index, that maps any tuple to a set of indexing keys and assigns tuples with high syntactic similarity to the same buckets. Hence, the neighbors of a query tuple can be efficiently identified by simply retrieving those tuples that appear in the same buckets associated to the query tuple itself, without completely scanning the original database. Two alternative schemes for computing indexing keys are discussed and compared. An extensive experimental evaluation on both synthetic and real data shows the effectiveness
  of our approach.'
---
