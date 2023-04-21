#!/usr/bin/python3
"""This module creates a minimalist flask app"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def all_states():
    states = []
    for state in storage.all(State).values():
        # print(state)
        states.append(state.to_dict())
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
