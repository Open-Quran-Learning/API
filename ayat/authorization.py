from flask import Flask, request,jsonify
from ayat import app
# import requests

from .data_model import *

from functools import wraps


def logged_in_required(original_function):

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        
        current_user_token = request.json['token']
        current_user = User.query.filter_by(token = current_user_token).first()

        if not current_user:
            return jsonify({

                'status': 404
            })
        else:
            return original_function(*args, **kwargs)

    return wrapper



def admin_required(original_function):

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        
        current_user_token = request.json['token']

        current_user = User.query.filter_by(token = current_user_token).first()
        if not current_user:
            return jsonify({

                'status': 404
            })

        current_user_admin_check = current_user.user_type_id

        if  current_user_admin_check != 1:
            return jsonify({

                'status': 404
            })
        
        return original_function(*args, **kwargs) 
    
       

    return wrapper
    