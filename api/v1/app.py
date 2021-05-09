#!/usr/bin/python3
"""flask application"""


import app.views from api.v1.views
from flask import Flask, make_response, jsonifyimport
from flask_cors import CORS
from models import storage
from os import getenv

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST', '0.0.0.0'),
        port=getenv('HBNB_API_PORT', 5000),
        threaded=True
    )
