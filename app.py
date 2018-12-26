from flask import Flask
from datetime import datetime
import re
from flask import render_template
from flask import jsonify, make_response,json

from player_class import *

app = Flask(__name__)

@app.route("/")
def home():
    return "Mom is a noob"

@app.route("/hello/<name>")

def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    # BAD CODE! Avoid inline HTML for security reason, plus templates automatically escape HTML content.
    content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now

    return render_template(
        "hello_there.html",
        title="Hello, Flask",
        content=content
    )

@app.route("/jason")
def jason():
    p = player("jake",2,3,"four")
    jsonSTR = json.dumps(p.__dict__)
    return jsonSTR