from flask import Flask, redirect, url_for,send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.UsersSignin import UsersSignin
from api.UserSignup import UsersSignup

# app = Flask(__name__)

app = Flask(__name__, static_url_path='', static_folder='clientapp/build')
CORS(app) #comment this on deployment

api = Api(app)

# CALL REACTJS clientapp/build folder
@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')


# CALL API UsersSignin
api.add_resource(UsersSignin, '/users/signin')

# CALL API UsersSignup
api.add_resource(UsersSignup, '/users/signup')
