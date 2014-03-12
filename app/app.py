from flask import Flask, render_template, request, jsonify
from locator import Locator
app = Flask(__name__)

@app.route('/_locate_nearest')
def locate_nearest():
    address = request.args.get('address', 'Austin, TX', type=str)
    locator = Locator("/home/puppyplus/Projects/eater/data/geocoded_restaurants.json") 
    return jsonify({"results":[location[0]["name"] for location in locator.nearest(address)]})

@app.route('/')
def index():
    return render_template('app.html') 

if __name__ == '__main__':
    app.run(debug=True)
