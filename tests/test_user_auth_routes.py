from tests.conftest import get_jwt_for_testing, create_student
from ayat.models import users


def test_base_url(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Welcome to Ayat' in res.data


def test_create_student(client):
    payload = """{
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
        "action": "register_student",
        "profile_pic": "default",
        "country": "Algeria",
        "registeration_date": "2010-01-01"
    }"""
    res = client.post('/v1/users', data=payload)
    assert res.status_code == 200
    assert res.email == users.User.query.filter_by(email='testuser@email.com').first()


def test_create_staff(client):
    payload = """{
        "email": "testuser@email.com",
        "password": "testpass123",
        "full_name": "testuser",
        "phone": "1321431",
        "birth_date": "3222-02-03",
        "gender": true,
        "type": "staff",
        "action": "register_staff",
        "profile_pic": "default",
        "country": "Algeria",
        "registeration_date": "2010-01-01"
    }"""

    res = client.post('/v1/users', data=payload)
    assert res.status_code == 200
    assert res.email == users.User.query.filter_by(email='testuser@email.com').first()


def test_get_invalid_user(client):
    jwt = get_jwt_for_testing('user')
    res = client.get('/v1/users/123', data=jwt)
    assert res.status_code == 404


def test_get_all_users(client):
    jwt = get_jwt_for_testing('staff')
    res = client.get('/v1/users', data=jwt)
    assert res.status_code == 200


def test_login(client):
    create_student()
    payload = """{
        "action": "login",
        "email": "testuser@email.com",
        "password": "testpass123"
    }"""
    res = client.post('/v1/users', data=payload)
    assert res.status_code == 200
    assert res.email == b'testuser@email.com'


# TODO: token, msg
def test_promote_user(client):
    jwt = get_jwt_for_testing('staff')
    pass


# TODO: token, msg
def test_delete_user(client):
    pass
