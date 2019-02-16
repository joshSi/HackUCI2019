from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

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
            }
        ],
        zoom=12,
        cluster=True
    )
    return render_template('home.html', clustermap=clustermap)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)