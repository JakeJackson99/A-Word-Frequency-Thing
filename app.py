from unittest import result
from flask import Flask, render_template
from word_finder import *

app = Flask(__name__)

@app.route("/")
def index():
    results = filter_data(get_data(), 10, 8)
    print(results)
    return render_template("index.html", results=results)