#!/usr/bin/python3
"""This module creates a minimalist flask app"""
from flask import Flask, escape, render_template

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def p_route(text="is cool"):
    """This returns Python variable"""
    return "Python %s" % escape(text).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def n_route(n):
    """This returns a number fif it's a bumber"""
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_route(n):
    """This returns a number fif it's a bumber"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_odd_even(n):
    """This returns a html page rendered with jinja"""
    status = "odd"
    if n % 2 == 0:
        status = "even"
    return render_template('6-number_odd_or_even.html', n=n, status=status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
