from app import app, api, Resource
from app.models import User, Car
from flask import jsonify

class Users(Resource):
    def get(self):
        x = [user.jsonify() for user in User.query.all()]
        print(x)
        return x

api.add_resource(Users, '/users')