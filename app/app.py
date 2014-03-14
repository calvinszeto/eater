from flask import Flask, render_template, request, jsonify
from locator import Locator
app = Flask(__name__)

@app.route('/_locate_nearest')
def locate_nearest():
    address = request.args.get('address', 'Austin, TX', type=str)
    page = request.args.get('page', 0, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    locator = Locator("/home/puppyplus/Projects/eater/data/geocoded_restaurants.json") 
    curr_location, nearest_locations = locator.nearest(address, page, per_page)
    return jsonify({"loc": curr_location, "results":[location[0] for location in nearest_locations]})

@app.route('/')
def index():
    return render_template('app.html') 

if __name__ == '__main__':
    app.run(debug=True)
