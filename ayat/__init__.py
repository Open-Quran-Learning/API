from flask import Flask

app = Flask(__name__)


from ayat import telegram
from ayat import authentication
app.config['SECRET_KEY'] = 'thisisthesecretkey'
