from flask import Flask, request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
import jwt
# you need to install jwt >> using >>> pip install jwt 

# from functools import wraps
from ayat.models.programs import *
from ayat import app, db


@app.route('/v1/programs', methods=['POST'])
def create_program():
    
    return {}



@app.route('/v1/programs/<public_id>', methods=['PUT'])
def edit_program():
    
    return {}


@app.route('/v1/programs/<public_id>', methods=['GET'])
def retrieve_program():
    
    return {}

@app.route('/v1/programs/<public_id>', methods=['DELETE'])
def delete_program():
    
    return {}



@app.route('/v1/programs/<public_id>/enrollments', methods=['POST'])
def subscribe():
    
    return {}



@app.route('/v1/programs/<public_id>/enrollments', methods=['DELETE'])
def cancel_subscription():
    
    return {}
