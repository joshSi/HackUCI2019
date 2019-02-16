from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from functools import reduce
import googlemaps

app = Flask(__name__)
mykey = "AIzaSyASiSZuUB8z7D3Kd9ZoIIz3Ba4YWabpK1Q"
GoogleMaps(app, key=mykey)

@app.route("/")
def test_view():
    client = googlemaps.Client(key = mykey)
    myloc = googlemaps.client.geolocate(client, consider_ip = True)
    meMarker = {'icon' : 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png', 
            'lat' : myloc['location']['lat'],
            'lng' : myloc['location']['lng']}

    group_map = Map(
        center_on_user_location="true",
        identifier="group_map",
        varname="group_map",
        lat=meMarker['lat'],
        lng=meMarker['lng'],
        style="height: 425px; width: 1000px;",
        markers=[
            {
                'icon' : 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': 37.4500,
                'lng': -122.1350
            },
            {
                'icon' : 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': 37.4400,
                'lng': -120.1350
            },
            {
                'icon' : 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': 37.4300,
                'lng': -121.1350
            },
            {
                'icon' : 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': 36.4200,
                'lng': -120.1350
            },
        ],
        zoom=12,
        cluster=False
    )

    # Calculating the center point of the markers
    latList = []
    lngList = []
    latList = list(latList)
    lngList = list(lngList)
    for dict in group_map.markers:
        for key, value in dict.items():
            if key == 'lat':
                latList.append(dict['lat'])
            elif key == 'lng':
                lngList.append(dict['lng'])
    
    latList.append(meMarker['lat'])
    lngList.append(meMarker['lng'])
    center = {'icon' : 'http://maps.google.com/mapfiles/ms/icons/green-dot.png', 
            'lat' : (reduce((lambda x, y: x + y), latList[1:]) / len(latList[1:])),
            'lng' : (reduce((lambda x, y: x + y), lngList[1:]) / len(lngList[1:]))}
    group_map.markers.append(center)

    group_map.markers.append(meMarker)

    gmaps = googlemaps.Client(key="AIzaSyASiSZuUB8z7D3Kd9ZoIIz3Ba4YWabpK1Q")
    reverse_geocode_result = gmaps.reverse_geocode((center['lat'], center['lng']))
    #print(reverse_geocode_result)
    for dict in reverse_geocode_result:
        for key, value in dict.items():
            if key == 'formatted_address':
                #print(dict['formatted_address'])
                meetingPoint = dict['formatted_address']
                break
        else:
            continue
        break


    return render_template('index.html', group_map=group_map, meetingPoint=meetingPoint)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 8080)