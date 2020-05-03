from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask_cors import cross_origin

from functools import wraps
from ayat.models.users import * 
from ayat import app, db
import os

HASHINGMETHOD = os.environ.get('HASHINGMETHOD')

<<<<<<< HEAD
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

=======
>>>>>>> userRoutes

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            current_user = jwt.decode(token, app.config['SECRET_KEY'])

        except:
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
        return jsonify({"error": "user is unauthorized"}), 403

    users = User.query.all()
    output = []
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
    return jsonify({'users': output}), 200


@app.route('/v1/users/<public_id>', methods=['GET'])
@cross_origin()
@token_required
def get_one_user(current_user, public_id):

    if not current_user['type'] == 'staff':
        if not current_user['public_id'] == str(public_id):
            return jsonify({"error": "user is unauthorized"}), 403

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
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

    return jsonify({'user': user}), 200



@app.route('/v1/users/<public_id>',methods=['PUT'])
@cross_origin()
@token_required
def promote_user(current_user, public_id):
    if (not current_user['type'] == 'staff') and (not current_user['public_id'] == str(public_id)):
        return jsonify({"error": "user is unauthorized"}), 403

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'}), 404

    data = request.get_json()
    if current_user['public_id'] == str(public_id):
        user.name = data['name']
        user.email = data['email']
        user.password = generate_password_hash(data['password'], method= HASHINGMETHOD)
        user.country_name = data['country_name']
        user.profile_picture = data['profile_picture']
        user.phone_number = data['phone_number']
        user.birth_date = data['birth_date']
        user.type = data['type']

    db.session.commit()
    return jsonify({'message': 'The user has been promoted!'})


@app.route('/v1/users/<public_id>',methods=['DELETE'])
@cross_origin()
@token_required
def delete_user(current_user,public_id):
    if (not current_user['type'] == 'staff') or (not current_user['public_id'] == str(public_id)):
        return jsonify({"error": "user is unauthorized"}), 403
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message':'The user has been deleted!'})


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

        user = User.query.filter_by(email=user_email).first()

        if not user:
            return jsonify({"error": "user is unauthorized"}), 403

        if check_password_hash(user.password, user_password):
            token= jwt.encode({'public_id': str(user.public_id),
                               'email': user.email,
                               'type': user.type},app.config['SECRET_KEY'])
            return jsonify({
                            'token' : token.decode('UTF-8'),
                            'public_id' : user.public_id,
                            'name' : user.name,
                            'email' : user.email ,
                            'country_name' : user.country_name ,
                            'phone_number' : user.phone_number ,
                            'profile_picture' : user.profile_picture,
                            'birth_date' : user.birth_date ,
                            'gender' : user.gender ,
            }),200
        

        return jsonify({"error": "user is unauthorized"}), 403

    # creating a new user

    if data['action'] == 'register':

        # checking if user exists or not 
        user_email = data['email']
        user = User.query.filter_by(email=user_email).first()
        if user is not None:
            return jsonify({"status":  "1"})

        user_phone = data['phone']
        user = User.query.filter_by(phone_number=user_phone).first()
        if user is not None:
            return jsonify({"status":  "2"})

        hashed_password = generate_password_hash(data['password'], method= HASHINGMETHOD)

        new_user = Student(
                        name = data['full_name'],
                        public_id=str(uuid.uuid4()),
                        email = data['email'],
                        country_name = data['country'],
                        phone_number = data['phone'],
                        profile_picture = data['profile_pic'],
                        birth_date = data['birth_date'],
                        gender = data['gender'],
                        password=hashed_password,
                        registeration_date = data['registeration_date'],
                        type = "student",
                        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify({'status' : 'created'}),200
