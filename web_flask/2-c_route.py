#!/usr/bin/python3
"""This module creates a minimalist flask app"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def call_hbnb():
    """This returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """This returns C variable"""
    return "C %s" % escape(text).replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
