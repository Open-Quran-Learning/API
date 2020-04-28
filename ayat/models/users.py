from ayat import db

from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid

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

#############################################################################################################

## Association Table between student table and guardian table:

Student_Guardian = db.Table('student_guardian', db.Model.metadata,
    db.Column('student_guardian_id', db.Integer, primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.student_id'), nullable=False),
    db.Column('guardian_id', db.Integer, db.ForeignKey('guardian.guardian_id'), nullable=False),  

    UniqueConstraint('student_id','guardian_id'))


class Student(User):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    guardians = db.relationship('Guardian', secondary=Student_Guardian, backref=db.backref('student',lazy='dynamic'))

    recitation_enrollment = db.relationship("RecitationEnrollment", back_populates='student')
    # assessment_results = db.relationship("AssessmentResults", back_populates="student")
    program_enrollment = db.relationship("ProgramEnrollment", back_populates="student")

    __mapper_args__ = {'polymorphic_identity':'student'}


class Guardian(db.Model):
    __tablename__ = "guardian"
    guardian_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(30), unique=True, nullable=False)
    phone_number = db.Column(db.VARCHAR(15), unique=True, nullable=False)

    def __repr__(self):
        Info_text = (f'Guardian Id: {self.guardian_id}.\t'
            f'E-mail: {self.email}.\t'
            f'Phone Number: {self.phone_number}.\n')

        return Info_text

#############################################################################################################

## Association Table between staff table and permission table:

Staff_Permission = db.Table('staff_permission', db.Model.metadata,
    db.Column('staff_permission_id', db.Integer, primary_key=True),
    db.Column('permission_id', db.SmallInteger, db.ForeignKey('permission.permission_id'), nullable=False),
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.staff_id'), nullable= False),  

    UniqueConstraint('staff_id','permission_id'))


class Staff(User):
    __tablename__ = "staff"
    staff_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    assessment_results = db.relationship("AssessmentResults", back_populates="staff")
    permissions = db.relationship('Permission', secondary=Staff_Permission, backref=db.backref('staff',lazy='dynamic'))

    recitations = db.relationship('Recitation', backref=db.backref('staff'))

    __mapper_args__ = {'polymorphic_identity':'staff'}


class Permission(db.Model):
    __tablename__ = "permission"
    permission_id = db.Column(db.Integer, primary_key=True)
    permission_name = db.Column(db.VARCHAR(50) , nullable=False)

    def __repr__(self):
        Info_text = (f'Permission Id: {self.permission_id}.\t'
            f'Permission Name: {self.permission_name}.\n')

        return Info_text


###############################################################################################################################################################################################################################################################
### TESTING CODE IN PYTHON SHELL
### ---------------------------- ###


## Creating 3 new Students and adding them to the database ##

#>>> student1 = Student(name='Mohamed',email='moh@yahoo.com',country_name='Egypt',phone_number='0100',gender=True,password='moh123',is_activated=True,type='student')
#>>> student2 = Student(name='Ahmed',email='ahm@yahoo.com',country_name='Egypt',phone_number='0111',gender=True,password='ahm123',is_activated=True,type='student')
#>>> student3 = Student(name='Sara',email='sara@yahoo.com',country_name='Egypt',phone_number='0122',gender=False,password='sara123',is_activated=True,type='student')
#>>> db.session.add(student1)
#>>> db.session.add(student2)
#>>> db.session.add(student3)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Creating 2 new Guardians and adding them to the database ##

#>>> guardian1 = Guardian(email='guardian1@yahoo.com',phone_number='01010')
#>>> guardian2 = Guardian(email='guardian2@yahoo.com',phone_number='01111')
#>>> db.session.add(guardian1)
#>>> db.session.add(guardian2)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Assigning guardians to the existing students ##

#>>> student1.guardians.append(guardian1)
#>>> student2.guardians.append(guardian2)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Assigning a Student to a Guardian (To Check if the relationship is working as it should be bidirectional!) ##

#>>> guardian2.students.append(student3)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Getting the students Info that guardian1 has:

#>>> guardian1.students.all()
#OUTPUT: [Student Id: 1.  Student Name: Mohamed.  E-mail: moh@yahoo.com.  Country: Egypt. Phone Number: 0100.     Profile Picture: None.  Gender: True.   Password: moh123.       Activation: True.       Type: student.]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Getting the guardians Info that student2 has:

#>>> student2.guardians
#OUTPUT: [Guardian Id: 2.        E-mail: guardian2@yahoo.com.    Phone Number: 01111.]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
###############################################################################################################################################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Creating 2 new Staff and adding them to the database ##

#>>> staff1 = Staff(name='Hazem',email='staff1@yahoo.com',country_name='Egypt',phone_number='0111242',gender=True,password='staff111',is_activated=True,type='staff')
#>>> staff2 = Staff(name='haitham',email='staff2@yahoo.com',country_name='Egypt',phone_number='0123412',gender=True,password='staff222',is_activated=True,type='staff')
#>>> db.session.add(staff1)
#>>> db.session.add(staff2)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## CreaCreating 2 new Permissions and adding them to the database ##

#>>> permission1 = Permission(permission_name='Admin')
#>>> permission2 = Permission(permission_name='Supervisor')
#>>> db.session.add(permission1)
#>>> db.session.add(permission2)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Assigning a Permission to an existing Staff ##

#>>> staff1.permissions.append(permission1)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Assigning a Staff to an existing Permission (To Check if the relationship is working as it should be bidirectional!) ##

#>>> permission2.staff.append(staff2)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Getting the permissions Info that staff1 has:

#>>> staff1.permissions.all()
#OUTPUT: [Permission Id: 1.      Permission Name: Admin.]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Getting the Staff Info that have a specific permission:

#>>> permission2.staff.all()
#OUTPUT:[Staff Id: 5.   Staff Name: haitham.    E-mail: staff2@yahoo.com.       Country: Egypt. Phone Number: 0123412.  Profile Picture: None.  Gender: True.   Password: staff222.     Activation: True.       Type: staff.]


###############################################################################################################################################################################################################################################################

### This File is completely tested as well as all its related tables in the database and it works fine!.... ###