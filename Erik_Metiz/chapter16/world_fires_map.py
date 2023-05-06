import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Изучение структуры данных.
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        if column_header == 'latitude':
            lat_i = index
        if column_header == 'longitude':
            lon_i = index
        if column_header == 'brightness':
            br_i = index

    lats, lons, brightnesses = [], [], []
    for row in reader:
        lats.append(float(row[lat_i]))
        lons.append(float(row[lon_i]))
        brightnesses.append(float(row[br_i]))

# Нанесение данных на карту.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    #'text': hover_texts,
    'marker': {
        'size': [brightness/50 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': False,
        'colorbar': {'title': 'brightness'},
    },
}]

headline = "World fires"
my_layout = Layout(title=headline)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
