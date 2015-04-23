# This will be great!

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from cpstats import models
