---
title: Adversarial Games for generative modeling of Temporally-Marked Event Sequences
event: ISI Informal Workshop on Learning, Algorithms and Networks 
event_url: http://www.francescobonchi.com/workshop0220.pdf
location: Torino, Italy
summary: I discuss some issues and solutions in devising generative models for marked temporal poin processes.
abstract: "Increasing amounts of data are becoming available in the form of “asynchronous” sequences of event records, associated each with a content and a temporal mark, e.g. sequences of activities on social media, clickstream data, user interaction logs, point-of-interest trajectories, business process logs, application logs and IoT logs, to name a few. Such a kind of data are more general than classic time series, as the lapse of time between consecutive events in a sequence may be an arbitrary continuous value. Usually, events in the same sequence exhibit hidden correlations (e.g., an event can cause or prevent the occurrence of certain kinds of events in the future). Generative models constitute a powerful and versatile means for analysing such data (e.g., by supporting variegate key tasks, such as data completion, data denoising, simulation analyses), as well as for enabling the very generation of new data instances (e.g., for preventing information leakage). In particular, if devised in a conditional fashion, these models can be exploited to predict which events will happen in the remainder of a given (unfinished) sequence and when, based on the sequence’s history. Different kinds of neural generative models have been used in the last years for analysing sequence data, which range from Recurrent Neural Networks (RNNs), to Self- attention models, to more sophisticated frameworks like Variational Auto-encoders (VAEs) and Generative Adversarial Networks (GANs). In particular, basic GAN frameworks implement a sort min-max game, where a “discriminator” sub-net is trained to distinguish real data instances from those produced by a “generator” sub-net, which is trained instead to fool the former sub-net."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2020-02-18T11:00:00Z"
date_end: "2020-02-18T12:00:00Z"
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2017-01-01T00:00:00Z"

authors: []
tags: [Point Processes,Generative models]

# Is this a featured talk? (true/false)
featured: false

image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  focal_point: Right

links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/beman70
url_code: ""
url_pdf: ""
url_slides: "talk_ISI_feb20.pdf"
url_video: ""

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
#slides: example

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
#- internal-project

# Enable math on this page?
math: true
---


