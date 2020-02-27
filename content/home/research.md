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


The main focus of the research group is Behavior Computing and Analytics: that is, computationally efficient mathematical models for analysing complex systems and entities which interact within complex systems. Example include individuals, IoT Devices and sensors, Smart Object, etc. Behavior analytics is an important topic in different contexts including: consumer profiling, social computing, computational advertising and group-decision making, cybersecurity, opinion modeling, smart industry. The term "Behavior" refers to actions and reactions of any individual, in response to various stimuli or inputs. The recent advent of technologies for collecting and tracking behavioral data at large scale, has made it possible to devise new mathematical models that allow to analyse, understand, and predict actions. These include models for event streams, social network connections, purchasing habits and opinion formation. The main challenge is hence to understand structure and evolution dynamics of events, in a way that allows to disclose the latent mechanism which govern them and enact predictive abilities both on the short and long term. 

The research agenda includes the study of probabilistic generative models and statistical inference, deep representation learning and constraint-based modeling (which encompasses integration of symbolic-subsymbolic learning). In particular our focus is on the following themes.

- **Latent variable models** are among the most prominent tools for recommendation and social network analysis. Such tools can be especially fruitful in context such as (i) information diffusion, i.e. devising how information flows within a network of individuals; (ii) influence propagation, i.e. to identify the hidden factors explaining why, on the basis of his/her experience, a given subject is sensitive to specific informative content; (iv) recommendation, i.e. improving user experience within a specific situation by understanding the patterns governing the user’s choices. 
- Understanding the **structural, topical and temporal dynamics of user behavior**  can provide insights on the complex patterns that govern the information propagation process and it can be used to forecast future events. Designing new methods that can both model their dynamics and predict future behavior is crucial in many domains, including: Medical events (where the focus is on sequences of acute incidents, doctor’s visits, tests, diagnoses, and medications, Consumer behavior (purchasing patterns), “Quantified self” data (such as wearable devices and apps to record eating, traveling, working, sleeping, waking) , Social media actions (previous posts, shares, comments, messages, etc.), smart cities and mobility patterns (trajectories, taxi/car/public transportation adoptions, etc.).  
- The capability to **infer complex representations**, as well as latent relationships among entities, enables a more powerful approach to information analytics. For example, within Recommender Systems, the adoption of more complex representations (such as Knowledge Graphs) extends the amount of information available, thus strengthening the connections among entities thus supporting more precise modeling, diversity and explainability.
- Similarly, **injecting domain constraints within machine learning** allows to combine reasoning and learning, thus calibrating the resulting predictive and descriptive models to more realistic situations where bias and/or inaccuracies can be avoided. 
- Contributions to **Security Intelligence** include the development of techniques for 1) security analytics, based on behavioral profiling, to detect malicious activities and devise models of trust; 2) social sensing for prediction of sensitive information diffusion flows and secure information sharing; 3) attack prevention/response based on machine learning and AI to improve reaction to incidents; 4) privacy-preserving information handling based on theoretically guaranteed models of privacy.




