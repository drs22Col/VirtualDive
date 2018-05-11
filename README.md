# Visualizing Our Planet's Coral Reefs

PDSB project to create a bokeh app that visualizes over 10,500 reefs around the world and their name, reef type, predicted species composition, country, and GPS coordinates over Google Maps. Because this project is primarily meant to be a tutorial, users will primarily interact with Jupyter Notebooks. The primary notebook that users should interact with is **2-Example-Bokeh-App-VirtualDive.ipynb**.

To clone and run Jupyter Notebooks locally, clone this repo using

`git clone https://github.com/mistergroot/VirtualDive.git`

and navigate to the notebooks folder.

**Dependencies**:

Prior to running any notebooks, please install `bokeh`, `colorcet`, `pandas`, and `numpy` through `conda` by running the following command in your terminal:

`conda install bokeh colorcet pandas numpy`

To run through the entire process of creating a functional Bokeh app, following the following notebooks in this order:

1. `1-Download-Data-And-Cleaning.ipynb`
2. `2-Example-Bokeh-App-VirtualDive.ipynb`
3. `3-Embedding-With-Heroku.ipynb`

The rest of the notebooks in `./notebooks` are notebooks that are being actively developed. Don't view these unless you'd like to see my messy workflow and the inner workings of my mind (believe me, nobody wants that).

To view the fully completed (as of the deadline 5/11 - development will be continuing after this date) and embedded Bokeh app (through Heroku), VirtualDive, please visit this hidden and unfinished portion of my website:

http://www.locatelliphotography.com/new-page-1

I have a free Heroku account so the server is only active for part of the day. The server sleeps from 12am to 6am PST so if you visit during that time period it will take a while to load as the server has to wake up.

<span style="color:red">**NOTE: Because of an issue with the Google Maps API, the 180th Meridian (around Fiji) cannot be in the frame otherwise the glyphs all shift or disappear. If you pan towards Hawaii, the glyphs will disappear until the 180th Meridian is out of frame. Please keep this in mind when interacting with this example Bokeh app. This is a limitation with Google Maps API, not with Bokeh. I will fix this by switching over to a WMTS XYZ Tile Source in the future.**</span>