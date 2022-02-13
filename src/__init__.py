

from flask import Flask, jsonify
from flask_restx import Resource, Api


#instantiate the app
app = Flask(__name__)

api = Api(app)
#API = application programming interface

#Sets config
app.config.from_object('src.config.DevelopmentConfig')



class Ping(Resource):
    def get(self):
        return {
            'status':'success',
            'message':'pong!?'
        }

api.add_resource(Ping,'/ping')
