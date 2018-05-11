# Visualizing Our Planet's Coral Reefs

PDSB project to create a bokeh app that visualizes over 10,500 reefs around the world and their name, reef type, predicted species composition, country, and GPS coordinates. Because this project is primarily meant to be a tutorial, users will primarily interact with Jupyter Notebooks. The most up-to-date and functional notebook is **VirtualDive-NASAdata.ipynb**.

To clone and run Jupyter Notebooks locally, clone this repo using

`git clone https://github.com/mistergroot/VirtualDive.git`

and navigate to the notebooks folder.

**Dependencies**:

Prior to running the aforementioned notebook, please install bokeh and colorcet by running:

`conda install bokeh colorcet`

To view the fully completed (as of the deadline 5/11 - development will be continuing after this date) and embedded Bokeh app, VirtualDive, please visit this hidden and unfinished portion of my website:

http://www.locatelliphotography.com/new-page-1

**NOTE: Due to an issue with the Google Maps API, if the 180th meridian is found in the frame of the map, all glyphs will shift/disappear until the 180th meridian is out of the frame. In other words, to test out the app, try not to pan towards Hawaii from the starting frame, only towards Africa**
