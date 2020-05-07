import pytest
from flask import g, session
from sqlalchemy import false, true


def test_base_url(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Welcome to Ayat' in res.data


def test_create_student(client):
    payload = """{
        "email": "sdacdca@dskca.casd",
        "password": "sca",
        "full_name": "dsca",
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


def test_create_staff(client):
    payload = """{
        "email": "sdacdca@dskca.casd",
        "password": "sca",
        "full_name": "dsca",
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

# TODO: add token, assert result(user)
def test_get_invalid_user(client):
    res = client.get('/v1/users/123', data="JWT")
    assert res.status_code == 403

# TODO: add token, assert how many users, assert msg
def test_get_all_users(client):
    res = client.get('/v1/users')
    assert res.status_code == 403

# TODO: msg
def test_login(client):
    pass

# TODO: token, msg
def test_promote_user(client):
    pass

# TODO: token, msg
def test_delete_user(client):
    pass
