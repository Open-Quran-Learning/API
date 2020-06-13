import pytest
from ayat import app, db
from ayat.models.users import *
from ayat.models.programs import *
from werkzeug.security import generate_password_hash, check_password_hash
import jwt


@pytest.fixture
def create_app():
    app_test = app
    app_test.config['TESTING'] = True

    with app_test.app_context():
        db.create_all()
    # db.create_all()
    yield app_test
    db.drop_all()


@pytest.fixture
def client(create_app):
    return create_app.test_client()


# =========== Functions ========== #
def create_student(email, phone):
    # Hint:
    # if the student have guardian just uncomment it.
    # new_guardian = Guardian(
    #     email="DDSADAS@mail.com",
    #     phone_number="16548484"
    # )
    student = Student(
        name="khaled mohamed",
        public_id=str(uuid.uuid4()),
        email=email,
        country_name="egypt",
        phone_number=phone,
        profile_picture="default",
        birth_date="2020-01-01",
        gender=True,
        password=generate_password_hash("passworddd", method="sha256"),
        registeration_date="2010-01-01",
        type="student"
    )
    # db.session.add(new_guardian)
    # student.guardians.append(new_guardian)
    db.session.add(student)
    db.session.commit()
    return {
        "public_id": student.public_id,
        "email": student.email,
        "type": "student"
    }


def create_staff(email, phone):
    new_permission = Permission(
        permission_name="manager"
    )
    staff = Staff(
        name="mohamed mo2men",
        public_id=str(uuid.uuid4()),
        email=email,
        country_name="Egypt",
        phone_number=phone,
        profile_picture="default.png",
        birth_date="2010-03-03",
        gender=False,
        password=generate_password_hash("paworddd", method="sha256"),
        registeration_date="2010-05-05",
        type="staff",
    )
    db.session.add(new_permission)
    staff.permissions.append(new_permission)
    db.session.add(staff)
    db.session.commit()
    return {
        "public_id": staff.public_id,
        "email": staff.email,
        "type": "staff"
    }


def generate_jwt(public_id, email, type):
    token = jwt.encode({'public_id': str(public_id),
                        'email': email,
                        'type': type}, app.config['SECRET_KEY'], algorithm='HS256')

    return token


def create_program():

    requirement = {
        'min_age': 10,
        'max_age': 20,
        'gender': False
    }
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

    new_program = Program(
        public_program_id=str(uuid.uuid4()),
        program_name='TestProg',
        difficulty_level='Easy',
        price=150,
        program_picture='program_pic',
        is_open_to_public=True,
        program_cover='program_cover',
        program_description='description text prog',
        available=True,
        start_date='2020-05-15',
        end_date='2020-07-19',
        requirement=requirement_to_add
    )

    # new_program_prerequisites = {
    #     {
    #         'public_program_id': 'e885f927-2b95-4a27-b1c4-223d21f429d0'
    #     },
    #     {
    #         'public_program_id': 'e885f927-2b95-4a27-b1c4-223d21f429d0'
    #     }
    # }
    #
    # for prerequisite in new_program_prerequisites:
    #     new_program_prerequisite = Program.query.filter_by(
    #         public_program_id=prerequisite['public_program_id']
    #     ).first()
    #     if new_program_prerequisite:
    #         new_program.prerequisites.append(new_program_prerequisite)

    new_program_categories = [{'type': 'text8'}, {'type': 'text10'}]

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

    new_program_faqs = [
          {
            'question': 'Text',
            'answer': 'Text'
          },
          {
            'question': 'Text',
            'answer': 'Text'
          }
    ]

    for faq in new_program_faqs:
        new_faq = Faq(question=faq['question'], answer=faq['answer'])
        db.session.add(new_faq)
        new_program.faqs.append(new_faq)

    new_program_skills = [
        {
            'name': 'Pla'
        },
        {
            'name': 'PlaPla'
        }
    ]
    for skill in new_program_skills:
        existing_skill = Skill.query.filter_by(
            skill_name=skill['name']).first()

        if not existing_skill:
            new_skill = Skill(skill_name=skill['name'])
            db.session.add(new_skill)
            new_program.skills.append(new_skill)
        else:
            new_program.skills.append(existing_skill)

    db.session.add(new_program)
    db.session.commit()

    return {'program_name': new_program.program_name,
            'program_public_id': new_program.public_program_id,
            }
