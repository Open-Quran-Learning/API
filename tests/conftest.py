import pytest
from ayat import app, db
from ayat.models import *


@pytest.fixture
def create_app():
    app_test = app
    app_test.config['TESTING'] = True

    with app_test.app_context():
        db.create_all()
    # db.create_all()
    yield app_test

    db.drop_all()


@pytest.fixture
def client(create_app):
    return create_app.test_client()


# TODO: commit created user to db
@pytest.fixture
def create_student():
    user = """{
        "guardian_email": "adva@sadv.adfva",
        "guardian_name": "adsva",
        "guardian_phone": "113413",
        "email": "testuser@email.com",
        "password": "testpass123",
        "full_name": "testuser",
        "phone": "1321431",
        "birth_date": "3222-02-03",
        "gender": true,
        "type": "student",
        "action": "register_staff",
        "profile_pic": "default",
        "country": "Algeria",
        "registeration_date": "2010-01-01"
    }"""


# TODO: commit user to db
@pytest.fixture
def create_staff():
    staff = """{
        "email": "teststaff@email.com",
        "password": "testpass123",
        "full_name": "teststaff",
        "phone": "1321431",
        "birth_date": "3222-02-03",
        "gender": true,
        "type": "staff",
        "action": "register_staff",
        "profile_pic": "default",
        "country": "Algeria",
        "registeration_date": "2010-01-01"
    }"""


@pytest.fixture
def get_jwt_for_testing(type, client):
    if type == 'staff':
        create_staff()
        payload = """{
            "action": "login",
            "email": "teststaff@email.com",
            "password": "testpass123"
        }"""
        res = client.post('/v1/users', data=payload)
    else :
        create_student()
        payload = """{
            "action": "login",
            "email": "testuser@email.com",
            "password: "testpass123"
        }"""
        res = client.post('/v1/users', data=payload)
    
    return res.token
