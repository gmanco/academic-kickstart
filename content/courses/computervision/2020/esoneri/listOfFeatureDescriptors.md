---
title: Esonero 1
linktitle: Esonero 1
toc: false
type: docs
date: "2020-04-02T00:00:00+01:00"
draft: false


# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 100
---

#  Feature descriptors

In questo esonero è chiesto agli studenti di sperimentare con un feature descriptr tra quelli elencati in seguito. In particolare si chiede di: 

- Scegliere un feature descriptor
- Preparare delle slides dettagliate (max 15) che lo descrivono
- Preparare un notebook in cui: 
	- si implementa l'algoritmo che sta alla slide 62 (istogramma basato sui feature descriptors) 
	- si applica la regressione logistica (da scikit-learn) sul set di immagini (MNIST)
	- si valutano i risultati della classificazione confrontandoli con la regressione logistica applicata alla flattenizzazione raw dell'immagine (opportunamente preprocessata). 

Gli studenti interessati ad effettuare l'esonero dovranno mandare una mail al docente indicando, in ordine di priorità, tre scelte dalla lista di cui sotto.
Le assegnazioni verranno comunicate a lezione. La deadline per la consegna degli elaborati è il **16 aprile 2020**.




## OpenCV

Tutorials disponibili [qui](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html).


