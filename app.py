from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, this is a new version of python3-flask-heroku-app"