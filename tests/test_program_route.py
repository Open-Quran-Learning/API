from .conftest import create_staff, create_student, generate_jwt, create_program


def test_staff_creating_program(client):
    payload = """{
    "program_name": "Heynow2",
    "program_level": "easy",
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
    "requirement" : {
        "min_age": 15,
        "max_age": 25,
        "gender": true
    },
    "is_open_to_public": true,
    "start_date" : "2015-05-05",
    "end_date" : "2015-05-05",
    "skills":[
        {"name":"sdf"},
        {"name":"hello"}],
    "available": true
}"""

    staff = create_staff('teststaff@email.com', '0123456789')
    jwt = generate_jwt(
        public_id=staff['public_id'],
        email=staff['email'],
        type=staff['type'],
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

# def test_student_creating_program(client):
#     payload = """{
#    "program_name": "Name example",
#     "prerequisite": [
#       {
#         "public_program_id": "e885f927-2b95-4a27-b1c4-223d21f429d0"
#       },
#       {
#         "public_program_id": "e885f927-2b95-4a27-b1c4-223d21f429d0"
#       }
#     ],
#     "program_level": "Difficulty",
#     "program_category": [
#       {
#         "type": "tessxt"
#       },
#       {
#         "type": "tesss2xt"
#       }
#     ],
#     "price": "551",
#     "program_pic": "<Pic>",
#     "FAQ": [
#       {
#         "question": "Text",
#         "answer": "Text"
#       },
#       {
#         "question": "Text",
#         "answer": "Text"
#       }
#     ],
#     "program_cover": "<Local pic>",
#     "Program_description": "text example",
#     "available": true,
#     "is_open_to_public": true,
#     "start_date" : "2015-05-05",
#     "end_date" : "2015-05-05",
#     "requirement":{
#             "min_age": "5",
#             "max_age": "20",
#             "gender" : false
#     },
#     "skills":[
#     {
#     "name":"sdf"
#     },
#     {
#     "name":"hello"
#     }
#     ]
# }"""
#     data = create_student('teststudent@email.com', '0123456789')
#     jwt = generate_jwt(
#         public_id=data['public_id'],
#         email=data['email'],
#         type=data['type'],
#     )
#
#     res = client.post(
#         '/v1/programs',
#         data=payload,
#         headers={'x-access-token': jwt}
#     )
#
#     json_data = res.get_json()
#     assert res.status_code == 403
#     assert json_data['status'] == 'forbidden'
#
#
# def test_staff_creating_program_without_token(client):
#     payload = """{
#    "program_name": "Name example",
#     "prerequisite": [
#       {
#         "public_program_id": "e885f927-2b95-4a27-b1c4-223d21f429d0"
#       },
#       {
#         "public_program_id": "e885f927-2b95-4a27-b1c4-223d21f429d0"
#       }
#     ],
#     "program_level": "Difficulty",
#     "program_category": [
#       {
#         "type": "tessxt"
#       },
#       {
#         "type": "tesss2xt"
#       }
#     ],
#     "price": "551",
#     "program_pic": "<Pic>",
#     "FAQ": [
#       {
#         "question": "Text",
#         "answer": "Text"
#       },
#       {
#         "question": "Text",
#         "answer": "Text"
#       }
#     ],
#     "program_cover": "<Local pic>",
#     "Program_description": "text example",
#     "available": true,
#     "is_open_to_public": true,
#     "start_date" : "2015-05-05",
#     "end_date" : "2015-05-05",
#     "requirement":{
#             "min_age": "5",
#             "max_age": "20",
#             "gender" : false
#     },
#     "skills":[
#     {
#     "name":"sdf"
#     },
#     {
#     "name":"hello"
#     }
#     ]
# }"""
#
#     res = client.post(
#         '/v1/programs',
#         data=payload
#     )
#
#     json_data = res.get_json()
#     assert res.status_code == 401
#     assert json_data['message'] == 'Token is missing'
#
#
# def test_student_editing_program(client):
#     payload = """{
#             "program_name": "Name example",
#             "program_level": "Difficulty",
#             "program_category": [
#                 {
#                     "type": "tessxt"
#                 },
#                 {
#                     "type": "tesss2xt"
#                 }
#             ],
#             "price": "551",
#             "program_pic": "<Pic>",
#             "FAQ": [
#                 {
#                     "question": "Text",
#                     "answer": "Text"
#                 },
#                 {
#                     "question": "Text",
#                     "answer": "Text"
#                 }
#             ],
#             "program_cover": "<Local pic>",
#             "Program_description": "text example",
#             "available": true,
#             "is_open_to_public": true,
#             "start_date": "2015-05-05",
#             "end_date": "2015-05-05",
#             "requirement": {
#                 "min_age": 5,
#                 "max_age": 25,
#                 "gender": false
#             },
#             "skills": [
#                 {
#                     "name": "sdf"
#                 },
#                 {
#                     "name": "hello"
#                 }
#             ]
#         }"""
#
#     program = create_program('Test Course')
#     student = create_student('student@email.com', '745465465')
#     jwt = generate_jwt(
#         student['public_id'],
#         student['email'],
#         student['type']
#     )
#
#     res = client.put(
#         f'/v1/programs/{program["public_id"]}',
#         data=payload,
#         headers={'x-access-token': jwt}
#     )
#
#     json_data = res.get_json()
#     assert res.status_code == 403
#     # assert json_data['status'] == b'forbidden'
#     assert b'forbidden' in res.data
#
#
# def test_staff_editing_existing_program(client):
#     payload = """{
#             "program_name": "Name example",
#             "program_level": "Difficulty",
#             "program_category": [
#                 {
#                     "type": "tessxt"
#                 },
#                 {
#                     "type": "tesss2xt"
#                 }
#             ],
#             "price": "551",
#             "program_pic": "<Pic>",
#             "FAQ": [
#                 {
#                     "question": "Text",
#                     "answer": "Text"
#                 },
#                 {
#                     "question": "Text",
#                     "answer": "Text"
#                 }
#             ],
#             "program_cover": "<Local pic>",
#             "Program_description": "text example",
#             "available": true,
#             "is_open_to_public": true,
#             "start_date": "2015-05-05",
#             "end_date": "2015-05-05",
#             "requirement": {
#                 "min_age": 5,
#                 "max_age": 25,
#                 "gender": false
#             },
#             "skills": [
#                 {
#                     "name": "sdf"
#                 },
#                 {
#                     "name": "hello"
#                 }
#             ]
#         }"""
#     program = create_program('Test Course')
#     staff = create_staff('staff@email.com', '745465465')
#     jwt = generate_jwt(
#         staff['public_id'],
#         staff['email'],
#         staff['type']
#     )
#
#     res = client.put(
#         f'/v1/programs/{program["public_id"]}',
#         data=payload,
#         headers={'x-access-token': jwt}
#     )
#
#     json_data = res.get_json()
#     assert res.status_code == 200
#     # assert json_data['status'] == b'edited'
#     assert b'edited' in res.data
#
#
# def test_staff_editing_not_existing_program(client):
#     payload = """{
#             "program_name": "Name example",
#             "program_level": "Difficulty",
#             "program_category": [
#                 {
#                     "type": "tessxt"
#                 },
#                 {
#                     "type": "tesss2xt"
#                 }
#             ],
#             "price": "551",
#             "program_pic": "<Pic>",
#             "FAQ": [
#                 {
#                     "question": "Text",
#                     "answer": "Text"
#                 },
#                 {
#                     "question": "Text",
#                     "answer": "Text"
#                 }
#             ],
#             "program_cover": "<Local pic>",
#             "Program_description": "text example",
#             "available": true,
#             "is_open_to_public": true,
#             "start_date": "2015-05-05",
#             "end_date": "2015-05-05",
#             "requirement": {
#                 "min_age": 5,
#                 "max_age": 25,
#                 "gender": false
#             },
#             "skills": [
#                 {
#                     "name": "sdf"
#                 },
#                 {
#                     "name": "hello"
#                 }
#             ]
#         }"""
#     program_id = 'sssss'
#     staff = create_staff('staff@email.com', '745465465')
#     jwt = generate_jwt(
#         staff['public_id'],
#         staff['email'],
#         staff['type'])
#
#     res = client.put(
#         f'/v1/programs/{program_id}',
#         data=payload,
#         headers={'x-access-token': jwt}
#     )
#
#     assert res.status_code == 404
#
#
# def test_retrieve_existing_program(client):
#     program = create_program('Test Program')
#
#     res = client.get(
#         f'/v1/programs/{program["public_id"]}'
#     )
#
#     json_data = res.get_json()
#
#     assert res.status_code == 200
#     assert json_data['program_name'] == program['program_name']
#
#
# def test_retrieve_not_existing_program(client):
#     program_id = 'test'
#
#     res = client.get(
#         f'/v1/programs/{program_id}'
#     )
#
#     assert res.status_code == 404
#     assert b'content not found' in res.data
#
#
# def test_delete_existing_program_with_privileged_user(client):
#     staff = create_staff('staff@email.com', '124566')
#     program = create_program('test program')
#     jwt = generate_jwt(
#         staff['public_id'],
#         staff['email'],
#         staff['type']
#     )
#
#     res = client.delete(
#         f'/v1/programs/{program["public_id"]}',
#         headers={'x-access-token': jwt}
#     )
#
#     assert res.status_code == 200
#     assert b'deleted' in res.data
#
#
# def test_delete_not_existed_program(client):
#     program_id = '454121'
#     staff = create_staff('staff@email.com', '45460')
#     jwt = generate_jwt(
#         staff['public_id'],
#         staff['email'],
#         staff['type']
#     )
#
#     res = client.delete(
#         f'/v1/programs/{program_id}',
#         headers={'x-access-token': jwt}
#     )
#
#     assert res.status_code == 404
#     assert b'program not found' in res.data
#
#
# def test_delete_program_with_unprivileged_user(client):
#     student = create_student('student@email.com', '124566')
#     program = create_program('test program')
#     jwt = generate_jwt(
#         student['public_id'],
#         student['email'],
#         student['type']
#     )
#
#     res = client.delete(
#         f'/v1/programs/{program["public_id"]}',
#         headers={'x-access-token': jwt}
#     )
#
#     assert res.status_code == 403
#     assert b'forbidden' in res.data
#
#
# def test_student_subscribing_to_program(client):
#     student = create_student('student99@email.com', '1548732')
#     program = create_program('test program')
#     jwt = generate_jwt(
#         student['public_id'],
#         student['email'],
#         student['type']
#     )
#
#     res = client.post(
#         f'/v1/programs/{program["public_id"]}/enrollments',
#         headers={'x-access-token': jwt}
#     )
#     assert res.status_code == 200
#     assert b'enrolled' in res.data
#
#
# def test_staff_subscribing_to_program(client):
#     staff = create_staff('staff44@email.com', '44692310')
#     program = create_program('test program')
#     jwt = generate_jwt(
#         staff['public_id'],
#         staff['email'],
#         staff['type']
#     )
#
#     res = client.post(
#         f'/v1/programs/{program["public_id"]}/enrollments',
#         headers={'x-access-token': jwt}
#     )
#     assert res.status_code == 403
#     assert b'you are a staff member' in res.data
#
#
# def test_student_subscribing_to_program_again(client):
#     student = create_student('student66@email.com', '54616567')
#     program = create_program('test program')
#     jwt = generate_jwt(
#         student['public_id'],
#         student['email'],
#         student['type']
#     )
#
#     res = client.post(
#         f'/v1/programs/{program["public_id"]}/enrollments',
#         headers={'x-access-token': jwt}
#     )
#
#     assert res.status_code == 403  # there is no code in docs and programs_routes.py file
#     assert b'User is already subscribed' in res.data
#
#
# def test_enrolled_student_cancel_subscription(client):
#     student = create_student('student33@email.com', '793001546')
#     program = create_program('test program')
#     jwt = generate_jwt(
#         student['public_id'],
#         student['email'],
#         student['type']
#     )
#
#     res = client.delete(
#         f'/v1/programs/{program["public_id"]}/enrollments',
#         headers={'x-access-token': jwt}
#     )
#
#     assert res.status_code == 200
#     assert b'success' in res.data
#
#
# def test_not_enrolled_student_cancel_subscription(client):
#     student = create_student('student11@email.com', '67946130')
#     program = create_program('test program')
#     jwt = generate_jwt(
#         student['public_id'],
#         student['email'],
#         student['type']
#     )
#
#     res = client.delete(
#         f'/v1/programs/{program["public_id"]}/enrollments',
#         headers={'x-access-token': jwt}
#     )
#
#     assert res.status_code == 403
#     assert b'user not enrolled' in res.data
