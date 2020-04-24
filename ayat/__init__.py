from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:ASDasd225588@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
db = SQLAlchemy(app)

from ayat.models import models
from ayat import authentication_routes
