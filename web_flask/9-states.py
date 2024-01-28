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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    data = storage.all(State).values()
    data_sorted = sorted(data, key=lambda x: x.name)
    return render_template("9-states.html", states=data_sorted, ids=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
