import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# test data
tpe = {
    "id": 0,
    "city_name": "Taipei",
    "country_name": "Taiwan",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "New York",
    "country_name": "United States",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "London",
    "country_name": "United Kingdom",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}

cities = [tpe, nyc, ldn]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)

app.run()
