+++
widget = "research"  # The name of the widget that you created.
headless = true  # This file represents a page section.
#active = true  # Activate this widget? true/false
weight = 25 # Order that this section will appear in.

title = "Research Topics"
subtitle = ""


[content]
  # Page type to display. E.g. post, talk, or publication.
  page_type = "research"
  
  
  # Choose how many pages you would like to offset by
  offset = 0

  # Page order. Descending (desc) or ascending (asc) date.
  order = "desc"

  # Filter posts by a taxonomy term.
  [content.filters]
    tag = ""
    category = ""
    publication_type = ""
    exclude_featured = false

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"


[background]
  # Background color.
  color = "navy"
  
  # Background gradient.
  gradient_start = "#4bb4e3"
  gradient_end = "#2b94c3"
  
  # Background image.
  image = "background.jpg"  # Name of image in `static/img/`.
  image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  text_color_light = true

[image]
placement = 1.0
caption = "Photo by [Academic](https://sourcethemes.com/academic/)"
focal_point = "Center"
preview_only = false

+++



I am the scientific coordinator of the ICAR research group Behavioral Modeling and Scalable Analytics (formerly [ADALab: Laboratory of Advanced Analytics on Complex Data](https://www.cnr.it/it/focus/018-5/il-laboratorio-di-analitica-avanzata-su-dati-complessi-ada-lab)).


Il gruppo di ricerca si occupa di Behavior Computing & Analytics: modelli matematici e computazionalmente efficienti per l’analisi di sistemi complessi ed entità (ad esempio individui, dispositivi IoT/mobile, smart objects, etc.) che interagiscono in ambienti complessi. La BCA rappresenta una tema di ricerca importante in diversi contesti reali quali consumer profiling, social computing, computational advertising e group decision-making, cybersecurity, formazione d’opinione, smart industry, smart society, smart IoT. Con il termine “Behavior” si fa riferimento ad un’astrazione matematica efficiente che possa riassumere, descrivere e predire le azioni e reazioni intraprese da un'entità  in risposta a vari stimoli o input nel proprio ambiente naturale (pattern recognition), evidenziando anche le possibili devianze dal comportamento tipico ed atteso (anomaly detection). Il challenge è quindi cercare di comprendere la dinamica strutturale ed evolutiva dei flussi comportamentali, così da catturare/modellare i meccanismi che li governano e predire eventi ed anomalie nel breve e nel lungo periodo. 


"Le tecnologie di rifermento del gruppo di ricerca sono il probabilistic modeling ed il deep learning, sui quali è prevista sia ricerca applicativa che ricerca di base, spaziando dai latent variable models tramite probabilistic (graphical) generative models, alle tecniche di inferenza statistica, deep representation learning e constraint-based modeling (integrazione simbolico-subsimbolico) in complex domains. 
I latent variable models rappresentano lo stato dell’arte in ambiti recommendation/social network analysis/event forecasting. Questi modelli sono challenging sia dal punto di vista applicativo (utilizzarli in contesti quali l’information diffusion e information propagation o in contesti in cui la topologia dei dati conta non è banale) sia per i risvolti teorici (le tecniche attuali di apprendimento non sono adeguate). 
L’inferenza e la strutturazione di Knowledge Graphs, nonché la ricostruzione delle relazioni che li caratterizzano rappresenta un tema di grande interesse e con notevoli risvolti applicativi: ad esempio, nell’ambito della recommendation, il knowledge graph amplia l’ammontare di informazione disponibile, rafforzando così le connessioni tra le entità coinvolte e supportando diversità e explainability dei risultati della raccomandazione.
Il problema di rendere la modellazione e profilazione dipendente da vincoli di dominio è un aspetto estremamente challenging che permetterebbe di combinare aspetti di reasoning ad aspetti di apprendimento. Di fatto, gli attuali modelli matematici possono essere considerati “statici”, poiché sono adattamenti del supervised learning tradizionale. Da questo punto di vista, è necessario studiare come i modelli statici possano essere migliorati rendendoli calibrati ai vari aspetti e vincoli di sistema da considerare. 
Particolare rilevanza avrà lo studio di tecniche ed approcci di Anomaly Detection basata su analisi comportamentale per il monitoraggio di sistemi complessi (ad es. reti di calcolatori, reti sociali, processi industriali, reti di sensori per il monitoraggio ambientale ed energetico, etc.). L’obiettivo è comprendere il comportamento del sistema sotto analisi e rilevare eventi inattesi od anomali così da prevenirli o, qualora non sia possibile prevederli, identificarli prontamente ed attivare l’insieme di contromisure più efficaci per limitarne gli impatti. Il focus sarà posto su due aspetti fondamentali. Da un lato, la necessità di garantire adeguati livelli di efficienza in domini in cui le quantità dei dati da elaborare sono massive (ad esempio, a partire da algoritmi sviluppati basati sul concetto di solving set, utilizzabili anche in scenari multicore e/o manycore per gestire dati nativamente distribuiti e/o necessitanti di grandi risorse di calcolo). Da un altro lato, il comportamento delle entità operanti nel sistema in analisi può cambiare/evolvere nel tempo (concept drift), per cui i modelli sviluppati devono essere in grado di adattarsi rapidamente a tali cambiamenti ma nel contempo essere in grado rilevare anomalie in maniera stabile."




