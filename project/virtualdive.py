from bokeh.io import curdoc
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, Annulus, Legend, LegendItem,
    Range1d, PanTool, WheelZoomTool, CustomJS, HoverTool, TapTool
)
from bokeh.models.mappers import CategoricalColorMapper, LogColorMapper
from colorcet import bkr as palette, fire as fire
import pandas as pd
import numpy as np

#Download Data

protected = pd.read_csv("protected.csv")
unprotected = pd.read_csv("unprotected.csv")
data = pd.read_csv("popdata.csv")

protectedsource = ColumnDataSource(
    data=dict(
        lat=protected['LAT'],
        lon=protected['LON'],
        color=protected['PROTECTED'],
        reefnames=protected.REEF_NAME.tolist(),
        reeftype=protected.REEF_TYPE.tolist(),
    )
)

unprotectedsource = ColumnDataSource(
    data=dict(
        lat=unprotected['LAT'],
        lon=unprotected['LON'],
        color=unprotected['PROTECTED'],
        reefnames=unprotected.REEF_NAME.tolist(),
        reeftype=unprotected.REEF_TYPE.tolist(),
    )
)

popsource = ColumnDataSource(
    data=dict(
        poplat=data['lat'],
        poplon=data['lon'],
        colorpop=data['popdens'],
    )
)

map_options = GMapOptions(lat=7.2, lng=122, scale_control=True, map_type="satellite", zoom=4)

url = "https://www.google.com/search?q=butt&oq=butt&aqs=chrome..69i57j69i60j0l4.1565j0j1&client=ubuntu&sourceid=chrome&ie=UTF-8"

cb_code = """
var ind = source.selected['1d'].indices;
var data = source.data;
console.log(source['z'][ind])
"""
tap = TapTool(name="foo", callback = CustomJS(args=dict(source=protectedsource), code = cb_code))

zoom = WheelZoomTool()

hover = HoverTool(names=["foo"], tooltips="""
    <HTML>
    <HEAD>
    <style>    
    .bk-tooltip {
        background-color: black !important;
        }
    </style>
    </HEAD>
    <BODY>
    <div class = ".bk-tooltip">
        <div>
            <span style="font-size: 12px; font-weight: bold; color: white;">@reefnames</span>
        </div>
        <div>
            <span style="font-size: 10px;color: white;">@reeftype Reef</span>
        </div>
        <div>
            <span style="font-size: 10px; color: #696;">(@lat, @lon)</span>
        </div>
    </div>
    </BODY>
    </HTML>
    """)

pan = PanTool(dimensions="both")

plot = GMapPlot(
    x_range=Range1d(-160, 160), 
    y_range=Range1d(-80, 80), 
    map_options=map_options, 
    sizing_mode='stretch_both',
    tools=[hover, tap, zoom, pan]
)

plot.title.text = "VirtualDive"
plot.title.text_font_size = "25px"
plot.title_location="right"
plot.title.align = "right"
plot.api_key = "AIzaSyAX0RhQ5JTdQAjveEADHzBXbxkVLYCiPps"

#color_mapper = CategoricalColorMapper(factors=['hi', 'lo'], palette=[RdBu3[2], RdBu3[0]])
#color_mapper = LogColorMapper(palette="Viridis5", low=min_median_house_value, high=max_median_house_value)

paletteinvert = palette[::-1]

color_mapper = CategoricalColorMapper(palette=["magenta", "cyan"], factors=['No','Yes'])
color_mapper2 = LogColorMapper(palette=fire)

protectedannulus = Annulus(x="lon", 
                y="lat", 
                inner_radius=4000,
                outer_radius=7000,
                fill_color="cyan",
                fill_alpha=0.3, 
                line_color=None)

unprotectedannulus = Annulus(x="lon", 
                y="lat", 
                inner_radius=4000,
                outer_radius=7000,
                fill_color={'field': 'color', 'transform': color_mapper},
                fill_alpha=0.3, 
                line_color=None)

popcircle = Circle(x="poplon", 
                y="poplat", 
                radius=12000,
                fill_color={'field': 'colorpop', 'transform': color_mapper2}, 
                fill_alpha=0.8,
                line_color=None)

plot.add_glyph(protectedsource, protectedannulus, name="foo")

plot.add_glyph(unprotectedsource, unprotectedannulus, name="foo")

plot.add_glyph(popsource, popcircle)

protectedreef = LegendItem(label='Protected Reef', renderers=[plot.renderers[0]])
unprotectedreef = LegendItem(label='Unprotected Reef', renderers=[plot.renderers[1]])
legend1 = Legend(items=[protectedreef, unprotectedreef], location='top_right')
plot.add_layout(legend1)

curdoc().add_root(plot)
