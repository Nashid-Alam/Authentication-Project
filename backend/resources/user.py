from flask_restful import Resource
from flask import request
from models.user_model import User, db

class Users(Resource):
    def get(self):
        data = User.find_all()
        results = [u.json() for u in data]
        return results

    def post(self):
        data = request.get_json()
        user = User(**data)
        user.create()
        return user.json(), 201


class SingleUser(Resource):
    def get(self, id):
        pass

    def delete(self, id):
        pass

    def put(self, id):
        pass