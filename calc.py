import numpy

def getCenter(coordList):
    coord_count = len(coordList)
    if coord_count <= 0:
        return False

    X = 0.0
    Y = 0.0
    Z = 0.0

    for i, j in coordList:
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