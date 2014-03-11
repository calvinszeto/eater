import json

class Locator:

    _locations = []

    def __init__(self, locations_file):
        with open(locations_file, "r") as f:
            _locations = json.JSONDecoder().decode(f)
