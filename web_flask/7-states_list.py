#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    data = storage.all(State).values()
    data_sorted = sorted(data, key=lambda x: x.name)
    return render_template("7-states_list.html", states=data_sorted)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
