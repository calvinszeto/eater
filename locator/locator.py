import json
import math

class Locator:

    _locations = []

    def __init__(self, locations_file):
        with open(locations_file, "r") as f:
            _locations = json.JSONDecoder().decode(f)

    def _geocode(address):
        url = ("https://maps.googleapis.com/maps/api/geocode/json?"
               "address={}&sensor=false&key=AIzaSyDoxUfm0UVU8vMbto7lXPKDDTD2BbAYFAI").format(urllib.quote(address))
        return json.loads(urlopen(url).read())

    def _deg2rad(deg):
        return deg * (math.pi/180)

    def _distance(loc1, loc2):
        R = 6371; # Radius of the earth in km
        lat1 = loc1. 
        dLat = deg2rad(lat2-lat1);  
        dLon = deg2rad(lon2-lon1); 
        var a = 
        Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
Math.sin(dLon/2) * Math.sin(dLon/2)
    ; 
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
    var d = R * c; // Distance in km
    return d;


    def nearest(self, address):
        curr_location = _geocode(address)
        nearest_locations = [(location, _distance(curr_location, location)) for location in _locations] 
        nearest_locations.sort(key=lambda t: t[-1])
        return nearest_locations


if __name__ == "main":
