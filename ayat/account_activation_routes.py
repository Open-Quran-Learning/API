from flask import Flask, request, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask_cors import cross_origin

from functools import wraps
from ayat.models.users import *
from ayat import app, db

from ayat.helpers import send_message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature

import os
import logging

from ayat import mail
from flask_mail import Message





serializer = URLSafeTimedSerializer("thisissecret")

@app.route("/v1/users/<public_id>/confirm",methods=['GET']) #'POST',
@cross_origin()
def confirm_email(public_id):

    data = request.get_json(force=True)

    current_user = User.query.filter_by(public_id=public_id ).first()
    if not current_user:
        return jsonify({'status': 'user not found'})
    # if request.method == "POST":
    #     current_user_email = data["email"]
    #     user_email_check = User.query.filter_by(email= current_user_email ).first()
    #     if user_email_check is not None and str(current_user.email) != str(user_email_check.email):
    #         return jsonify({"status":"email exists"})

    user_email = current_user.email
    token_email = serializer.dumps(user_email, salt= "email_confirm")
    confirmation_link = url_for('confirm_email_token', token = token_email, public_id = public_id, _external = True)
    content = f"Welcome to ayat. \n This is the link to confirm your email which will expire in two hours. \n link : \n {confirmation_link}"
    msg = Message("Ayat Email Confirmation",sender="ayatquraancenter@gmail.com",recipients=user_email.split())
    msg.body = content
    mail.send(msg)  
    # send_message(subject="Ayat Email Confirmation",recipients= user_email,content= content,html_content= "<h1>hello</h1>", resource="hello.jpg",resource_type= "jpg")
    

    return jsonify({"status":"message was sent"})







@app.route("/v1/users/<public_id>/confirm/<token>",methods=['GET']) #'POST',
@cross_origin()
def confirm_email_token(token, public_id):

    twoHours = 60*60*2

    try:
        email = serializer.loads(token, salt= "email_confirm", max_age= twoHours)
        user_to_activate = User.query.filter_by(public_id = public_id).first()
        user_to_activate.is_activated = True
        db.session.commit()
    
    except SignatureExpired:
         return jsonify({"status":"token has expired"})
    
    except BadTimeSignature:
        return jsonify({"status":"token is damaged"})

    return jsonify({"status":"confirmed"}),200
