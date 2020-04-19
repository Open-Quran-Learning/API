import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@127.0.0.1:5432/test'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

###   User Class will be replaced with the Student Class from users.py file without forgetting to put the following line 
###   recitation_enrollment = db.relationship("Recitation_Enrollment", back_populates="student") in Student Class to build
###   the relationship with Student Class and Recitation_Enrollment Class in this file.

#############################################################################################################

### Association Class For the 3 Tables:

class Recitation_Enrollment(db.Model):
    __tablename__ = 'recitation_enrollment'

    recitation_enrollment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable= False)
    recitation_id = db.Column(db.Integer, db.ForeignKey('recitation.recitation_id'), nullable= False)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.assignment_id'), nullable= False)
    join_date = db.Column(db.TIMESTAMP, nullable= False)
    is_accepted = db.Column(db.Boolean, nullable= False)

    UniqueConstraint(student_id, recitation_id, assignment_id)

    student = db.relationship("Student")  ## Don't forget to import Student Class from users.py
    recitation = db.relationship("Recitation")
    assignment = db.relationship("Assignment")

    def __repr__(self):
        Info_text = (f'Recitation Enrollment Id: {self.recitation_enrollment_id}.\t'
            f'Student Id: {self.student_id}.\t'
            f'Recitation Id: {self.recitation_id}.\t'
            f'Assignment Id: {self.assignment_id}.\t'
            f'Join Date: {self.join_date}.\t'
            f'Acceptance: {self.is_accepted}.\n'
            )

        return Info_text 

#############################################################################################################

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
    	Info_text = (f'{self.__class__.__name__} Id: {self.user_id}.\t'
    		f'{self.__class__.__name__} Name: {self.name}.\t'
    		f'Public Id: {self.public_id}.\t'
    		f'E-mail: {self.email}.\t'
    		f'Country: {self.country_name}.\t'
    		f'Phone Number: {self.phone_number}.\t'
    		f'Profile Picture: {self.profile_picture}.\t'
    		f'Birth Date: {self.birth_date}.\t'
    		f'Gender: {self.gender}.\t'
    		f'Password: {self.password}.\t'
    		f'Registeration Date: {self.registeration_date}.\t'
    		f'Activation: {self.is_activated}.\t'
    		f'Type: {self.type}.\n')

    	return Info_text


class Student(User):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    recitation_enrollment = db.relationship("Recitation_Enrollment", back_populates="student")

    __mapper_args__ = {'polymorphic_identity':'student'}


class Recitation(db.Model):
    __tablename__ = "recitation"
    recitation_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric, nullable=False)
    number_of_seats = db.Column(db.SmallInteger , nullable=False)

    recitation_enrollment = db.relationship("Recitation_Enrollment", back_populates="recitation")

    def __repr__(self):
        Info_text = (f'Recitation Id: {self.recitation_id}.\t'
            f'Price: {self.price}.\t'
            f'Number Of Seats: {self.number_of_seats}.\n')

        return Info_text 


class Assignment(db.Model):
    __tablename__ = "assignment"
    assignment_id = db.Column(db.Integer, primary_key=True)
    revision_from_surah = db.Column(db.SmallInteger, nullable=False)
    revision_from_ayah = db.Column(db.SmallInteger, nullable=False)
    revision_to_surah = db.Column(db.SmallInteger, nullable=False)
    revision_to_ayah = db.Column(db.SmallInteger, nullable=False)
    new_from_surah = db.Column(db.SmallInteger, nullable=False)
    new_from_ayah = db.Column(db.SmallInteger, nullable=False)
    new_to_surah = db.Column(db.SmallInteger, nullable=False)
    new_to_ayah = db.Column(db.SmallInteger, nullable=False)
    assignment_date = db.Column(db.Date, nullable=False)

    recitation_enrollment = db.relationship("Recitation_Enrollment", back_populates="assignment")

    def __repr__(self):
        Info_text = (f'Assignment Id: {self.assignment_id}.\t'
            f'Revision From Surah: {self.revision_from_surah}.\t'
            f'Revision From Ayah: {self.revision_from_ayah}.\t'
            f'Revision To Surah: {self.revision_to_surah}.\t'
            f'Revision To Ayah: {self.revision_to_ayah}.\t'
            f'New From Surah: {self.new_from_surah}.\t'
            f'New From Ayah: {self.new_from_ayah}.\t'
            f'New To Surah: {self.new_to_surah}.\t'
            f'New To Ayah: {self.new_to_ayah}.\t'
            f'Assignment Date: {self.assignment_date}.\n')

        return Info_text
    
#############################################################################################################


## TESTING CODE IN PYTHON SHELL

#>>> student1 = Student(name='Mohamed',email='moh@yahoo.com',country_name='Egypt',phone_number='010',gender=True,password='moh123',is_activated=True,type='student')
#>>> student2 = Student(name='Ahmed',email='ahm@yahoo.com',country_name='Egypt',phone_number='011',gender=True,password='ahm123',is_activated=True,type='student')
#>>> student3 = Student(name='Ayman',email='aym@yahoo.com',country_name='Egypt',phone_number='012',gender=True,password='aym123',is_activated=True,type='student')
#>>> db.session.add(student1)
#>>> db.session.add(student2)
#>>> db.session.add(student3)
#>>> db.session.commit()
#>>> recitation1 = Recitation(price=100,number_of_seats=20)
#>>> recitation2 = Recitation(price=200,number_of_seats=30)
#>>> recitation3 = Recitation(price=300,number_of_seats=50)
#>>> db.session.add(recitation1)
#>>> db.session.add(recitation2)
#>>> db.session.add(recitation3)
#>>> db.session.commit()
#>>> assignment1 = Assignment(revision_from_surah=1,revision_from_ayah=1,revision_to_surah=1,revision_to_ayah=10,new_from_ayah=1,new_from_ayah=11,new_to_surah=1,new_to_ayah=20,assignment_date=12)
#>>> assignment1 = Assignment(revision_from_surah=1,revision_from_ayah=1,revision_to_surah=1,revision_to_ayah=10,new_from_surah=1,new_from_ayah=11,new_to_surah=1,new_to_ayah=20,assignment_date=12)
#>>> assignment2 = Assignment(revision_from_surah=100,revision_from_ayah=1,revision_to_surah=102,revision_to_ayah=20,new_from_surah=103,new_from_ayah=1,new_to_surah=105,new_to_ayah=20,assignment_date=10)
#>>> assignment3 = Assignment(revision_from_surah=2,revision_from_ayah=1,revision_to_surah=2,revision_to_ayah=30,new_from_surah=2,new_from_ayah=31,new_to_surah=2,new_to_ayah=60,assignment_date=8)
#>>> db.session.add(assignment1)
#>>> db.session.add(assignment2)
#>>> db.session.add(assignment3)
#>>> db.session.commit()
#>>> assoc1 = Recitation_Enrollment(student=student1,recitation=recitation1,assignment=assignment1)
#>>> assoc2 = Recitation_Enrollment(student=student2,recitation=recitation2,assignment=assignment2)
#>>> assoc3 = Recitation_Enrollment(student=student3,recitation=recitation3,assignment=assignment3)
#>>> db.session.add(assoc1)
#>>> db.session.add(assoc2)
#>>> db.session.add(assoc3)
#>>> db.session.commit()
#>>> assoc4 = Recitation_Enrollment(student=student2,recitation=recitation2,assignment=assignment1)
#>>> db.session.add(assoc4)
#>>> db.session.commit()