1. [SIFT](https://docs.opencv.org/4.2.0/d5/d3c/classcv_1_1xfeatures2d_1_1SIFT.html), Class for extracting keypoints and computing descriptors using the Scale Invariant Feature Transform ([SIFT](https://docs.opencv.org/4.2.0/d5/d3c/classcv_1_1xfeatures2d_1_1SIFT.html)) algorithm by D. Lowe. Riferimenti: David G Lowe. [Distinctive image features from scale-invariant keypoints](https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf). *International journal of computer vision*, 60(2):91–110, 2004.
2. [SURF](https://docs.opencv.org/4.2.0/d5/df7/classcv_1_1xfeatures2d_1_1SURF.html), Class for extracting Speeded Up Robust Features from an image. Riferimenti: Herbert Bay, Tinne Tuytelaars, and Luc Van Gool. [Surf: Speeded up robust features](http://scholar.google.it/scholar_url?url=https://lirias.kuleuven.be/retrieve/78517&hl=it&sa=X&scisig=AAGBfm2HNoDAKFbI70IQ22ndV5cBLu7pBw&nossl=1&oi=scholarr). *Computer Vision–ECCV 2006*, pages 404–417, 2006.
3. [AKAZE](https://docs.opencv.org/4.2.0/d8/d30/classcv_1_1AKAZE.html), Class implementing the [AKAZE](https://docs.opencv.org/4.2.0/d8/d30/classcv_1_1AKAZE.html) keypoint detector and descriptor extractor. Riferimenti: Pablo F Alcantarilla, Jesús Nuevo, and Adrien Bartoli. [Fast explicit diffusion for accelerated features in nonlinear scale spaces](http://www.bmva.org/bmvc/2013/Papers/paper0013/paper0013.pdf). *Trans. Pattern Anal. Machine Intell*, 34(7):1281–1298, 2011.
4. [Brisk](https://docs.opencv.org/4.2.0/de/dbf/classcv_1_1BRISK.html), Class implementing the [BRISK](https://docs.opencv.org/4.2.0/de/dbf/classcv_1_1BRISK.html) keypoint detector and descriptor extractor. [Stefan Leutenegger, Margarita Chli, and Roland Yves Siegwart. [Brisk: Binary robust invariant scalable keypoints](https://www.researchgate.net/publication/221110715_BRISK_Binary_Robust_invariant_scalable_keypoints). In *Computer Vision (ICCV), 2011 IEEE International Conference on*, pages 2548–2555. IEEE, 2011.
5. [Mser](https://docs.opencv.org/4.2.0/d3/d28/classcv_1_1MSER.html), Maximally stable extremal region extractor, for grey scale and color image. Riferimenti: David Nistér and Henrik Stewénius. [Linear time maximally stable extremal regions](https://www.researchgate.net/publication/221304597_Linear_Time_Maximally_Stable_Extremal_Regions). In *Computer Vision–ECCV 2008*, pages 183–196. Springer, 2008.; Per-Erik Forssén. Maximally stable colour regions for recognition and matching. In *Computer Vision and Pattern Recognition, 2007. CVPR'07. IEEE Conference on*, pages 1–8. IEEE, 2007.
6. [ORB](https://docs.opencv.org/4.2.0/db/d95/classcv_1_1ORB.html), The algorithm uses FAST in pyramids to detect stable keypoints, selects  the strongest features using FAST or Harris response, finds their  orientation using first-order moments and computes the descriptors using BRIEF (where the coordinates of random point pairs (or k-tuples) are  rotated according to the measured orientation). Riferimenti: Ethan Rublee, Vincent Rabaud, Kurt Konolige, and Gary Bradski. [Orb: an efficient alternative to sift or surf](http://www.willowgarage.com/sites/default/files/orb_final.pdf). In *Computer Vision (ICCV), 2011 IEEE International Conference on*, pages 2564–2571. IEEE, 2011.


## SK-Image

Documentation at the home page of the [scikit-image feature description package](https://scikit-image.org/docs/0.16.x/api/skimage.feature.html).

1. `skimage.feature.daisy`, Extract DAISY feature descriptors densely for the given image. DAISY is a feature descriptor similar to SIFT formulated in a way that allows for fast dense extraction. Typically, this is practical for bag-of-features image representations. Riferimenti: Tola et al. [Daisy: An efficient dense descriptor applied to wide- baseline stereo](https://infoscience.epfl.ch/record/138785/files/tola_daisy_pami_1.pdf). Pattern Analysis and Machine Intelligence, IEEE Transactions on 32.5 (2010): 815-830.]
2. `skimage.feature.hog`, Extract Histogram of Oriented Gradients (HOG) for a given image. Riferimenti: Dalal, N and Triggs, B, [Histograms of Oriented Gradients for Human Detection](https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf), IEEE Computer Society Conference on Computer Vision and Pattern Recognition 2005 San Diego, CA, USA, DOI:10.1109/CVPR.2005.177]
3. `skimage.feature.local_binary_pattern`, Gray scale and rotation invariant LBP (Local Binary Patterns). Riferimenti: Timo Ojala, Matti Pietikainen, Topi Maenpaa. [Multiresolution Gray-Scale and Rotation Invariant Texture Classification with Local Binary Patterns]( http://www.ee.oulu.fi/research/mvmp/mvg/files/pdf/pdf_94.pdf). 2002]
4. `skimage.feature.haar_like_feature`, Compute the Haar-like features for a region of interest (ROI) of an integral image. Riferimenti: Messom, Christopher H. and Andre L. C. Barczak. [Stream processing for fast and efficient rotated Haar-like features using rotated integral images](https://www.semanticscholar.org/paper/Stream-processing-for-fast-and-efficient-rotated-Messom-Barczak/b55e215acd9bc0496f1f611d6193fea0b10e4212). *IJISTA* 7 (2006): 40-57. 
5. `skimage.feature.BRIEF`, BRIEF binary descriptor extractor. BRIEF (Binary Robust Independent Elementary Features) is an efficient feature point descriptor. It is highly discriminative even when using relatively few bits and is computed using simple intensity difference tests. Riferimenti: Calonder, Michael & Lepetit, Vincent & Strecha, Christoph & Fua, Pascal. (2010). [BRIEF: Binary Robust Independent Elementary Features](https://www.cs.ubc.ca/~lowe/525/papers/calonder_eccv10.pdf). Eur. Conf. Comput. Vis.. 6314. 778-792. 10.1007/978-3-642-15561-1_56.  
6. `skimage.feature.ORB`, Oriented FAST and rotated BRIEF feature detector and binary descriptor extractor. Riferimenti: Ethan Rublee, Vincent Rabaud, Kurt Konolige and Gary Bradski. [ORB: An efficient alternative to SIFT and SURF](http://www.vision.cs.chubu.ac.jp/CV-R/pdf/Rublee_iccv2011.pdf). 

## 

#  Assegnazioni

- Giulia Katia Galimberti  **SIFT** (OpenCV)
- Maria Francesca Alati  **skimage.feature.hog**
- Lorenzo Defina  **Mser** (OpenCV)
- Emilio Casella  **Surf** (OpenCV)
- Simona Nisticò matricola **ORB** (OpenCV)
- Domenico Montesanto **AKAZE** (OpenCV)
- Caterina Maugeri **skimage.feature.local_binary_pattern**
- Giuseppe Surace  **skimage.feature.haar_like_feature**
- Antonello Crea **Daisy** (OpenCV)
- Anile Anna  **skimage.feature.BRIEF** 
- Vincenzo Parrilla  **SURF with Harris Corner Detection**. (OpenCV)
- Davide Medaglia **SIFT with Harris Corner Detection** (OpenCV)
- Antonio Commisso **Brisk** (OpenCV)
- Antonio Gagliostro: **skimage.feature.ORB** 

# Risultati

| Studente               | Voto |
| ---------------------- | ---- |
| Alati Maria  Francesca | 8    |
| Anile Anna             | 8    |
| Casella Emilio         | 7    |
| Commisso Antonio       | 7    |
| Crea Antonello         | 10   |
| Defina Lorenzo         | 6    |
| Gagliostro Antonio     | 9    |
| Galimberti Giulia      | 5    |
| Maugeri Caterina       | 8    |
| Medaglia Davide        | 8    |
| Montesanto Domenico    | 7    |
| Nisticò Simona         | 9    |
| Parrilla Vincenzo      | 7    |
| Surace Giuseppe        | 4    |