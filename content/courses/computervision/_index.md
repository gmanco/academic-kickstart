---
# Course title, summary, and position.
linktitle: Analisi di Immagini e Video (Computer Vision)
summary: Il corso mira a fornire solide basi in merito all’analisi di immagini e video e fornire una conoscenza delle principali tecniche di deep learning per il riconoscimento di oggetti e l’individuazione di sequenze rilevanti in un video. 


weight: 1

# Page metadata.
title: Panoramica
date: "2020-02-26T00:00:00Z"
lastmod: "2020-04-18T00:00:00Z"
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

- **[01/07/2020]** Rilasciate le [specifiche]({{< relref "../computervision/progetti/project2_spec.md" >}}) progetto per esame del 31/07/2020. La consegna degli elaborati deve avvenire il 29/07/2020. 
- **[09/06/2020]** Rilasciate le [specifiche]({{< relref "../computervision/progetti/project1_spec.md" >}}) progetto per esame del 01/07/2020. La consegna degli elaborati deve avvenire il 28/06/2020. 
- **[08/06/2020]** E disponibile la valutazione del secondo esonero, nalla rispettiva [pagina]({{< relref "../computervision/esoneri/convolution.md" >}}). 
- **[07/05/2020]** E disponibile la valutazione del primo esonero, nalla rispettiva [pagina]({{< relref "../computervision/esoneri/listOfFeatureDescriptors.md" >}}). 
- **[28/04/2020]** E disponibile la lista degli argomenti per il secondo esonero. La lista è disponibile [qui]({{< relref "../computervision/esoneri/convolution.md" >}}). Gli studenti che selgono di effettuare l'esonero devono concordare l'opzione con il docente tramite email. La deadline per la consegna degli elaborati è il 10 maggio 2020.
-  **[02/04/2020]** E disponibile la lista degli argomenti per il primo esonero. La lista è disponibile [qui]({{< relref "../computervision/esoneri/listOfFeatureDescriptors.md" >}}). Gli studenti che selgono di effettuare l'esonero devono comunicare le opzioni (3) al docente. Martedì 7 verrà comunicata l'assegnazione dei topic ai vari studenti. La deadline per la consegna degli elaborati è il 16 aprile 2020. 
- **[03/03/2020]** Si avvisano gli studenti che il corso di Analisi di Immagini e Video – Corso di Laurea Magistrale in Ingegneria Informatica verrà erogato in modalità streaming, utilizzando l’applicativo TEAMS, a partire dal giorno 17/03/2019, alle ore 8:30. La richiesta di iscrizione al corso può essere effettuata cliccando sul seguente [link](https://teams.microsoft.com/l/channel/19%3ac60bff4a6e874db3b5e0d2034412ed18%40thread.tacv 2/Generale?groupId=b4509060-7b45-4eab-80ce-55182356fb88&tenantId=7519d0cd-2106-47d9- adcb-320023abff57). Gli studenti già pratici dell’utilizzo di TEAMS e che abbiano già scaricato l’APP, possono iscriversi direttamente al corso (senza approvazione del docente) utilizzando il codice: **khm7h4s**




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
	-	Deep Learning: Review su Neural Networks per l'analisi di immagini e video. Convolutional Neural Networks. Reti ricorrenti. R-CNN. Gestione dell'overfitting.
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
| 1       | Introduzione al corso |[Slides]({{< relref "../computervision/lecture1.md" >}}) |17/03/2020 |
| 2       | Concetti fondamentali su Image processing e analysis |      [Slides, notebook]({{< relref "../computervision/lecture2.md" >}})               |19/03/2020 |
| 3       | Filtri |      [Slides, notebook]({{< relref "../computervision/lecture3.md" >}})               |24/03/2020 |
| 4       | Laboratorio 1: Image Processing in Python |      [Slides, notebook]({{< relref "../computervision/lecture_lab1.md" >}})               |26/03/2020 |
| 5       | Edge detection. Fourier Transform |      [Slides, notebook]({{< relref "../computervision/lecture4.md" >}})               |31/03/2020 |
| 6       | Classificazione. Feature detection & Description |      [Slides]({{< relref "../computervision/lecture5.md" >}}).    [Esonero]({{< relref "../computervision/esoneri/listOfFeatureDescriptors.md" >}})      |02/04/2020 |
| 7       | Laboratorio 2: sklearn. Pytorch |      [Slides, notebook]({{< relref "../computervision/lecture_lab2.md" >}})               |07/04/2020 |
| 8       | Modelli non lineari. CNN |      [Slides, notebook]({{< relref "../computervision/lecture6.md" >}})               |16/04/2020, 21/04/2020 |
| 10 | Laboratorio 3: Architetture CNN, data augmentation, transfer learning | [Slides, notebook]({{< relref "../computervision/lecture_lab3.md" >}}) |23/04/2020 |
| 11 | Object Detection. Region Proposal Networks, Single-Shot Detection. Yolo. | [Slides, notebooks]({{< relref "../computervision/lecture7.md" >}}) |28/04/2020, 30/04/2020 |
| 12 | Laboratorio 4: Object Detection | [Notebook]({{< relref "../computervision/lecture_lab4.md" >}}) |05/05/2020 |
| 13 | Segmentazione | [Slides, notebooks]({{< relref "../computervision/lecture8.md" >}}) |07/05/2020, 12/05/2020, 14/05/2020 |
| 14 | Action Recognition | [Slides, notebooks]({{< relref "../computervision/lecture9.md" >}}) |19/05/2020 |
| 15 | Modelli generativi. Variational Autoencoders | [Slides, notebooks]({{< relref "../computervision/lecture10.md" >}}) |21/05/2020 |
| 16 | Generative Adversarial Networks. Image translation | [Slides, notebooks]({{< relref "../computervision/lecture11.md" >}}) |26/05/2020, 28/05/2020 |
| 17 | Laboratorio 5: Generative Adversarial Networks | [Slides, notebook]({{< relref "../computervision/lecture_lab5.md" >}}) |04/06/2020 |


