from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS



from flask_mail import Mail

import os

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
                                        
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
db = SQLAlchemy(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('AYAT_EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('AYAT_EMAIL_PASS')
app.config['MAIL_ASCII_ATTACHMENTS'] = True
mail = Mail(app)

from ayat.models import models
<<<<<<< HEAD




=======
from ayat import helpers
from ayat import authentication_routes
from ayat.authorization import authorization_decorators
>>>>>>> userRoutes
