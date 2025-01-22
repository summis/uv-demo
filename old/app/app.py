from flask import Flask, redirect, render_template
from werkzeug import Response

import algorithm

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return render_template("index.html")


@app.route("/optimize", methods=["POST"])
def button_click() -> Response:
    algorithm.optimize()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
