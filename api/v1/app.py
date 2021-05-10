#!/usr/bin/python3
"""flask application"""


from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from models import storage
from os import getenv

app = Flask(__name__)
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
