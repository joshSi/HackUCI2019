from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from functools import *

app = Flask(__name__)

GoogleMaps(app, key="AIzaSyASiSZuUB8z7D3Kd9ZoIIz3Ba4YWabpK1Q")
@app.route("/")
def test_view():
    clustermap = Map(
        identifier="clustermap",
        varname="clustermap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'lat': 37.4500,
                'lng': -122.1350
            },
            {
                'lat': 37.4400,
                'lng': -122.1350
            },
            {
                'lat': 37.4300,
                'lng': -122.1350
            },
            {
                'lat': 36.4200,
                'lng': -122.1350
            },
            {
                'lat': 36.4100,
                'lng': -121.1350
            },
        ],
        zoom=12,
        cluster=True
    )

    # Calculating the center point of the markers
    latList = [],
    lngList = [],
    latList = list(latList)
    lngList = list(lngList)
    for dict in clustermap.markers:
        for key, value in dict.items():
            if key == 'lat':
                latList.append(dict['lat'])
            else:
                lngList.append(dict['lng'])
    center = {'icon' : 'http://maps.google.com/mapfiles/ms/icons/green-dot.png', 
            'lat' : (reduce((lambda x, y: x + y), latList[1:]) / len(latList[1:])),
            'lng' : (reduce((lambda x, y: x + y), lngList[1:]) / len(lngList[1:]))}
    clustermap.markers.append(center.copy())

    return render_template('home.html', clustermap=clustermap)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)