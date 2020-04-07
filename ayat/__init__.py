from flask import Flask
import os

app = Flask(__name__)
token = os.environ['TOKEN']
base_url = f'https://api.telegram.org/bot{token}/'

from ayat import telegram


