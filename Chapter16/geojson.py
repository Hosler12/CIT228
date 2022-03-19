import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

with open('Chapter16/1.0_month.json') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

data = [{'type':'scattergeo', 'lon':lons, 'lat':lats, 'marker':{'size': [5*mag for mag in mags]},'text':mags}]
layout = Layout(title='All Earthquakes Above Mag 1.0 Last Month')
fig = {'data':data, 'layout':layout}
offline.plot(fig)