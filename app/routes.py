from app import app, api, Resource, db
from app.models import User, Car
from flask import jsonify, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from .config import LOCATIONIQ_API_KEY
import json
from app.distance import shortest_distance

def getLatLng(address):
    url = "https://us1.locationiq.com/v1/search.php"

    data = {
        'key': LOCATIONIQ_API_KEY,
        'q': address,
        'format': 'json'
    }

    response = json.loads(requests.get(url, params=data).text)[0]

    lat = response['lat']
    lon = response['lon']
    return {"lat": float(lat), "lon": float(lon)}

def getAddress(resp):
    address = json.loads(resp)['address']
    return address['house_number'] + ' ' + address['road'] + ' ' + address['city'] + ' ' + address['state'] + ' ' + address['country']

def changeDBp1(id):

    c = Car.query.get(id)
    c.status = "taken"
    c.user_id = "0016136179842"
    db.session.add(c)
    db.session.commit()
    return "car checked out"

def changeDBp2(id):

    c = Car.query.get(id)
    c.status = "free"
    c.user_id = None
    u = User.query.get("0016136179842")
    db.session.add(c)
    db.session.commit()
    return "car returned"  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/sms', methods=['GET', 'POST'])
def sms():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    coords = getLatLng(body)
    closest_car = shortest_distance(coords["lat"], coords["lon"], [(car.lat, car.lon) for car in Car.query.all()])
    url = 'https://us1.locationiq.com/v1/reverse.php?key={}&lat={}&lon={}&format=json'.format('d91ebed07712b2', closest_car[0], closest_car[1])
    resp.message(getAddress(requests.get(url).text))
    return str(resp)

class Cars(Resource):
    def get(self):
        return jsonify([car.jsonify() for car in Car.query.all()])

class Users(Resource):
    def get(self):
        return jsonify([user.jsonify() for user in User.query.all()])

api.add_resource(Users, '/users')
api.add_resource(Cars, '/cars')
