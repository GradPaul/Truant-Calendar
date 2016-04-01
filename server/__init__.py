from flask import Flask, render_template, request, jsonify, session, redirect
import datetime
import re
import server.views
import server.filters
from server.utils import *

app = Flask(__name__)
app.config.from_object("config.Config")
app.debug = app.config["DEBUG"]

#blueprints config
BLUEPRINTS = [
    views.pages
]

for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)

app.jinja_env.filters["content_chopper"] = filters.content_chopper
app.jinja_env.filters["completeProtocal"] = filters.completeProtocal
