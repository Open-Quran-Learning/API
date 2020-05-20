from flask import request, jsonify
from ayat.models.programs import *
from ayat.models.users import *
from ayat.models.assessments import *

from ayat.authentication_routes import token_required
from ayat import app, db
from datetime import date

from flask_cors import cross_origin
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s : %(name)s : %(levelname)s : %(message)s')
file_handler = logging.FileHandler('logging.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@app.route('/v1/programs', methods=['POST'])
@cross_origin()
@token_required
def create_program(current_user):
    if not current_user['type'] == 'staff':
        logger.warning("user hasn't have permission")
        return jsonify({"status": "forbidden"}), 403

    #####################################

    data = request.get_json(force=True)
    # to create unique requirements
    requirement = data['requirement']
    min_age_requirement_check = Requirement.query.filter_by(
        min_age=requirement['min_age']).first()
    max_age_requirement_check = Requirement.query.filter_by(
        max_age=requirement['max_age']).first()
    gender_requirement_check = Requirement.query.filter_by(
        gender=requirement['gender']).first()

    if (not min_age_requirement_check) or (not max_age_requirement_check) or (not gender_requirement_check):
        new_requirement = Requirement(

            min_age=requirement['min_age'],
            max_age=requirement['max_age'],
            gender=requirement['gender'],
        )
        db.session.add(new_requirement)
        requirement_to_add = new_requirement
    else:
        requirement_to_add = min_age_requirement_check

    # creating new program
    new_program = Program(
        public_program_id=str(uuid.uuid4()),
        program_name=data['program_name'],
        difficulty_level=data['program_level'],
        price=data['price'],
        program_picture=data['program_pic'],
        is_open_to_public=data['is_open_to_public'],  # new
        program_cover=data['program_cover'],
        program_description=data['Program_description'],
        available=data['available'],
        start_date=data['start_date'],  # new
        end_date=data['end_date'],  # new
        requirement=requirement_to_add  # new
    )

    # db.session.add(new_program)

    # new

    # new_program.requirement.append(new_requirement)

    # creating new prerequisites
    # Can create program without prerequisites
    if 'prerequisite' in data:
        new_program_prerequisites = data['prerequisite']

        for prerequisite in new_program_prerequisites:
            try:
                new_program_prerequisite = Program.query.filter_by(
                    public_program_id=prerequisite['public_program_id'], ).first()
                if new_program_prerequisite:
                    new_program.prerequisites.append(new_program_prerequisite)
            except:
                return jsonify({"error": "not a valid requirement public_id "}), 404

    # creating new categories
    new_program_categories = data['program_category']

    for category in new_program_categories:

        existing_category = Category.query.filter_by(
            category_name=category['type']).first()

        if not existing_category:
            print('not exist')
            new_category = Category(category_name=category['type'])
            db.session.add(new_category)
            new_program.category.append(new_category)
        else:
            new_program.category.append(existing_category)

    # creating new faqs
    new_program_faqs = data['FAQ']

    for faq in new_program_faqs:
        new_faq = Faq(question=faq['question'], answer=faq['answer'])
        db.session.add(new_faq)
        new_program.faqs.append(new_faq)

    # creating new skill
    new_program_skills = data['skills']  # new
    for skill in new_program_skills:
        existing_skill = Skill.query.filter_by(
            skill_name=skill['name']).first()

        if not existing_skill:
            print('not exist')
            new_skill = Skill(skill_name=skill['name'])
            db.session.add(new_skill)
            new_program.skills.append(new_skill)
        else:
            new_program.skills.append(existing_skill)

    # submitting program
    db.session.add(new_program)
    db.session.commit()

    logger.info("program is created")
    return jsonify({'status': 'created',
                    'program_public_id': new_program.public_program_id,
                    }), 200


@app.route('/v1/programs/<public_id>', methods=['PUT'])
@cross_origin()
@token_required
def edit_program(current_user, public_id):
    if not current_user['type'] == 'staff':
        logger.warning("user hasn't have permission")
        return jsonify({"status": "forbidden"}), 403

    data = request.get_json(force=True)

    # checking if program exists or not
    current_program = Program.query.filter_by(
        public_program_id=str(public_id)).first()

    if not current_program:
        return jsonify({"status": "program not found"}), 404

    #######################################

    # update requirement
    requirement = data['requirement']
    min_age_requirement_check = Requirement.query.filter_by(
        min_age=requirement['min_age']).first()
    max_age_requirement_check = Requirement.query.filter_by(
        max_age=requirement['max_age']).first()
    gender_requirement_check = Requirement.query.filter_by(
        gender=requirement['gender']).first()

    if (not min_age_requirement_check) or (not max_age_requirement_check) or (not gender_requirement_check):
        new_requirement = Requirement(

            min_age=requirement['min_age'],
            max_age=requirement['max_age'],
            gender=requirement['gender'],
        )
        db.session.add(new_requirement)
        requirement_to_add = new_requirement
    else:
        requirement_to_add = min_age_requirement_check
    # updating program
    current_program.program_name = data['program_name']
    current_program.difficulty_level = data['program_level']
    current_program.price = data['price']
    current_program.program_picture = data['program_pic']
    current_program.program_cover = data['program_cover']
    current_program.program_description = data['Program_description']
    current_program.available = data['available']
    current_program.is_open_to_public = data['is_open_to_public']
    current_program.start_date = data['start_date']
    current_program.end_date = data['end_date']
    current_program.requirement = requirement_to_add
    # ######

    # updating prerequisites
    if 'prerequisite' in data:
        current_program.prerequisites = []
        prerequisites = data['prerequisite']
        for prerequisite in prerequisites:
            current_program_prerequisite = Program.query.filter_by(
                public_program_id=prerequisite['public_program_id']).first()
            if current_program_prerequisite:
                current_program.prerequisites.append(current_program_prerequisite)

    # updating categories
    current_program.category = []
    current_program_categories = data['program_category']
    for category in current_program_categories:

        existing_category = Category.query.filter_by(
            category_name=category['type']).first()

        if not existing_category:
            print('not exist')
            new_category = Category(category_name=category['type'])
            db.session.add(new_category)
            current_program.category.append(new_category)
        else:
            current_program.category.append(existing_category)
    # adding faqs
    current_program_faqs = data['FAQ']
    for faq in current_program_faqs:
        current_faq = Faq(question=faq['question'], answer=faq['answer'])
        db.session.add(current_faq)
        current_program.faqs.append(current_faq)

    # updating skills
    current_program.skills = []
    current_program_skills = data['skills']  # new
    for skill in current_program_skills:
        existing_skill = Skill.query.filter_by(
            skill_name=skill['name']).first()

        if not existing_skill:
            print('not exist')
            new_skill = Skill(skill_name=skill['name'])
            db.session.add(new_skill)
            current_program.skills.append(new_skill)
        else:
            current_program.skills.append(existing_skill)

    db.session.add(current_program)
    db.session.commit()

    logger.info('program is updated')
    return jsonify({'status': 'edited'}), 200


@app.route('/v1/programs/<public_id>', methods=['GET'])
@cross_origin()
def retrieve_program(public_id):
    current_program = Program.query.filter_by(
        public_program_id=public_id).first()

    if not current_program:
        logger.warning("content isn't found")
        return jsonify({'status': "content not found"}), 404

    # ??????
    if current_program.prerequisites is not None:
        prerequisites = current_program.prerequisites
        prerequisite_list = []
        for prerequisite in prerequisites:
            prerequisite_list.append(
                {"public_program_id": prerequisite.public_program_id})
    else:
        prerequisite_list = ['there is no prerequisites for this program']

    program_categories = current_program.category
    category_list = []
    for category in program_categories:
        category_list.append({"type": category.category_name})

    program_faqs = current_program.faqs
    faqs_list = []
    for faq in program_faqs:
        faqs_list.append({"question": faq.question, "answer": faq.answer})

    program_skills = current_program.skills
    skills_list = []
    for skill in program_skills:
        skills_list.append({"name": skill.skill_name})

    program_requirement = current_program.requirement
    requirement_object = {"requirement": {
        "min_age": program_requirement.min_age,
        "max_age": program_requirement.max_age,
        "gender": program_requirement.gender
    }
    }

    logger.info("program is successfully retrieved")
    return jsonify({

        'public_program_id': current_program.public_program_id,
        'program_name': current_program.program_name,
        'program_level': current_program.difficulty_level,
        'price': str(current_program.price),
        'program_pic': current_program.program_picture,
        'is_open_to_public': current_program.is_open_to_public,
        'program_cover': current_program.program_cover,
        'Program_description': current_program.program_description,
        'available': current_program.available,
        'start_date': current_program.start_date,
        'end_date': current_program.end_date,
        'skills': skills_list,
        'FAQ': faqs_list,
        'program_category': category_list,
        'requirement': requirement_object,
        'prerequisite': prerequisite_list,

    }), 200


@app.route('/v1/programs', methods=['GET'])
@cross_origin()
def retrieve_all_programs():
    #
    query_list = Program.query.all()

    program_list = []
    for current_program in query_list:
        # prerequisites = current_program.prerequisites
        # prerequisite_list = []
        # for prerequisite in prerequisites:
        #     prerequisite_list.append({"name": prerequisite.program_name})

        program_categories = current_program.category
        category_list = []
        for category in program_categories:
            category_list.append({"type": category.category_name})

        # program_faqs = current_program.faqs
        # faqs_list = []
        # for faq in program_faqs:
        #     faqs_list.append({"question": faq.question, "answer": faq.answer})

        # program_skills = current_program.skills
        # skills_list = []
        # for skill in program_skills:
        #     skills_list.append({"name": skill.skill_name})

        # program_requirement = current_program.requirement
        # requirement_object = {"requirement": {
        #     "min_age": program_requirement.min_age,
        #     "max_age": program_requirement.max_age,
        #     "gender": program_requirement.gender
        # }
        # }

        logger.info("program is successfully retrieved")
        program_to_append = {

            'public_program_id': current_program.public_program_id,
            'program_name': current_program.program_name,
            'program_level': current_program.difficulty_level,
            'price': str(current_program.price),
            'program_pic': current_program.program_picture,
            'is_open_to_public': current_program.is_open_to_public,
            'program_cover': current_program.program_cover,
            'Program_description': current_program.program_description,
            'available': current_program.available,
            'start_date': current_program.start_date,
            'end_date': current_program.end_date,
            # 'skills': skills_list,
            # 'FAQ': faqs_list,
            'program_category': category_list,
            # 'requirement': requirement_object,
            # 'prerequisite': prerequisite_list,

        }
        program_list.append(program_to_append)
    logger.info("all programs are successfully retrieved")
    return jsonify({'programs': program_list}), 200


@app.route('/v1/programs/<public_id>', methods=['DELETE'])
@cross_origin()
@token_required
def delete_program(current_user, public_id):
    if not current_user['type'] == 'staff':
        logger.warning("user hasn't have permission")
        return jsonify({"status": "forbidden"}), 403

    current_program = Program.query.filter_by(
        public_program_id=public_id).first()
    if current_program is None:
        return jsonify({"status": "program not found"}), 404

    program_to_delete = Program.query.filter_by(
        public_program_id=public_id).first()

    db.session.delete(program_to_delete)
    db.session.commit()
    logger.info("program is successfully deleted")
    return jsonify({'status': 'deleted'}), 200


@app.route('/v1/programs/<public_program_id>/enrollments', methods=['POST'])
@cross_origin()
@token_required
def subscribe_to_program(current_user, public_program_id):
    if current_user['type'] == 'staff':
        return jsonify({"status": "you are a staff member"}), 403

    selected_user = User.query.filter_by(
        public_id=current_user['public_id']).first()
    current_program = Program.query.filter_by(
        public_program_id=public_program_id
    ).first()

    enrolled = ProgramEnrollment.query.filter_by(
        program_id=current_program.program_id,
        student_id=selected_user.user_id
    ).first()

    if enrolled:
        logger.warning("user is already subscribed")
        return jsonify({'error': 'User is already subscribed'}), 400

    new_program_enrollment = ProgramEnrollment(
        student=selected_user,
        program=current_program,
        is_accepted=True,
        join_date=date.today().strftime("%Y-%m-%d")
    )
    db.session.add(new_program_enrollment)
    db.session.commit()
    logger.info("user successfully enrolled")
    return jsonify({'status': "enrolled"}), 200


@app.route('/v1/programs/<public_program_id>/enrollments', methods=['DELETE'])
@cross_origin()
@token_required
def delete_program_enrollment(current_user, public_program_id):
    selected_user = User.query.filter_by(
        public_id=current_user['public_id']).first()
    current_program = Program.query.filter_by(
        public_program_id=public_program_id).first()

    enrolled = ProgramEnrollment.query.filter_by(program_id=current_program.program_id,
                                                 student_id=selected_user.user_id
                                                 ).first()  # user_id ???
    if not enrolled:
        logger.warning("user failed to enroll")
        return jsonify({'error': 'user not enrolled'}), 400

    db.session.delete(enrolled)
    db.session.commit()
    logger.info("enrollment deleted")
    return jsonify({'status': 'success'}), 200
