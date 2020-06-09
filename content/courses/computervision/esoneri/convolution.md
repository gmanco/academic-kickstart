---
title: Esonero 2
linktitle: Esonero 2
toc: false
type: docs
date: "2020-04-28T00:00:00+01:00"
draft: false


# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 200

---

#  Convolutional Neural Networks

In questo esonero è chiesto agli studenti di studiare le reti convoluzionali. 

- Scegliere un topic
- Preparare delle slides dettagliate (max 15) che lo descrivono
- Preparare un notebook in cui: 
  - si implementa quello che è richiesto
  - si illustrano i  risultati e la loro valutazione

Gli studenti interessati ad effettuare l'esonero dovranno mandare una mail al docente indicando, in ordine di priorità, tre scelte dalla lista di cui sotto.
Le assegnazioni verranno comunicate a lezione. La deadline per la consegna degli elaborati è il **10 maggio 2020**.



## GoogLeNet

1. Scegliere una delle seguenti varianti di GoogLeNet e implementarla, riaddestrando la rete su CIFAR-10 e mostrando i risultati. 
   - Utilizzare i layer di batch normalization [[Ioffe & Szegedy, 2015\]](https://d2l.ai/chapter_references/zreferences.html#ioffe-szegedy-2015)
   - Effettuare gli aggiustamenti all'inception block suggeriti in [[Szegedy et al., 2016\]](https://d2l.ai/chapter_references/zreferences.html#szegedy-vanhoucke-ioffe-ea-2016).
   - effettuare gli aggiustamenti alle residual connections suggerite in [[Szegedy et al., 2017\]](https://d2l.ai/chapter_references/zreferences.html#szegedy-ioffe-vanhoucke-ea-2017),
2. Qual'è la dimensione minima richiesta per l'immagine di input in GoogLeNet?

- Ioffe, S., & Szegedy, C. (2015). Batch normalization: accelerating deep network training by reducing internal covariate shift. *arXiv preprint arXiv:1502.03167*.
- Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., & Wojna, Z. (2016). Rethinking the inception architecture for computer vision. *Proceedings of the IEEE conference on computer vision and pattern recognition* (pp. 2818–2826).
- Szegedy, C., Ioffe, S., Vanhoucke, V., & Alemi, A. A. (2017). Inception-v4, inception-resnet and the impact of residual connections on learning. *Thirty-First AAAI Conference on Artificial Intelligence*.



## ResNet

1. Nelle versioni successive di ResNet, gli autori hanno cambiato l'architettura da “convolution, batch normalization, activation” in “batch normalization, activation, convolution”. Studia gli effetti di questo cambiamento nell'implementazione proposta in classe, ristrutturando la rete e riaddestrandola su CIFAR-10. [[He et al., 2016](https://arxiv.org/abs/1603.05027)]
2. Qual'è la dimensione minima richiesta per l'immagine di input in ResNet ?

- He, K., Zhang, X., Ren, S., & Sun, J. (2016). Identity mappings in deep residual networks. European conference on computer vision (pp. 630–645).



## Saliency Maps using Flashtorch

Studiare l'articolo [[Simonyan et al, 2014](https://arxiv.org/pdf/1312.6034.pdf)] e il package [flashtorch](https://github.com/MisaOgura/flashtorch) e usalo su alcune reti preaddestrate (VGG16, GoogLeNet, ResNet).

- Karen Simonyan, Andrea Vedaldi, Andrew Zisserman. Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps. ICLR2014
- [Visualize image specific class saliency with backprop](https://github.com/MisaOgura/flashtorch/blob/master/examples/visualize_saliency_with_backprop.ipynb)



## Alternative alla Batch Normalization

Prendere come riferimento la rete VGG16. Si studino gli effetti della normalizzazione riaddestrando la rete su CIFAR-10: 

1. Aggiungendo Batch Normalization
2. Aggiungendo Local Response Normalization
3. Implementando la tecnica di Group Normalization descritta in [[Wu et al, 2018](https://arxiv.org/pdf/1803.08494.pdf)]

- Y. Wu, K. He. Group Normalization. 
- [An alternative to Batch Normalization](https://towardsdatascience.com/an-alternative-to-batch-normalization-2cee9051e8bc)



#  Assegnazioni

- Costa Davide **Alternative alla Batch Normalization**
- Azzato Saverio **GoogleLeNet (aggiustamenti all’inception block)**
- Sergi Alfredo **GoogLeNet (aggiustamenti alle residual connection)**
- De Prete Alessandra **Saliency Maps using Flashtorch** 
- Prospero Papaleo **ResNet** 
- Lavecchia Umberto Mattia **GoogLeNet (con studio sulla batch normalization)**

# Risultati

| Studente             | Voto |
| -------------------- | ---- |
| Azzato Saverio       | 7    |
| Costa Davide         | 10   |
| Del Prete Alessandra | 10   |
| Lavecchia Mattia     | 5    |
| Papaleo Prospero     | 6    |
| Sergi Alfredo        | 7    |