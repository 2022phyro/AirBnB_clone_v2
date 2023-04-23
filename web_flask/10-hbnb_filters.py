#!/usr/bin/python3
"""This module creates a minimalist flask app"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def all_states():
    """Returns all states"""
    states = []
    for state in storage.all(State).values():
        states.append(state)
    states.sort(key=lambda x: x.name)
    amen = [x for x in storage.all(Amenity).values()]
    amen.sort(key=lambda x: x.name)
    return render_template("10-hbnb_filters.html", states=states, amen=amen)


@app.teardown_appcontext
def end_session(exception=None):
    """Ends the app"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
