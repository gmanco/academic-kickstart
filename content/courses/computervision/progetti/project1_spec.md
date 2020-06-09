---
title: Progetto 1
linktitle: Progetto 1
toc: false
type: docs
date: "2020-06-9T00:00:00+01:00"
draft: false

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 200
---

**Specifiche**

- Action Recognition in ambito sportivo

- Task: individuare 10 tipologie di azioni di basket

- Costruire un modello di classificazione

### Dataset

- Il dataset è composto da 32557 clip (MP4, 16 frame RGB) di azioni di basket. Il dataset è suddiviso in train (22779) e test (9778)

- Il test set è utilizzato per la valutazione, le clip (DA NON UTILIZZARE NEL TRAINING) sono definite in un file allegato a queste slide.

- Tipologia di azioni possibili (10 classi)
- Download: https://drive.google.com/open?id=1hLpbLmLFK2-GIvsmpJelGlEx94yQM2Ts

### Requisiti

- Definire e addestrare un modello di classificazione
- Descrivere in una relazione/presentazione le scelte progettuali e tutti i parametri utilizzati nella sperimentazione.
- Consegnare notebook (e/o file sorgente), relazione e dump del modello

### Protocollo di valutazione 

- Valutazione generale del progetto

- Loading del modello e calcolo delle precisione media sul test set



Baseline-1 - 8 pt – Valore 0.40 Baseline-2 - 7 pt – Valore 0.60

Per accedere all’orale sono necessari almeno 8 pt.

### Assegnazione dei punteggi:

- Se il modello supera la Baseline-1: 8 pt
- Se il modello non supera la Baseline-2: (p – Baseline-1)/(Baseline-2 - Baseline-1) * 7 pt
- Se il modello supera la Baseline-2: 7 pt + bonus
- Bonus (p – Baseline-2)/(BESTMODEL - Baseline-2) * 5 pt

## Appelli

- 1 – luglio – Progetto attuale

- Consegna entro domenica 28 giugno

- 31 – luglio – Nuovo Progetto (stesse modalità) 
  - Rilascio indicativo fine giugno



Per ulteriori info vedere [qui](https://github.com/gmanco/cv_notebooks/tree/master/project_1)


