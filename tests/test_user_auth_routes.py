from tests.conftest import generate_jwt, create_student, create_staff
from ayat.models.users import User


def test_base_url(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Welcome to Ayat' in res.data


def test_create_student(client):
    payload = """{
        "action":   "register_student",
        "full_name":  "exampddldde",
        "email":  "explsaddfddsd@dsadas.com",
        "country":  "example",
        "phone":   "32132132dd1213",
        "profile_pic": "2d222",
        "birth_date":   "2015-05-16",
        "gender": false,
        "password":   "464468",
        "gender": false,
        "guardian_email": "dsadadsdsa@dsadsa.com",
        "guardian_phone": "468d686848",
        "registeration_date":   "2015-05-16"
    }"""
    res = client.post('/v1/users', data=payload)
    json_data = res.get_json()
    assert res.status_code == 200
    assert json_data['status'] == "created"


def test_create_student_with_invalid_phone(client):
    data = create_student(email="ddsadas@dsa.com", phone="265156655")
    payload = """{
        "action":   "register_student",
        "full_name":  "exampddldde",
        "email":  "explsaddfddsd@dsadas.com",
        "country":  "example",
        "phone":   "265156655",
        "profile_pic": "2d222",
        "birth_date":   "2015-05-16",
        "gender": false,
        "password":   "464468",
        "gender": false,
        "guardian_email": "dsadadsdsa@dsadsa.com",
        "guardian_phone": "468d686848",
        "registeration_date":   "2015-05-16"
        }"""
    res = client.post('/v1/users', data=payload)
    json_data = res.get_json()
    assert json_data['status'] == "2"


def test_create_student_with_invalid_email(client):
    data = create_student(email="ddsadas@dsa.com", phone="2651655")
    payload = """{
        "action":   "register_student",
        "full_name":  "exampddldde",
        "email":  "ddsadas@dsa.com",
        "country":  "example",
        "phone":   "265156655",
        "profile_pic": "2d222",
        "birth_date":   "2015-05-16",
        "gender": false,
        "password":   "464468",
        "gender": false,
        "guardian_email": "dsadadsdsa@dsadsa.com",
        "guardian_phone": "468d686848",
        "registeration_date":   "2015-05-16"
        }"""
    res = client.post('/v1/users', data=payload)
    json_data = res.get_json()
    assert json_data['status'] == "1"


def test_create_staff(client):
    payload = """{
        "action":   "register_staff",
        "full_name":  "exampddle",
        "email":  "explsaddfdddd@dsda.com",
        "country":  "example",
        "phone":  "15656462224",
        "profile_pic": "2dddd",
        "birth_date":   "2015-05-16",
        "gender": false,
        "permission_name": "manager",
        "password":   "4644268",
        "registeration_date":   "2015-05-16"
    }"""

    res = client.post('/v1/users', data=payload)
    json_data = res.get_json()
    assert res.status_code == 200
    assert json_data['status'] == "created"


def test_create_staff_with_invalid_phone(client):
    create_staff(email="ddsad@dsa.com", phone="265155")

    payload = """{
        "action":   "register_staff",
        "full_name":  "exampddle",
        "email":  "explsaddfdddd@dsda.com",
        "country":  "example",
        "phone":  "265155",
        "profile_pic": "2dddd",
        "birth_date":   "2015-05-16",
        "gender": false,
        "permission_name": "manager",
        "password":   "4644268",
        "registeration_date":   "2015-05-16"
    }"""

    res = client.post('/v1/users', data=payload)
    json_data = res.get_json()
    assert json_data['status'] == "2"


def test_create_staff_with_invalid_email(client):
    create_staff(email="ddsad@dsa.com", phone="26533155")

    payload = """{
        "action":   "register_staff",
        "full_name":  "exampddle",
        "email":  "ddsad@dsa.com",
        "country":  "example",
        "phone":  "265155",
        "profile_pic": "2dddd",
        "birth_date":   "2015-05-16",
        "gender": false,
        "permission_name": "manager",
        "password":   "4644268",
        "registeration_date":   "2015-05-16"
    }"""

    res = client.post('/v1/users', data=payload)
    json_data = res.get_json()
    assert json_data['status'] == "1"


def test_login(client):
    data = create_student(email="ddsadas@dsa.com", phone="265156655")
    payload = """{
        "action": "login",
        "email": "ddsadas@dsa.com",
        "password": "passworddd"
    }"""
    res = client.post('/v1/users', data=payload)
    print(res.get_json())
    assert res.status_code == 200


def test_login_with_invalid_email(client):
    create_student(email="ddsadas@dsa.com", phone="265156655")
    payload = """{
        "action": "login",
        "email": "ddsad3as@dsa.com",
        "password": "passworddd"
    }"""
    res = client.post('/v1/users', data=payload)
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['message'] == "user not found"
    assert res.status_code == 404


def test_login_with_invalid_password(client):
    create_student(email="ddsad3as@dsa.com", phone="265156655")
    payload = """{
        "action": "login",
        "email": "ddsad3as@dsa.com",
        "password": "passworddde"
    }"""
    res = client.post('/v1/users', data=payload)
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['message'] == "invalid password"
    assert res.status_code == 404


def test_get_user(client):
    data = create_student(email="ddsadas@dsa.com", phone="265156655")
    jwt = generate_jwt(public_id=data['public_id'],
                       email=data['email'],
                       type=data['type'])
    res = client.get(f'/v1/users/{data["public_id"]}', headers={"x-access-token": jwt})
    print(res.get_json())
    assert res.status_code == 200


def test_get_user_with_staff(client):
    student = create_student(email="ddsadas@dsa.com", phone="265156655")
    data = create_staff(email="ddsad@dsa.com", phone="265155")
    jwt = generate_jwt(public_id=data['public_id'],
                       email=data['email'],
                       type=data['type'])
    res = client.get(f'/v1/users/{student["public_id"]}', headers={"x-access-token": jwt})
    print(res.get_json())
    assert res.status_code == 200


def test_get_user_with_invalid_token(client):
    data = create_student(email="ddsadads@dsa.com", phone="265156655")
    strange = create_student(email="ddsadadds@dsa.com", phone="26335156655")
    jwt = generate_jwt(public_id=strange['public_id'],
                       email=strange['email'],
                       type=strange['type'])
    res = client.get(f'/v1/users/{data["public_id"]}', headers={"x-access-token": jwt})
    print(res.get_json())
    assert res.status_code == 403


def test_get_invalid_user(client):
    jwt = generate_jwt(public_id="123456",
                       email="student@mail.com",
                       type="student")
    res = client.get(f'/v1/users/123456', headers={"x-access-token": jwt})
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['message'] == "Faild to query"
    assert res.status_code == 500


def test_get_all_users(client):
    create_student(email="ddsadas@dsa.com", phone="2651655")
    create_staff(email="ddsad@dsa.com", phone="265155")
    create_student(email="dds@dsa.com", phone="26515445")
    data = create_staff(email="ddsaa@dsa.com", phone="26515555")

    jwt = generate_jwt(public_id=data['public_id'],
                       email=data['email'],
                       type=data['type'])

    res = client.get('/v1/users', headers={"x-access-token": jwt})
    print(res.get_json())
    assert res.status_code == 200


def test_get_all_users_with_not_staff(client):
    create_student(email="ddsadas@dsa.com", phone="2651655")
    create_staff(email="ddsad@dsa.com", phone="265155")
    data = create_student(email="dds@dsa.com", phone="26515445")
    create_staff(email="ddsaa@dsa.com", phone="26515555")

    jwt = generate_jwt(public_id=data['public_id'],
                       email=data['email'],
                       type=data['type'])

    res = client.get('/v1/users', headers={"x-access-token": jwt})
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['message'] == "user is unauthorized"
    assert res.status_code == 403


def test_promote_user(client):
    data = create_student(email="dds@dsa.com", phone="26515445")

    jwt = generate_jwt(public_id=data['public_id'],
                       email=data['email'],
                       type=data['type'])

    payload = """{
        "full_name":  "exampddldde",
        "email":  "explsaddfddsd@dsadas.com",
        "country":  "Egypt",
        "phone":   "3213213d1213",
        "profile_pic": "default.png",
        "password":   "464468",
        "birth_date": "2010-02-03"
    }"""
    res = client.put(f'/v1/users/{data["public_id"]}', data=payload, headers={"x-access-token": jwt})
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['status'] == "updated"


def test_promote_user_with_invalid_email(client):
    create_student(email="dds@dsa.com", phone="26515445")
    data = create_student(email="dddds@dsa.com", phone="2653315445")

    jwt = generate_jwt(public_id=data['public_id'],
                       email=data['email'],
                       type=data['type'])

    payload = """{
        "full_name":  "exampddldde",
        "email":  "dds@dsa.com",
        "country":  "Egypt",
        "phone":   "3213213d1213",
        "profile_pic": "default.png",
        "password":   "464468",
        "birth_date": "2010-02-03"
    }"""
    res = client.put(f'/v1/users/{data["public_id"]}', data=payload, headers={"x-access-token": jwt})
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['status'] == "1"


def test_promote_user_with_invalid_phone(client):
    create_student(email="dds@dsa.com", phone="26515445")
    data = create_student(email="dddds@dsa.com", phone="2653315445")

    jwt = generate_jwt(public_id=data['public_id'],
                       email=data['email'],
                       type=data['type'])

    payload = """{
        "full_name":  "exampddldde",
        "email":  "dddddds@dsa.com",
        "country":  "Egypt",
        "phone":   "26515445",
        "profile_pic": "default.png",
        "password":   "464468",
        "birth_date": "2010-02-03"
    }"""
    res = client.put(f'/v1/users/{data["public_id"]}', data=payload, headers={"x-access-token": jwt})
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['status'] == "2"


def test_promote_invalid_user(client):
    create_student(email="dds@dsa.com", phone="26515445")
    data = create_student(email="dddds@dsa.com", phone="2653315445")

    jwt = generate_jwt(public_id="123145",
                       email=data['email'],
                       type=data['type'])

    payload = """{
        "full_name":  "exampddldde",
        "email":  "dddddds@dsa.com",
        "country":  "Egypt",
        "phone":   "26515445",
        "profile_pic": "default.png",
        "password":   "464468",
        "birth_date": "2010-02-03"
    }"""
    res = client.put('/v1/users/12345', data=payload, headers={"x-access-token": jwt})
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['status'] == "user is unauthorized"


def test_delete_user(client):
    data = create_student(email="dds@dsa.com", phone="26515445")

    jwt = generate_jwt(public_id=data['public_id'],
                       email=data['email'],
                       type=data['type'])

    res = client.delete(f'/v1/users/{data["public_id"]}', headers={"x-access-token": jwt})
    print(res.get_json())
    json_data = res.get_json()
    assert json_data['status'] == "deleted"

# TODO
# Delete with not staff
# Delete with invalid user
# PUT with not found public_id



