from datetime import datetime
from flask import Flask, request
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.yaml'  # Our API url

app = Flask(__name__)
api = Api(app)
CORS(app)
# Call factory function to create the swagger blueprint
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL,
                                              API_URL,
                                              config={'app_name': "My API"})

# Register blueprint at URL
app.register_blueprint(swaggerui_blueprint) #, url_prefix=SWAGGER_URL)

# Use reqparse to parse incoming requests
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the user', required=True)
parser.add_argument('birthdate', type=str, help='Birthdate of the user (YYYY-MM-DD)', required=True)

# Initialize empty list to store user data
users = []

@app.route('/age', methods=['POST'])
# Calculate age based on input data and send user data to frontend
def post_age():
    args = parser.parse_args()
    name = args['name']
    birthdate = datetime.strptime(args['birthdate'], '%Y-%m-%d').date()
    age = (datetime.now().date() - birthdate).days // 365

    user = {'name': name, 'birthdate': birthdate, 'age': age}
    users.append(user)

    return jsonify(user), 201


@app.route('/age', methods=['GET'])
# Retrieve user data from the list and send it to frontend
def get_age_list():
    age_list = []
    for user in users:
        age_list.append({'name': user['name'], 'age': user['age']})
    return jsonify(age_list)

# start the flask server and wait for requests
if __name__ == '__main__':
    app.run(debug=True)

# The 'abort' method can be used to return an HTTP error response
# For example:
# abort(404, message="User not found")

# The 'Resource' class can be used to define API endpoints as classes
# For example:
# class User(Resource):
#     def get(self, user_id):
#         user = get_user(user_id)
#         if not user:
#             abort(404, message="User not found")
#         return jsonify(user)
#
# api.add_resource(User, '/users/<int:user_id>')
