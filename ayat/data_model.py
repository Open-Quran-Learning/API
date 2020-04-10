from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gkgulqpyyzvkoj:79f564db7ebd2d9380987e48469d987d5f74ab789893ea336daa255ef71ca43a@ec2-54-147-209-121.compute-1.amazonaws.com:5432/d2d9d2jm3utbv'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class UserType(db.Model):
    __tablename__ = 'usertype'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    type = db.Column(db.VARCHAR(20), unique=True)
    users = db.relationship('User', backref='user_id', lazy=True)

    def __init__(self, _type):
        self.type = _type


user_address = db.Table('user_address',
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                        db.Column('address', db.Integer, db.ForeignKey('address.id'), primary_key=True))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.VARCHAR(30), unique=True)
    first_name = db.Column(db.VARCHAR(30), unique=False)
    last_name = db.Column(db.VARCHAR(30), unique=False)
    guardian_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    guardian = db.relationship('User', uselist=False, remote_side=[id])
    email = db.Column(db.VARCHAR(120), unique=True)
    token = db.Column(db.VARCHAR(), unique=True)
    chat_id = db.Column(db.Integer, nullable=False)
    profile_picture = db.Column(db.VARCHAR(20), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    gender = db.Column(db.Boolean)
    password = db.Column(db.VARCHAR(40))
    user_type_id = db.Column(db.Integer, db.ForeignKey('usertype.id'))
    phone_number = db.relationship('Cellphone', backref='user', lazy=True)
    user_address = db.relationship('Address', secondary=user_address, lazy='dynamic',
                                   backref=db.backref('user', lazy=True))

    def __init__(self, user_name, first_name, last_name, email, token, chat_id, profile_picture,
                 birth_date, gender, password):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.token = token
        self.chat_id = chat_id
        self.profile_picture = profile_picture
        self.birth_date = birth_date
        self.gender = gender
        self.password = password

    def __repr__(self):
        return '<User %r>, <Gender %r>' % (self.user_name, self.email)


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.VARCHAR(30), unique=False, nullable=True)

    def __init__(self, country):
        self.country_name = country

    def __repr__(self):
        return '<Address %r>' % self.country_name


class Cellphone(db.Model):
    __tablename__ = 'cellphone'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.VARCHAR(20), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def __repr__(self):
        return '<Cellphone %r>' % self.phone_number


if __name__ == '__main__':
    app.run(debug=True)
