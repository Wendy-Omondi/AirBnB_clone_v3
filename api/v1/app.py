#!/usr/bin/python3
"""flask application"""


import app.views from api.v1.views
from flask import Flask, make_response, jsonifyimport
from flask_cors import CORS
from models import storage
from os import getenv

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(app_views)

@app.errorhandler(404)
def page_not_found(error):
    """returns a JSON-formatted 404 status code response."""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST', '0.0.0.0'),
        port=getenv('HBNB_API_PORT', 5000),
        threaded=True
    )
