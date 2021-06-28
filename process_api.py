import flask_cors
from flask import Flask ,jsonify
from flask_restful import Api,Resource,request,reqparse
import os
from flask_cors import CORS
from flask_jwt_extended import *
import datetime
from Important_sent import TEXT_PROCCESS


class best_sent(Resource):


    @flask_cors.cross_origin()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("info", required=True)
        content = parser.parse_args()
        info = content["info"]
        text_processor = TEXT_PROCCESS();
        fav_sent = text_processor.GET_BEST_SENT(info)
        response = jsonify({"result": fav_sent})
      #  response.headers.add("Access-Control-Allow-Origin", "*")
        return response


app = Flask(__name__)
CORS(app)
api = Api(app)
api.add_resource(best_sent,"/text")
app.config['JWT_SECRET_KEY']='MY_SECREST_KEY'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] =datetime.timedelta(days=1)
jwt = JWTManager(app)
app.run(
host="0.0.0.0",
port=8888
)





