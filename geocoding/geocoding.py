import urllib
from urllib2 import urlopen
import json

def geocode(address):
    url = ("https://maps.googleapis.com/maps/api/geocode/json?"
           "address={}&sensor=false&key=AIzaSyDoxUfm0UVU8vMbto7lXPKDDTD2BbAYFAI").format(urllib.quote(address))
    return json.loads(urlopen(url).read())

with open("../data/restaurants.json", "r") as f:
    restaurants = json.load(f)
    print "Geocoding scraped data..."
    geocoded_data = json.JSONEncoder().encode([geocode(restaurant["address"])["results"][0] for restaurant in restaurants])
    with open("../data/geocoded_restaurants.json", "w") as g:
        json.dump(geocoded_data, g)
