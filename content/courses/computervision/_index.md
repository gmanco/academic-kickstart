---
# Course title, summary, and position.
linktitle: Analisi di Immagini e Video (Computer Vision)
summary: Il corso mira a fornire solide basi in merito all’analisi di immagini e video e fornire una conoscenza delle principali tecniche di deep learning per il riconoscimento di oggetti e l’individuazione di sequenze rilevanti in un video. 


weight: 1

# Page metadata.
title: Panoramica
date: "2021-03-01T00:00:00Z"
lastmod: "2021-03-01T00:00:00Z"
draft: false  # Is this a draft? true/false
toc: true  # Show table of contents? true/false
type: docs  # Do not modify.

# Add menu entry to sidebar.
# - name: Declare this menu item as a parent with ID `name`.
# - weight: Position of link in menu.
menu: 
  computervision:
    name: Panoramica
    weight: 1
  
---

## Annunci

-  **[12/04/2021]** I risultati del primo esonero  sono disponibili al seguente [link]({{< relref "../computervision/esoneri/esonero1.md" >}}). 
-  **[01/03/2021]** Questo è il sito web dell'edizione 2020-2021 del corso. L'edizione precedente è disponibile al sequente [link]({{< relref "../computervision/2020" >}}). 
- **[03/03/2021]** Si avvisano gli studenti che il corso di Analisi di Immagini e Video – Corso di Laurea Magistrale in Ingegneria Informatica verrà inizialmente erogato in modalità streaming, utilizzando l’applicativo TEAMS, a partire dal giorno 02/03/2019, alle ore 11:30. La richiesta di iscrizione al corso può essere effettuata cliccando sul seguente [link](https://teams.microsoft.com/l/team/19%3a85cc03830d8145e9b23ab2b9f21641f0%40thread.tacv2/conversations?groupId=8bbaa92e-68d3-4c10-887f-157c5a2392ab&tenantId=7519d0cd-2106-47d9-adcb-320023abff57). Gli studenti già pratici dell’utilizzo di TEAMS e che abbiano già scaricato l’APP, possono iscriversi direttamente al corso (senza approvazione del docente) utilizzando il codice: **czo3mqk**




## Breve descrizione del corso


Il corso è finalizzato ad acquisire e sperimentare le tecniche di base per l’analisi di immagini e video. Verranno illustrati i concetti fondamentali per l’analisi delle immagini e verranno illustrate le principali tecniche di object detection, object tracking e action detection. Durante il corso saranno presentati modelli di reti neurali CNN e RNN, tecniche di transfer learning, Residual and Attention network ed una introduzione ai modelli generativi e alle Adversarial networks. Gli esempi applicativi faranno uso del linguaggio Python e dei framework di Deep Learning Pytorch/Tensorflow.

Competenze specifiche:

* comprensione dei concetti legati all’image e al video processing
* conoscenza degli aspetti caratterizzanti di machine learning e deep learning
* comprensione delle principali tecniche per l’analisi di immagini e video
* abilità di utilizzare algoritmi di image analysis per la risoluzione di problemi specifici



## Docenti
- Giuseppe Manco. Ricevimento: mercoledì’ 14:30-16:30. 
- Francesco Pisani. Rivevimento lunedì 15-17.

## Programma

1.	**Introduzione alla computer vision**
	-	Concetti fondamentali su Image processing e analysis: Image Basics, Python per Image Processing, Manipolazione di immagini.
	-	Trasformazioni: Normalizzazione, filtri, Edge detection, morfologia, thresholding e segmentazione.
2.	**Classificazione di immagini e video**
	-	Introduzione alla classificazione: applicazioni; approcci classici; scikit-Learn per la classificazione; limitazioni.
	-	Deep Learning: Review su Neural Networks per l'analisi di immagini e video. Convolutional Neural Networks. Reti ricorrenti. Gestione dell'overfitting.
	-	Concetti avanzati. Principali architetture di rete e loro caratteristiche: VGG, AlexNet, Inception and Residual Networks, Attention Networks. Transfer Learning.
3.	**Concetti avanzati**
	-	Object Detection: Sliding windows, boundary boxes e anchors. Region Proposal Networks. Yolo e Darknet. Applicazioni.
	-	Object tracking e action recognition. Optical flow; Single/multiple objects tracking; Action classification and localization.
	-	Image segmentation e synthesis. UNet. Neural style transfer.
	-	Modelli Generativi: Probabilistic Modeling, Autoencoders. Generative Adversarial Networks. Applicazioni: Colorization, Reconstruction, Super-Resolution, Synthesis, Text-to-image.
	-	Adversarial Machine Learning. Principali attacchi e contromisure. Adversarial-free deep networks.



## Materiale didattico
- Lucidi delle lezioni
- Notebooks e lucidi delle esercitazioni
- Libri di consultazione:
	- E.R. Davies, Computer Vision: Principles, Algorithms, Applications, Learning. Fifth edition. Elsevier/Academic Press, 2018 **[Davies18]**
	- Jan Erik Solem, Programming Computer Vision with Python. O'Reilly Media, 2012. **[Solem12]**
	- Mohamed Elgendy, [Deep Learning for Vision Systems](https://www.manning.com/books/deep-learning-for-vision-systems). Manning, 2020. **[Elg20]**
	- Rafael C. Gonzalez, Richard E. Woods, Digital image processing. 4th edition. Pearson, 2018. **[Gon18]**
	- Richard Szeliski, Computer Vision: Algorithms and Applications. Springer, 2011. **[Sze11]**
	- Jason M.Kinser, Image operators: image processing in Python. CRC Press, 2019. **[Kin19]**

## Sillabo delle lezioni


| Lezione | Argomenti                                            | Materiale didattico | Data       |
| ------- | ---------------------------------------------------- | ------------------- | ---------- |
| 1       | Introduzione al corso |[Slides]({{< relref "../computervision/lecture1.md" >}}) |02/03/2021 |
| 2 | Python and image processing |[Slides, notebook]({{< relref "../computervision/lecture_lab1.md" >}}) |04/03/2021 |
| 3 | Concetti fondamentali su image processing e analysis |[Slides, notebook]({{< relref "../computervision/lecture2.md" >}}) |09/03/2021 |
| 4 | Filtri |[Slides, notebook]({{< relref "../computervision/lecture3.md" >}}) |11/03/2021 |
| 5 | Laboratorio: image processing in Python |[Slides, notebook]({{< relref "../computervision/lecture_lab2.md" >}}) |16/03/2021 |
| 6 | Filtraggio Spaziale e sulle frequenze. Edge Detection |[Slides, notebook]({{< relref "../computervision/lecture4.md" >}}) |18/03/2021 |
| 7 | Edges, lines, shapes |[Slides, notebook]({{< relref "../computervision/lecture5.md" >}}) |23/03/2021 |
| 8 | Laboratorio: Filtri, edge detection |[Slides, notebook]({{< relref "../computervision/lecture_lab3.md" >}}) |25/03/2021 |
| 9 | Introduzione alla Classification. Features |[Slides, notebooks]({{< relref "../computervision/lecture6.md" >}}) |30/03/2021, 13/04/2021, 15/04/2021 |
| 10 | Reti Neurali. Convoluzione |[Slides, notebooks]({{< relref "../computervision/lecture7.md" >}}) |20/04/2021 |
| 11 | Convoluzione. Laboratorio: SIFT, Introduzione a Pytorch |[Slides, notebooks]({{< relref "../computervision/lecture_lab4.md" >}}) |22/04/2021 |


