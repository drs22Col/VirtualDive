# Project Proposal

### 1) **The problem** 

As part of my master's thesis, I seek to understand the population genetics of *Acropora formosa* and *Porites lobata* in the context of physical oceanography. In order to run approximate Bayesian computation on the genetic data (which will be collected over the summer and sequenced in the fall), I must have first have an understanding of the dispersal of coral larvae throughout the study area (American Samoa). Based on my searches, there are currently no programs that make it easy for scientists to download publicly accessible oceanographic data from the Pacific Island Ocean Observing System (PacIOOS) and run larval simulations and visualize them. Thus, my goal is to create a program that scrapes the data from PacIOOS and outputs formatted data into the LarvalDispersal class of the GeoEco package (http://code.env.duke.edu/projects/mget). 

### 2) **The data**

This project will make use of the high-resolution (1.9mi spatial resolution - 3 hourly temporal resolution) ocean currents forecasts of Samoa from PacIOOS. If possible, the data from PacIOOS will be compared with the lower resolution (0.33 degree x 0.33 degree spatial resolution - 5 day temporal resolution) data from NASA JPL's OSCAR to verify that the predictions from both systems are in agreement. 

### 3) **The tools**

To achieve these goals, I will be using the `requests` Python tool to web scrape the data from ERDDAP (the PacIOOS's data access site). This data will then be formatted by a class object called `larvalformat` that I create as part of this project. After this, the project will largely be a pipeline in which I pipe the outputs of the `requests` and `larvalformat` into `RunSimulation` of the LarvalDispersal class from the GeoEco package. The outputs of `RunSimulation` will then be piped into a data visualization software that has not yet been chosen. The GeoEco package has been created for use with ArcGIS Desktop 9.2 and up and I would like to make this project be entirely open-access and free so I will likely be changing the code to make use of GQIS or something similar.

### 4) **The novelty**

No publication or program that I know of makes use of fine-scale forecast data from sources like PacIOOS. The main source of novelty in this proposal is the usage of the data. I would like to make it so the class object I create for web scraping and formatting data can download data from any user-defined publicly accessible oceanographical data source. For now I will be focusing my efforts on PacIOOS since it is the only source of data that has high-resolution ocean current forecasts of my study region (American Samoa).

### 5) **The goal**

By the due date, I would like to have a program created that will webscrape data from PacIOOS, format it for use with GeoEco, pipe the data into `RunSimulation`, and pipe the resulting data into a visualization software. The program I create in this class will be used as part of my master's thesis project on the population genetics of *Acropora formosa* and *Porites lobata* in American Samoa. The goal is to have a publication by early 2019 that includes figures created by this package. In the future, I intend on expanding the program I build for this class to make use of all publicly accessible oceanographic datasets. Combining physical oceanography with biogeography will be a large part of my career and I believe that creating a program that is easily understood by users and that simulates dispersal is extremely important for informing conservation efforts in corals.