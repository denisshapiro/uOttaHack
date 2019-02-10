from app import app, api, Resource, db
from app.models import User, Car
from flask import jsonify, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from .config import LOCATIONIQ_API_KEY
import json
import sqlalchemy

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
    return f'{lat}, {lon}'

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
    resp.message(getLatLng(body))
    return str(resp)

class Users(Resource):
    def get(self):
        return jsonify([user.jsonify() for user in User.query.all()])

api.add_resource(Users, '/users')
