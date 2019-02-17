from flask import Flask, render_template, request, redirect
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from functools import reduce
from copy import copy
import googlemaps

app = Flask(__name__)
mykey = "AIzaSyASiSZuUB8z7D3Kd9ZoIIz3Ba4YWabpK1Q"
GoogleMaps(app, key=mykey)

friend_locations = []
meetingPoint = None

@app.route("/")
def redir():
    return redirect("/home")

@app.route("/demo")
def inputLocation():
    return render_template('demo.html')


@app.route("/home")
def something():
    return render_template('index.html')


@app.route("/input", methods = ['POST', 'GET'])
def enter_data():
    global friend_locations
    if request.method == 'POST':
        #Add to database later
        friend_locations += [{
            'icon' : 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
            'lat' : float(request.form['lat']),
            'lng' : float(request.form['lng'])}]
        #print("latitude", request.form['lat'])
        #print("longitude", request.form['lng'])
        return redirect("/home")

@app.route("/map")
def test_view():
    global friend_locations, meetingPoint
    gmaps = googlemaps.Client(key=mykey)
    myloc = gmaps.geolocate()

    
    meMarker = {'icon' : 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png', 
            'lat' : myloc['location']['lat'],
            'lng' : myloc['location']['lng']}
    
    friend_locations += [meMarker]

    latList, lngList = [], []
    # Calculating the center point of the markers
    for point in friend_locations:
        latList.append(point['lat'])
        lngList.append(point['lng'])
    
    latList.append(meMarker['lat'])
    lngList.append(meMarker['lng'])
    center = {'icon' : 'http://maps.google.com/mapfiles/ms/icons/green-dot.png', 
            'lat' : (reduce((lambda x, y: x + y), latList[1:]) / len(latList[1:])),
            'lng' : (reduce((lambda x, y: x + y), lngList[1:]) / len(lngList[1:])),
            'infobox': "<b style='color:green;'>Meeting Point</b>"}
    big_list = copy(friend_locations)
    big_list.append(center)
    group_map = Map(
        center_on_user_location="true",
        identifier="group_map",
        varname="group_map",
        lat=meMarker['lat'],
        lng=meMarker['lng'],
        style="height: 425px; width: 1000px;",
        markers=big_list,
        zoom=12,
        cluster=False
    )
    
    reverse_geocode_result = gmaps.reverse_geocode((center['lat'], center['lng']))
    for dict in reverse_geocode_result:
        for key, value in dict.items():
            if key == 'formatted_address':
                print()
                meetingPoint = dict['formatted_address']
                break
        else:
            continue
        break
    return render_template('map.html', group_map=group_map, meetingPoint=meetingPoint)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 8080)