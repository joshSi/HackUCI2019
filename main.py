from flask import Flask, render_template, request, redirect
from flask_googlemaps import GoogleMaps, Map, icons
from copy import copy
import googlemaps, numpy

def getCenter(coordSet):
    coord_count = len(coordSet)
    if coord_count <= 0:
        return False

    X = 0.0
    Y = 0.0
    Z = 0.0

    for i, j in coordSet:
        lat = i * numpy.pi / 180
        lng = j * numpy.pi / 180

        a = numpy.cos(lat) * numpy.cos(lng)
        b = numpy.cos(lat) * numpy.sin(lng)
        c = numpy.sin(lat)

        X += a
        Y += b
        Z += c


    X /= coord_count
    Y /= coord_count
    Z /= coord_count

    lng = numpy.arctan2(Y, X)
    hyp = numpy.sqrt(X * X + Y * Y)
    lat = numpy.arctan2(Z, hyp)

    newlat = (lat * 180 / numpy.pi)
    newlng = (lng * 180 / numpy.pi)
    return newlat, newlng

app = Flask(__name__)
mykey = "AIzaSyASiSZuUB8z7D3Kd9ZoIIz3Ba4YWabpK1Q"
GoogleMaps(app, key=mykey)

friend_locations = []
meetingPoint = None

@app.route("/showLoc", methods = ['POST', 'GET'])
def getLoc():
    if request.method == 'POST':
        lat, lng = request.form['myLoc'].split(',')
        me = {
            'icon' : 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
            'lat' : float(lat),
            'lng' : float(lng),
            'infobox' : request.form['username']
                +' ('+"{0:.2f}".format(float(lat))+', '+"{0:.2f}".format(float(lng))+')'}
    return redirect('/map')

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
            'lng' : float(request.form['lng']),
            'infobox' : request.form['username']
                +' ('+"{0:.2f}".format(float(request.form['lat']))+', '+"{0:.2f}".format(float(request.form['lng']))+')'}]
        # print("latitude", request.form['lat'])
        # print("longitude", request.form['lng'])
        # print("username", request.form['username'])
        return redirect("/home")

@app.route("/map")
def test_view():
    global friend_locations, meetingPoint
    gmaps = googlemaps.Client(key=mykey)
    myloc = gmaps.geolocate()

    
    meMarker = {'icon' : 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png', 
            'lat' : myloc['location']['lat'],
            'lng' : myloc['location']['lng'],
            'infobox' : 'You'}
    
    friend_locations += [meMarker]
    print("length: ", len(friend_locations))

    coordSet = set()
    # Calculating the center point of the markers
    print("List:")
    for point in friend_locations:
        coordSet.add((point['lat'], point['lng']))
        print('\t', point['lat'], point['lng'])

    new_lat, new_lng = getCenter(coordSet)
    center = {'icon' : 'http://maps.google.com/mapfiles/ms/icons/green-dot.png', 
            'lat' : (new_lat),
            'lng' : (new_lng),
            'infobox': "<b style='color:green;'>Meeting Point</b>"
                +' ('+"{0:.2f}".format(new_lat)+', '+"{0:.2f}".format(new_lng)+')'}
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
    
    meetingPoint = ''
    print(big_list)
    #print(center)
    reverse_geocode_result = gmaps.reverse_geocode((center['lat'], center['lng']))
    #print(reverse_geocode_result)
    for dict in reverse_geocode_result:
        #print(dict)
        for key, value in dict.items():
            if key == 'formatted_address':
                meetingPoint = dict['formatted_address']
                break
        else:
            continue
        break
    if meetingPoint == '':
        meetingPoint = 'Unnamed Location'

    return render_template('map.html', group_map=group_map, meetingPoint=meetingPoint)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 8080)