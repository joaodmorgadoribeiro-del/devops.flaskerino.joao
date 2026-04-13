import os
from flask import Flask

application = Flask(__name__)

DESIRED_PATH = os.getenv("DESIRED_PATH", "/")
NUMBER = os.getenv("NUMBER", "0")

@application.route(DESIRED_PATH)
def greeting():
    return f"<h1>Hello from cool server {DESIRED_PATH} number {NUMBER}!</h1>"

@application.route("/healthcheck")
def healthcheck():
    return "It works!", 200

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)
