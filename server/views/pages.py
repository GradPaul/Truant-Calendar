from flask import Blueprint, request, render_template
from flask import current_app as app
import requests
from server.utils import *

pages = Blueprint(__name__, __name__)

@pages.route("/")
def index():
    return render_template("index.html")

@pages.route("/result")
def result():
    return render_template("result.html")

