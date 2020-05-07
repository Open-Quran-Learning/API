import pytest
from ayat import app, db
from ayat.models import *


@pytest.fixture
def create_app():
    app_test = app
    app_test.config['TESTING'] = True

    with app_test.app_context():
        db.create_all()

    yield app_test

    db.drop_all()


@pytest.fixture
def client(create_app):
    return create_app.test_client()


@pytest.fixture
def runner(create_app):
    return create_app.test_cli_runner()
