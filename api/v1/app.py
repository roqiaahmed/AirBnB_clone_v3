#!/usr/bin/python3

""" Module for app """
from flask import Flask, make_response, jsonify
from models import storage
from os import environ
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(error):
    """Closes the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Returns a JSON-formatted 404 status code response"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
