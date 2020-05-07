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


def test_get_invalid_user(client):
    res = client.get('/v1/users/123')
    assert res.status_code == 403
