#!/usr/bin/python3

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", methods=["GET"])
def serve_home():
    return render_template("home.html")

@app.route("/clock", methods=["GET"])
def serve_polar_clock():
    return render_template("polar_clock.html")

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=81, debug=True)

