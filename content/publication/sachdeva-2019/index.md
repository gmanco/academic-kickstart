---
title: "Sequential Variational Autoencoders for Collaborative Filtering"
date: 2019-01-01
publishDate: 2019-09-07T09:18:44.874439Z
authors: ["Noveen Sachdeva", "Giuseppe Manco", "Ettore Ritacco", "Vikram Pudi"]
publication_types: ["1"]
abstract: "Variational autoencoders were proven successful in domains such as computer vision and speech processing. Their adoption for modeling user preferences is still unexplored, although recently it is starting to gain attention in the current literature. In this work, we propose a model which extends variational autoencoders by exploiting the rich information present in the past preference history. We introduce a recurrent version of the VAE, where instead of passing a subset of the whole history regardless of temporal dependencies, we rather pass the consumption sequence subset through a recurrent neural network. At each time-step of the RNN, the sequence is fed through a series of fully-connected layers, the output of which models the probability distribution of the most likely future preferences. We show that handling temporal information is crucial for improving the accuracy of the VAE: In fact, our model beats the current state-of-the-art by valuable margins because of its ability to capture temporal dependencies among the user-consumption sequence using the recurrent encoder still keeping the fundamentals of variational autoencoders intact."
featured: true
publication: "*Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining - WSDM ′19*"
url_pdf: "https://arxiv.org/abs/1811.09975"
url_code: 'https://github.com/noveens/svae_cf'
url_slides: 'https://www.slideshare.net/giuseppemanco/sequential-variational-autoencoders-for-collaborative-filtering'
doi: "10.1145/3289600.3291007"


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: '[**SVAE**](featured.png)'
  focal_point: ""
  preview_only: false


tags: ["Variational Autoencoders", "Recurrent Networks", "Sequence modeling","Collaborative Filtering","Deep Learning", "Recommender Systems", "Generative Models"]

---

