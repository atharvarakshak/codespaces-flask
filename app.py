from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/name")
def display():
    return render_template("index1.html")

@app.route("/age")
def age():
    return "42"

