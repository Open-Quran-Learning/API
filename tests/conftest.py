import pytest
from ayat import app, db
from ayat.models.users import *
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

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


# =========== Functions ========== #
def create_student(email, phone):
    # Hint:
    # if the student have guardian just uncomment it.
    # new_guardian = Guardian(
    #     email="DDSADAS@mail.com",
    #     phone_number="16548484"
    # )
    student = Student(
        name="khaled mohamed",
        public_id=str(uuid.uuid4()),
        email=email,
        country_name="egypt",
        phone_number=phone,
        profile_picture="default",
        birth_date="2020-01-01",
        gender=True,
        password= generate_password_hash("passworddd", method="sha256"),
        registeration_date="2010-01-01",
        type="student"
    )
    # db.session.add(new_guardian)
    # student.guardians.append(new_guardian)
    db.session.add(student)
    db.session.commit()
    return {
        "public_id": student.public_id,
        "email": student.email,
        "type": "student"
    }


def create_staff(email, phone):
    new_permission = Permission(
        permission_name="manager"
    )
    staff = Staff(
        name="mohamed mo2men",
        public_id=str(uuid.uuid4()),
        email=email,
        country_name="Egypt",
        phone_number=phone,
        profile_picture="default.png",
        birth_date="2010-03-03",
        gender=False,
        password=generate_password_hash("paworddd", method="sha256"),
        registeration_date="2010-05-05",
        type="staff",
    )
    db.session.add(new_permission)
    staff.permissions.append(new_permission)
    db.session.add(staff)
    db.session.commit()
    return {
        "public_id": staff.public_id,
        "email": staff.email,
        "type": "staff"
    }


def generate_jwt(public_id, email, type):
    token = jwt.encode({'public_id': str(public_id),
                        'email': email,
                        'type': type}, app.config['SECRET_KEY'])

    return token
