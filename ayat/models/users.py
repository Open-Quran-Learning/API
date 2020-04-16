import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(40), nullable=False)
    public_id = db.Column(UUID(as_uuid=True),default=uuid.uuid4, unique=True,nullable=False)
    email = db.Column(db.VARCHAR(120), unique=True, nullable=False)
    country_name = db.Column(db.VARCHAR(30), nullable=False)
    phone_number = db.Column(db.VARCHAR(15), unique=True, nullable=False)
    profile_picture = db.Column(db.VARCHAR(20)) ## FrontEnd will set a default Profile Picture
    birth_date = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    password = db.Column(db.VARCHAR(30),nullable=False)
    registeration_date = db.Column(db.Date,nullable=False)
    is_activated = db.Column(db.Boolean)
    
    type = db.Column(db.String(30), nullable=False)

    __mapper_args__ = { 'polymorphic_identity': 'user',
                        'polymorphic_on': type
                      }

    
    def __repr__(self):
    	Info_text = (f'{self.__class__.__name__} Id: {self.user_id}.\n'
    		f'{self.__class__.__name__} Name: {self.name}.\n'
    		f'Public Id: {self.public_id}.\n'
    		f'E-mail: {self.email}.\n'
    		f'Country: {self.country_name}.\n'
    		f'Phone Number: {self.phone_number}.\n'
    		f'Profile Picture: {self.profile_picture}.\n'
    		f'Birth Date: {self.birth_date}.\n'
    		f'Gender: {self.gender}.\n'
    		f'Password: {self.password}.\n'
    		f'Registeration Date: {self.registeration_date}.\n'
    		f'Activation: {self.is_activated}.'
    		)

    	return Info_text

#############################################################################################################

Student_Guardian = db.Table('student_guardian', db.Model.metadata,
    db.Column('student_guardian_id', db.Integer, primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.student_id'), nullable=False),
    db.Column('guardian_id', db.Integer, db.ForeignKey('guardian.guardian_id'), nullable=False),  

    UniqueConstraint('student_id','guardian_id'))


class Student(User):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    guardians = db.relationship('Guardian', secondary=Student_Guardian, backref=db.backref('students',lazy='dynamic'))

    __mapper_args__ = {'polymorphic_identity':'student'}


class Guardian(db.Model):
    __tablename__ = "guardian"
    guardian_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(30), unique=True, nullable=False)
    phone_number = db.Column(db.VARCHAR(15), unique=True, nullable=False)

    def __repr__(self):
        Info_text = (f'Guardian Id: {self.guardian_id}.\n'
            f'E-mail: {self.email}.\n'
            f'Phone Number: {self.phone_number}.')

        return Info_text

#############################################################################################################

Staff_Permission = db.Table('staff_permission', db.Model.metadata,
    db.Column('staff_permission_id', db.Integer, primary_key=True),
    db.Column('permission_id', db.SmallInteger, db.ForeignKey('permission.permission_id'), nullable=False),
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.staff_id'), nullable= False),  

    UniqueConstraint('staff_id','permission_id'))


class Staff(User):
    __tablename__ = "staff"
    staff_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    permissions = db.relationship('Permission', secondary=Staff_Permission, backref=db.backref('staff',lazy='dynamic'))

    __mapper_args__ = {'polymorphic_identity':'staff'}


class Permission(db.Model):
    __tablename__ = "permission"
    permission_id = db.Column(db.Integer, primary_key=True)
    permission_name = db.Column(db.VARCHAR(50) , nullable=False)

    def __repr__(self):
        Info_text = (f'Permission Id: {self.permission_id}.\n'
            f'Permission Name: {self.permission_name}.')

        return Info_text

#############################################################################################################

