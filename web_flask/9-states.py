#!/usr/bin/python3
"""This module creates a minimalist flask app"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def all_states():
    """Returns all states"""
    states = []
    for state in storage.all(State).values():
        states.append(state)
    states.sort(key=lambda x: x.name)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def curr_state(id):
    key = "State.{}".format(id)
    if key in storage.all(State).keys():
        curr = storage.all(State)[key]
        return render_template('9-states.html', curr=curr)
    else:
        return render_template('9-states.html')


@app.teardown_appcontext
def end_session(exception=None):
    """Ends the app"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
