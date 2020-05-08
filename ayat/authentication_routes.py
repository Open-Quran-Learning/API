from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask_cors import cross_origin

from functools import wraps
from ayat.models.users import *
from ayat import app, db
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
file_handler = logging.FileHandler('logging.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
HASHINGMETHOD = "sha256"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            logger.warning('missing the token')
            return jsonify({'message': 'Token is missing'}), 401

        try:
            current_user = jwt.decode(token, app.config['SECRET_KEY'])
            logger.info('success to decode token')

        except:
            logger.exception('Token is invalid')
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/')
@cross_origin()
def index():
    return 'Welcome to Ayat'


@app.route('/v1/users', methods=['GET'])
@cross_origin()
@token_required
def get_all_users(current_user):
    if not current_user['type'] == 'staff':
        logger.warning('user is unauthorized')
        return jsonify({"message": "user is unauthorized"}), 403
    try:
        users = User.query.all()
        if users:
            output = []
            logger.info('succeeded to query')
            for user in users:
                user_data = {
                    'public_id': user.public_id,
                    'email': user.email,
                    'country_name': user.country_name,
                    'phone_number': user.phone_number,
                    'profile_picture': user.profile_picture,
                    'birth_date': user.birth_date,
                    'gender': user.gender,
                    'registeration_date': user.registeration_date,
                    'is_activated': user.is_activated,
                    'type': user.type
                }

                output.append(user_data)
        else:
            logger.warning('user not found')
            return jsonify({'message': 'No user found!'}), 404
    except:
        logger.warning('faild to query')
        return jsonify({'message': 'Faild to query'}), 500

    return jsonify({'users': output}), 200


@app.route('/v1/users/<public_id>', methods=['GET'])
@cross_origin()
@token_required
def get_one_user(current_user, public_id):
    if not current_user['type'] == 'staff':
        if not current_user['public_id'] == str(public_id):
            logger.warning('user is unauthorized')
            return jsonify({"message": "user is unauthorized"}), 403
    try:
        user = User.query.filter_by(public_id=public_id).first()
        if not user:
            logger.warning('user not found ')
            return jsonify({'message': 'No user found!'}), 404

        user = {
            'public_id': user.public_id,
            'email': user.email,
            'country_name': user.country_name,
            'phone_number': user.phone_number,
            'profile_picture': user.profile_picture,
            'birth_date': user.birth_date,
            'gender': user.gender,
            'registeration_date': user.registeration_date,
            'is_activated': user.is_activated,
            'type': user.type
        }
        logger.info('succeeded to query')
        return jsonify({'user': user}), 200

    except:
        logger.exception('faild to query')
        return jsonify({'message': 'Faild to query'}), 500


@app.route('/v1/users/<public_id>', methods=['PUT'])
@cross_origin()
@token_required
def promote_user(current_user, public_id):
    data = request.get_json(force=True)
    # if (not current_user['type'] == 'staff') and (not current_user['public_id'] == str(public_id)):
    #     return jsonify({"error": "user is unauthorized"}), 403
    if (not current_user['type'] == 'staff') and (not current_user['public_id'] == str(public_id)):
        logger.warning('user is unauthorized')
        return jsonify({"status": "user is unauthorized"}), 403
    elif (not current_user['public_id'] == str(public_id)) and current_user['type'] == 'student':
        return jsonify({"status": "user is unauthorized"}), 403

    user_email = data['email']
    user = User.query.filter_by(email=user_email).first()
    if user is not None:
        if str(user.public_id) != str(public_id) and (not current_user['type'] == 'staff'):
            print(current_user['type'])
            return jsonify({"status": "1"})

    user_phone = data['phone']
    user = User.query.filter_by(phone_number=user_phone).first()
    if user is not None:
        if str(user.public_id) != str(public_id) and (not current_user['type'] == 'staff'):
            return jsonify({"status": "2"})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        logger.warning('user not found ')
        return jsonify({'message': 'No user found!'}), 404

    # if current_user['public_id'] == str(public_id):
    user.name = data['full_name']
    user.email = data['email']
    user.password = generate_password_hash(data['password'], method=HASHINGMETHOD)
    user.country_name = data['country']
    user.profile_picture = data['profile_pic']
    user.phone_number = data['phone']
    user.birth_date = data['birth_date']

    # if current_user['type'] == 'staff':
    #     user.type = data['type']

    # db.session.add(user)
    try:
        db.session.commit()
        return jsonify({"status": "updated"})
    except:
        return jsonify({"status": "you changed the mail or phone with existing one"})


@app.route('/v1/users/<public_id>', methods=['DELETE'])
@cross_origin()
@token_required
def delete_user(current_user, public_id):
    if (not current_user['type'] == 'staff') and (not current_user['public_id'] == str(public_id)):
        logger.warning('user is unauthorized')
        return jsonify({"status": "user is unauthorized"}), 403
    elif (not current_user['public_id'] == str(public_id)) and current_user['type'] == 'student':
        return jsonify({"status": "user is unauthorized"}), 403

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        logger.warning('user not found ')
        return jsonify({'status': 'no user found'})
    db.session.delete(user)
    db.session.commit()

    logger.info('succeeded to deleted')
    return jsonify({'status': 'deleted'}), 200


@app.route('/v1/users', methods=['POST'])
@cross_origin()
def login_or_create():
    data = request.get_json(force=True)
    print(data)
    # login checking
    print('this is request')
    print(request)
    print('this is data')
    print(data)
    # if not data['action'] :
    #     return jsonify({"error": "user is unauthorized"}), 403

    if data['action'] == 'login':

        user_email = data['email']
        user_password = data['password']

        try:
            user = User.query.filter_by(email=user_email).first()

            if not user:
                logger.warning('user not found')
                return jsonify({"message": "user not found"}), 404

            if check_password_hash(user.password, user_password):
                token = jwt.encode({'public_id': str(user.public_id),
                                    'email': user.email,
                                    'type': user.type}, app.config['SECRET_KEY'])
                logger.info('user succeeded to login')
                return jsonify({
                    'token': token.decode('UTF-8'),
                    'public_id': user.public_id,
                    'name': user.name,
                    'email': user.email,
                    'country_name': user.country_name,
                    'phone_number': user.phone_number,
                    'profile_picture': user.profile_picture,
                    'birth_date': user.birth_date,
                    'gender': user.gender,
                }), 200
            else:
                logger.warning('invalid password')
                return jsonify({'message': 'invalid password'}), 404

        except:
            logger.exception('faild to login')
            return jsonify({'message': 'user is unauthorized'}), 403

        # return jsonify({"error": "user is unauthorized"}), 403

    # creating a new user

    if data['action'] == 'register_student':

        # checking if user exists or not 
        user_email = data['email']
        user = User.query.filter_by(email=user_email).first()
        if user is not None:
            return jsonify({"status": "1"})

        user_phone = data['phone']
        user = User.query.filter_by(phone_number=user_phone).first()
        if user is not None:
            return jsonify({"status": "2"})

        hashed_password = generate_password_hash(data['password'], method=HASHINGMETHOD)
        new_guardian = Guardian(
            email=data['guardian_email'],
            phone_number=data['guardian_phone']
        )
        new_user = Student(
            name=data['full_name'],
            public_id=str(uuid.uuid4()),
            email=data['email'],
            country_name=data['country'],
            phone_number=str(data['phone']),
            profile_picture=data['profile_pic'],
            birth_date=data['birth_date'],
            gender=data['gender'],
            password=hashed_password,
            registeration_date=data['registeration_date'],
            type="student"
        )
        db.session.add(new_guardian)
        new_user.guardians.append(new_guardian)
        db.session.add(new_user)
        db.session.commit()
        logger.info('user succeeded to register')
        return jsonify({'status': 'created'}), 200

    if data['action'] == 'register_staff':

        # checking if user exists or not 
        user_email = data['email']
        user = User.query.filter_by(email=user_email).first()
        if user is not None:
            logger.info('email is already existed')
            return jsonify({"status": "1"})

        user_phone = data['phone']
        user = User.query.filter_by(phone_number=user_phone).first()
        if user is not None:
            logger.info('phone number is already existed')
            return jsonify({"status": "2"})

        hashed_password = generate_password_hash(data['password'], method=HASHINGMETHOD)
        new_permission = Permission(
            permission_name=data['permission_name']
        )
        new_user = Staff(
            name=data['full_name'],
            public_id=str(uuid.uuid4()),
            email=data['email'],
            country_name=data['country'],
            phone_number=data['phone'],
            profile_picture=data['profile_pic'],
            birth_date=data['birth_date'],
            gender=data['gender'],
            password=hashed_password,
            registeration_date=data['registeration_date'],
            type="staff",
        )
        db.session.add(new_permission)
        new_user.permissions.append(new_permission)
        db.session.add(new_user)
        db.session.commit()
        logger.info('user succeeded to register')
        return jsonify({'status': 'created'}), 200
