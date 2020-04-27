from flask import Flask, request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
import jwt
# you need to install jwt >> using >>> pip install jwt 

# from functools import wraps
from ayat.models.programs import *
from ayat.models.users import *
from ayat.authentication_routes import  token_required
from ayat import app, db


@app.route('/v1/programs', methods=['POST'])
@token_required
def create_program(current_user):

    if not current_user['type'] == 'staff':
        return jsonify({"status": "forbidden"}), 403

    data = request.get_json()

    new_program = Program(

                            public_program_id = str(uuid.uuid4()),
                            program_name = data['program_name'],
                            difficulty_level = data['program_level'],
                            price = data['price'],
                            program_picture = data['program_pic'],
                            program_cover = data['program_cover'],
                            program_description = data['Program_description'],
                            available = data['available'],
                            # ######

    )

    new_program_faqs = data['FAQ']
    for faq in new_program_faqs:
        new_program.faqs = faq
    

    
    db.session.add(new_program)
    db.session.commit()
    return jsonify({'status' : 'created'}),200




@app.route('/v1/programs/<public_id>', methods=['PUT'])
@token_required
def edit_program():
    
    return {}


@app.route('/v1/programs/<public_id>', methods=['GET'])
def retrieve_program(public_id):

    current_program = Program.query.filter_by(public_program_id=public_id).first()

    if not current_program :
        return jsonify({'status': "content not found"}),404
    
    #### ??????
    prerequisites = current_program.prerequisites


    return jsonify({

                    'program_name':current_program.program_name,
                    'prerequisite' : prerequisites, 
                    'program_level' : current_program.difficulty_level,
                    'program_category': '',
                    'price': current_program.price,
                    'program_pic' : current_program.program_picture,
                    'FAQ' : '',
                    'program_cover' : current_program.program_cover,
                    'Program_description' : current_program.program_description,
                    'available' : current_program.available,



    })

@app.route('/v1/programs/<public_id>', methods=['DELETE'])
@token_required
def delete_program(current_user, public_id):

    if not current_user['type'] == 'staff':
        return jsonify({"status": "forbidden"}), 403
    
    program_to_delete = Program.query.filter_by(public_program_id=public_id).first()

    db.session.delete(program_to_delete)
    db.session.commit()
    return jsonify({'status': 'deleted'}),200
    



@app.route('/v1/programs/<public_id>/enrollments', methods=['POST'])
def subscribe():
    
    return {}



@app.route('/v1/programs/<public_id>/enrollments', methods=['DELETE'])
def cancel_subscription():
    
    return {}
