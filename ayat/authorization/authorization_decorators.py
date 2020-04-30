from flask import request, jsonify
import jwt
from functools import wraps
from ayat.models.users import User
from ayat import app


def teacher_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        try:
            current_user = jwt.decode(token, app.config['SECRET_KEY'])
            if not current_user['type'] == 'staff':
                return jsonify({'error': 'user is unauthorized'}), 403

            user = User.query.filter_by(public_id=current_user['public_id']).first()

            if not user.type.permission == 'teacher':
                return jsonify({'message': 'user is unauthorized'}), 403

        except:
            return jsonify({'message': 'invalid token!'}), 403
        return f(current_user, *args, **kwargs)

    return decorated


def teacher_or_above_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        try:
            current_user = jwt.decode(token, app.config['SECRET_KEY'])
            if not current_user['type'] == 'staff':
                return jsonify({'error': 'user is unauthorized'}), 403

            user = User.query.filter_by(public_id=current_user['public_id']).first()

            if user.type.permission == 'student':
                return jsonify({'message': 'user is unauthorized'}), 403

        except:
            return jsonify({'message': 'invalid token!'}), 403
        return f(current_user, *args, **kwargs)

    return decorated


def supervisor_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        try:
            current_user = jwt.decode(token, app.config['SECRET_KEY'])
            if not current_user['type'] == 'staff':
                return jsonify({'error': 'user is unauthorized'}), 403

            user = User.query.filter_by(public_id=current_user['public_id']).first()

            if not user.type.permission == 'supervisor':
                return jsonify({'message': 'user is unauthorized'}), 403

        except:
            return jsonify({'message': 'invalid token!'}), 403
        return f(current_user, *args, **kwargs)

    return decorated


def supervisor_or_above_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        try:
            current_user = jwt.decode(token, app.config['SECRET_KEY'])
            if not current_user['type'] == 'staff':
                return jsonify({'error': 'user is unauthorized'}), 403

            user = User.query.filter_by(public_id=current_user['public_id']).first()

            if user.type.permission == 'teacher' or user.type.permission == 'student':
                return jsonify({'message': 'user is unauthorized'}), 403

        except:
            return jsonify({'message': 'invalid token!'}), 403
        return f(current_user, *args, **kwargs)

    return decorated


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        try:
            current_user = jwt.decode(token, app.config['SECRET_KEY'])
            if not current_user['type'] == 'staff':
                return jsonify({'error': 'user is unauthorized'}), 403

            user = User.query.filter_by(public_id=current_user['public_id']).first()

            if not user.type.permission == 'admin':
                return jsonify({'message': 'user is unauthorized'}), 403

        except:
            return jsonify({'message': 'invalid token!'}), 403
        return f(current_user, *args, **kwargs)

    return decorated
