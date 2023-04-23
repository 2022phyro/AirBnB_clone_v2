#!/usr/bin/python3
"""This module creates a minimalist flask app"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def all_states():
    """Returns all states"""
    states = []
    for state in storage.all(State).values():
        states.append(state)
    states.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def end_session(exception=None):
    """Ends the app"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
