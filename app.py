import os
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hey! I am Mathew. This is my first Docker app!"
@app.route("/age")
def age():
    return "I'd rather not say!"
@app.route("/hobby")
def hobby():
    return "I love learning DevOps and breaking things in Kubernetes."
@app.route("/stack")
def stack():
    return "Python, Docker, Kubernetes, Linux"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
