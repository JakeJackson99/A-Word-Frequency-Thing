from unittest import result
from flask import Flask, render_template
from word_finder import filter_data, get_data

app = Flask(__name__)

@app.route("/")
def index():
    results = filter_data(get_data(), 10, 8)
    return render_template("index.html", results=results)