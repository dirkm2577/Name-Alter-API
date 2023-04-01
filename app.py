from datetime import date
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = []

class User(Resource):
    def post(self):
        data = request.get_json()
        users.append(data)
        return {'message': 'User created', 'data': data}, 201

    def get(self, name):
        for user in users:
            if user['name'] == name:
                birthdate = date.fromisoformat(user['birthdate'])
                today = date.today()
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                return {'name': name, 'age': age}
        return {'message': 'User not found'}, 404

api.add_resource(User, '/user', '/user/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
