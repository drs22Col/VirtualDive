# Project Proposal

### 1) **The problem** 

Based on my searches, there are currently no programs that makes it easy for scientists to download publicly accessible oceanographic data from PacIOOS and run larval simulations and visualize them. Thus, my goal is to create a program that scrapes the data and outputs formatted data into the LarvalDispersal class of the GeoEco package (http://code.env.duke.edu/projects/mget). 

### 2) **The data**

This project will make use of the ocean currents forecasts of Samoa from the Pacific Island Ocean Observing System (PacIOOS). The PacIOOS has fine-scale forecasts of ocean currents but does not have actual observed surface ocean currents for the region. If possible, the data of PacIOOS will be compared with the lower resolution (0.33 degree x 0.33 degree spatial resolution - 5 day temporal resolution) data from NASA JPL's OSCAR to verify that the predictions from both systems are in agreement. 

### 3) **The tools**

To achieve these goals, I will be using the `requests` Python tool to web scrape the data from ERDDAP (the PacIOOS's data access site). This data will then be formatted by a class object called `larvalformat` that I create as part of this project. After this, the project will largely be a pipeline in which I pipe the outputs of the `requests` and `larvalformat` into `RunSimulation` of the LarvalDispersal class from the GeoEco package. The outputs of `RunSimulation` will then be piped into a data visualization software that has not yet been chosen. The GeoEco package has been created for use with ArcGIS Desktop 9.2 and up and I would like to make this project be entirely open-access and free so I will likely be changing the code to make use of GQIS or something similar.

### 4) **The novelty**

No publication or program that I know of makes use of fine-scale forecast data from sources like PacIOOS. The main source of novelty in this proposal is the usage of the data. I would like to make it so the class object I create for web scraping and formatting data can download data from any user-defined publicly accessible oceanographical data source. For now I will be focusing my efforts on PacIOOS since it is the only source of data that has high-resolution ocean current forecasts of my study region (American Samoa).

### 5) **The goal**

