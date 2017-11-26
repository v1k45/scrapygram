from flask import Flask


app = Flask(__name__)

@app.route("/echo")
def echo():
    return "Are bhai bhai bhai..."
