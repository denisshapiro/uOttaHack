from app import app, api, Resource
from app.models import User, Car
from flask import jsonify, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

class Users(Resource):
    def get(self):
        x = [user.jsonify() for user in User.query.all()]
        print(x)
        return x

api.add_resource(Users, '/users')