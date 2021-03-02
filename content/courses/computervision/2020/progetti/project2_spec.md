---
title: Progetto 2
linktitle: Progetto 2
toc: false
type: docs
date: "2020-07-1T00:00:00+01:00"
draft: false

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 300
---

**Specifiche**

- Action Recognition in ambito sportivo

- Task: individuare 10 tipologie di azioni di basket

- Costruire un modello di classificazione

### Dataset

Si utilizza lo stesso dataset dell'appello precedente ([appello precedente](https://github.com/gmanco/cv_notebooks/blob/master/project1)) con lo stesso protocollo di valutazione e le baseline riportate di seguito.

> Principali differenze rispetto all'appello precedente:
>
> - nuovo test set
> - nuovi valori baseline
> - oltre al materiale già indicato, è necessario consegnare anche una presentazione da mostrare durante l'esame

### Requisiti

- Definire e addestrare un modello di classificazione
- Descrivere in una presentazione le scelte progettuali e tutti i parametri utilizzati nella sperimentazione.
- Consegnare notebook (e/o file sorgente), **PRESENTAZIONE** e dump del modello

### Protocollo di valutazione 

- Valutazione generale del progetto

- Loading del modello e calcolo delle precisione media sul test set

```
Baseline-1 - 8 pt – Valore 0.65
Baseline-2 - 7 pt – Valore 0.70

Per accedere all’orale sono necessari almeno 8 pt.

Assegnazione dei punteggi:
Se il modello supera la Baseline-1: 8 pt
Se il modello non supera la Baseline-2: (p – Baseline-1)/(Baseline-2 - Baseline-1) * 7 pt
Se il modello supera la Baseline-2: 7 pt + bonus
Bonus (p – Baseline-2)/(BESTMODEL - Baseline-2) * 5 pt
```

**Nuovo TestSet**

Per costruire il test set utilizzare le chiavi fornite nel file [testset_keys_1lug2020.txt](https://github.com/gmanco/cv_notebooks/blob/master/project_2/testset_keys_1lug2020.txt)

```
MD5 (testset_keys_1lug2020.txt) = d66ed18631567fdf3069cbd7fc9e5de1
```

**Appello**

- Data Rilascio 01/07/2020
- Data Consegna 29/07/2020 ore 12.00
- Data Appello 31/07/2020



Per ulteriori info vedere https://github.com/gmanco/cv_notebooks/tree/master/project_2


