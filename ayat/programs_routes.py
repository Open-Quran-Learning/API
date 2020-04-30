from flask import Flask, request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
import jwt
# you need to install jwt >> using >>> pip install jwt 

# from functools import wraps
from ayat.models.programs import *
from ayat.models.users import *
from ayat.models.assessments import *
from ayat.authentication_routes import  token_required
from ayat import app, db
from datetime import  date

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
    new_program_prerequisites = data['prerequisite']
    for prerequisite in new_program_prerequisites:
        
        new_program.prerequisites.append(prerequisite) 


    new_program_categories = data['program_category']
    for category in new_program_categories:
        new_category = Category(category_name = category['type'])
        db.session.add(new_category)
        new_program.category.append(new_category)

    new_program_faqs = data['FAQ']
    for faq in new_program_faqs:
        new_faq = Faq(question = faq['question'] , answer = 'answer')
        db.session.add(new_faq)
        new_program.category.append(new_faq)

    
    db.session.add(new_program)
    db.session.commit()
    return jsonify({'status' : 'created'}),200




@app.route('/v1/programs/<public_id>', methods=['PUT'])
@token_required
def edit_program(current_user):

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
    new_program_prerequisites = data['prerequisite']
    for prerequisite in new_program_prerequisites:
        
        new_program.prerequisites.append(prerequisite) 


    new_program_categories = data['program_category']
    for category in new_program_categories:
        new_category = Category(category_name = category['type'])
        db.session.add(new_category)
        new_program.category.append(new_category)

    new_program_faqs = data['FAQ']
    for faq in new_program_faqs:
        new_faq = Faq(question = faq['question'] , answer = 'answer')
        db.session.add(new_faq)
        new_program.category.append(new_faq)

    
    db.session.add(new_program)
    db.session.commit()
    return jsonify({'status' : 'created'}),200



@app.route('/v1/programs/<public_id>', methods=['GET'])
def retrieve_program(public_id):

    current_program = Program.query.filter_by(public_program_id=public_id).first()

    if not current_program :
        return jsonify({'status': "content not found"}),404
    
    #### ??????
    prerequisites = current_program.prerequisites
    prerequisite_list = []
    for prerequisite in prerequisites:
        prerequisite_list.append({"name": prerequisite.program_name})


    program_categories = current_program.category
    category_list = []
    for category in program_categories:
        category_list.append({"type": category.category_name})
    

    program_faqs = current_program.faqs
    faqs_list = []
    for faq in program_faqs:
        faqs_list.append({"question": faq.question,"answer": faq.answer})



    return jsonify({

                    'program_name':current_program.program_name,
                    'prerequisite' : prerequisite_list, 
                    'program_level' : current_program.difficulty_level,
                    'program_category': category_list,
                    'price': current_program.price,
                    'program_pic' : current_program.program_picture,
                    'FAQ' : faqs_list,
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
    



@app.route('/v1/programs/<public_program_id>/enrollments',methods=['POST'])
@token_required
def subscribe_to_program(current_user,public_program_id):
    enrolled = ProgramEnrollment.query.filter_by(id=public_program_id, user_id=current_user['public_id']).first()
    if enrolled:
        return jsonify({'error': 'User is already subscribed'})
    new_program_enrollment =ProgramEnrollment(program_id=public_program_id,student_id=current_user['publid_id'],is_accepted=True,join_date=date.today().strftime("%Y-%m-%d"))
    db.session.add(new_program_enrollment)
    db.session.commit()
    return jsonify({'status' : "enrolled"})
    

@app.route('/v1/programs/<public_program_id>/enrollments',methods=['DELETE'])
@token_required
def delete_program_enrollment(current_user,public_program_id):
    enrolled = ProgramEnrollment.query.filter_by(program_id=public_program_id, student_id=current_user['public_id']).first()
    if not enrolled:
        return jsonify({'error': 'User not enrolled'})

    db.session.delete(enrolled)
    db.session.commit()