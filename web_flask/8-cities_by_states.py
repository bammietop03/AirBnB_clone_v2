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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    data = storage.all(State).values()
    data_sorted = sorted(data, key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=data_sorted)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
