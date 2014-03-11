import urllib
from urllib2 import urlopen
import json

def geocode(address):
    url = ("https://maps.googleapis.com/maps/api/geocode/json?"
           "address={}&sensor=false&key=AIzaSyDoxUfm0UVU8vMbto7lXPKDDTD2BbAYFAI").format(urllib.quote(address))
    return json.loads(urlopen(url).read())

with open("../data/restaurants.json", "r") as f:
    restaurants = json.load(f)
    for restaurant in restaurants:
        print geocode(restaurant["address"])
