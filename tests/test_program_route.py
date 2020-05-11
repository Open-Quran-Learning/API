from .conftest import create_staff, create_student, generate_jwt, create_program


# Abd-Elsattar
# TODO: test_student_subscribing_to_program
# TODO: test_staff_subscribing_to_program
# TODO: test_student_subscribing_to_program_again
# TODO: test_enrolled_student_cancel_subscription
# TODO: test_not_enrolled_student_cancel_subscription


def test_staff_creating_program(client):
    payload = """{
        "program_name": "program name",
        "program_level": "Medium",
        "price": "551",
        "program_pic": "pic",
        "program_cover": "Local pic",
        "Program_description": "text example",
        "available": true
    }"""
    data = create_staff('teststaff@email.com', '0123456789')
    jwt = generate_jwt(
        public_id=data['public_id'],
        email=data['email'],
        type=data['type'],
    )

    res = client.post(
        '/v1/programs',
        data=payload,
        headers={'x-access-token': jwt}
    )

    json_data = res.get_json()
    assert res.status_code == 200
    # assert json_data['status'] == b'created'
    assert b'created' in res.data


def test_student_creating_program(client):
    payload = """{
   "program_name": "<Name example>",

    "prerequisite": [
      {
        "name": "name of already exist program"
      },
      {
        "name": "name of already exist program"
      }
    ],
    "program_level": "<Difficulty>",

    "program_category": [
      {
        "type": "text"
      },
      {
        "type": "text"
      }
    ],

    "price": "551",

    "program_pic": "<Pic>",

    "FAQ": [
      {
        "question": "Text",
        "answer": "Text"
      },
      {
        "question": "Text",
        "answer": "Text"
      }
    ],

    "program_cover": "<Local pic>",

    "Program_description": "text example",

    "available": true

}"""
    data = create_student('teststudent@email.com', '0123456789')
    jwt = generate_jwt(
        public_id=data['public_id'],
        email=data['email'],
        type=data['type'],
    )

    res = client.post(
        '/v1/programs',
        data=payload,
        headers={'x-access-token': jwt}
    )

    json_data = res.get_json()
    assert res.status_code == 403
    assert json_data['status'] == b'forbidden'


def test_staff_creating_program_without_token(client):
    payload = """{
   "program_name": "<Name example>",

    "prerequisite": [
      {
        "name": "name of already exist program"
      },
      {
        "name": "name of already exist program"
      }
    ],
    "program_level": "<Difficulty>",

    "program_category": [
      {
        "type": "text"
      },
      {
        "type": "text"
      }
    ],

    "price": "551",

    "program_pic": "<Pic>",

    "FAQ": [
      {
        "question": "Text",
        "answer": "Text"
      },
      {
        "question": "Text",
        "answer": "Text"
      }
    ],

    "program_cover": "<Local pic>",

    "Program_description": "text example",

    "available": true

}"""

    res = client.post(
        '/v1/programs',
        data=payload
    )

    json_data = res.get_json()
    assert res.status_code == 403
    assert json_data['status'] == b'user is unauthorized'


def test_student_editing_program(client):
    payload = 'test'
    program = create_program('Test Course')
    student = create_student('student@email.com', '745465465')
    jwt = generate_jwt(
        student['public_id'],
        student['email'],
        student['type']
    )

    res = client.put(
        f'/v1/programs/{program["public_id"]}',
        data=payload,
        headers={'x-access-token': jwt}
    )

    json_data = res.get_json()
    assert res.status_code == 403
    # assert json_data['status'] == b'forbidden'
    assert b'forbidden' in res.data


def test_staff_editing_existing_program(client):
    payload = 'test'
    program = create_program('Test Course')
    staff = create_staff('staff@email.com', '745465465')
    jwt = generate_jwt(
        staff['public_id'],
        staff['email'],
        staff['type']
    )

    res = client.put(
        f'/v1/programs/{program["public_id"]}',
        data=payload,
        headers={'x-access-token': jwt}
    )

    json_data = res.get_json()
    assert res.status_code == 200
    # assert json_data['status'] == b'edited'
    assert b'edited' in res.data


def test_staff_editing_not_existing_program(client):
    payload = 'test'
    program_id = 'sssss'
    staff = create_staff('staff@email.com', '745465465')
    jwt = generate_jwt(
        staff['public_id'],
        staff['email'],
        staff['type'])

    res = client.put(
        f'/v1/programs/{program_id}',
        data=payload,
        headers={'x-access-token': jwt}
    )

    assert res.status_code == 404


def test_retrieve_existing_program(client):
    program = create_program('Test Program')

    res = client.get(
        f'/v1/programs/{program["public_id"]}'
    )

    json_data = res.get_json()

    assert res.status_code == 200
    assert json_data['program_name'] == program['program_name']


def test_retrieve_not_existing_program(client):
    program_id = 'test'

    res = client.get(
        f'/v1/programs/{program_id}'
    )

    assert res.status_code == 404
    assert b'content not found' in res.data


def test_delete_existing_program_with_privileged_user(client):
    staff = create_staff('staff@email.com', '124566')
    program = create_program('test program')
    jwt = generate_jwt(
        staff['public_id'],
        staff['email'],
        staff['type']
    )

    res = client.delete(
        f'/v1/programs/{program["public_id"]}',
        headers={'x-access-token': jwt}
    )

    assert res.status_code == 200
    assert b'deleted' in res.data


def test_delete_not_existed_program(client):
    program_id = '454121'
    staff = create_staff('staff@email.com', '45460')
    jwt = generate_jwt(
        staff['public_id'],
        staff['email'],
        staff['type']
    )

    res = client.delete(
        f'/v1/programs/{program_id}',
        headers={'x-access-token': jwt}
    )

    assert res.status_code == 404
    assert b'program not found' in res.data


def test_delete_program_with_unprivileged_user(client):
    student = create_student('student@email.com', '124566')
    program = create_program('test program')
    jwt = generate_jwt(
        student['public_id'],
        student['email'],
        student['type']
    )

    res = client.delete(
        f'/v1/programs/{program["public_id"]}',
        headers={'x-access-token': jwt}
    )

    assert res.status_code == 403
    assert b'forbidden' in res.data
