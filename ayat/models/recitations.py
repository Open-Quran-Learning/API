from ayat import db

from sqlalchemy.dialects.postgresql import UUID
import uuid

#############################################################################################################

### Association Class For the 3 related Tables:

class RecitationEnrollment(db.Model):
    __tablename__ = 'recitation_enrollment'

    recitation_enrollment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable= False)
    recitation_id = db.Column(db.Integer, db.ForeignKey('recitation.recitation_id'), nullable= False)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.assignment_id'), nullable= False)
    join_date = db.Column(db.TIMESTAMP, nullable= False)
    is_accepted = db.Column(db.Boolean, nullable= False)

    db.UniqueConstraint(student_id, recitation_id, assignment_id)

    student = db.relationship('Student', back_populates='recitation_enrollment')
    recitation = db.relationship('Recitation', back_populates='recitation_enrollment')
    assignment = db.relationship('Assignment', back_populates='recitation_enrollment')

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

class Recitation(db.Model):
    __tablename__ = "recitation"
    recitation_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric, nullable=False)
    number_of_seats = db.Column(db.SmallInteger , nullable=False)

    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))

    recitation_enrollment = db.relationship('RecitationEnrollment', back_populates='recitation')

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

    recitation_enrollment = db.relationship("RecitationEnrollment", back_populates='assignment')

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
            f'Assignment Date: {self.assignment_date}.\n'
            )

        return Info_text


class RecitationReport(db.Model):
    __tablename__ = 'recitation_report'
    recitation_report_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    recitation_id = db.Column(db.Integer, nullable=False)
    assignment_id = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.SMALLINT, nullable=False)
    is_absent = db.Column(db.Boolean, nullable=False)

###############################################################################################################################################################################################################################################################
### TESTING CODE IN PYTHON SHELL
### ---------------------------- ###


## Creating 3 new Students and adding them to the database ##

#>>> student1 = Student(name='Mohamed',email='moh@yahoo.com',country_name='Egypt',phone_number='010',gender=True,password='moh123',is_activated=True,type='student')
#>>> student2 = Student(name='Ahmed',email='ahm@yahoo.com',country_name='Egypt',phone_number='011',gender=True,password='ahm123',is_activated=True,type='student')
#>>> student3 = Student(name='Ayman',email='aym@yahoo.com',country_name='Egypt',phone_number='012',gender=True,password='aym123',is_activated=True,type='student')
#>>> db.session.add(student1)
#>>> db.session.add(student2)
#>>> db.session.add(student3)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Creating 3 new Recitations and adding them to the database ##

#>>> recitation1 = Recitation(price=100,number_of_seats=20)
#>>> recitation2 = Recitation(price=200,number_of_seats=30)
#>>> recitation3 = Recitation(price=300,number_of_seats=50)
#>>> db.session.add(recitation1)
#>>> db.session.add(recitation2)
#>>> db.session.add(recitation3)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Creating 3 new assignments and adding them to the database ##

#>>> assignment1 = Assignment(revision_from_surah=1,revision_from_ayah=1,revision_to_surah=1,revision_to_ayah=10,new_from_surah=1,new_from_ayah=11,new_to_surah=1,new_to_ayah=20)
#>>> assignment2 = Assignment(revision_from_surah=100,revision_from_ayah=1,revision_to_surah=102,revision_to_ayah=20,new_from_surah=103,new_from_ayah=1,new_to_surah=105,new_to_ayah=20)
#>>> assignment3 = Assignment(revision_from_surah=2,revision_from_ayah=1,revision_to_surah=2,revision_to_ayah=30,new_from_surah=2,new_from_ayah=31,new_to_surah=2,new_to_ayah=60)
#>>> db.session.add(assignment1)
#>>> db.session.add(assignment2)
#>>> db.session.add(assignment3)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Associations of students, recitations and assignments and adding them to the association table (RecitationEnrollment) in the database:

#>>> assoc1 = RecitationEnrollment(student=student1,recitation=recitation1,assignment=assignment1,is_accepted=True)
#>>> assoc2 = RecitationEnrollment(student=student2,recitation=recitation2,assignment=assignment2,is_accepted=True)
#>>> assoc3 = RecitationEnrollment(student=student3,recitation=recitation3,assignment=assignment3,is_accepted=True)
#>>> db.session.add(assoc1)
#>>> db.session.add(assoc2)
#>>> db.session.add(assoc3)
#>>> db.session.commit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Getting the recitaion enrollment Info for any student:

#>>> student1.recitation_enrollment
#OUTPUT: [Recitation Enrollment Id: 1.   Student Id: 1.  Recitation Id: 1.       Assignment Id: 1.       Acceptance: True.]


## Getting recitaion enrollment Info for any recitation:

#>>> recitation1.recitation_enrollment
#OUTPUT: [Recitation Enrollment Id: 1.   Student Id: 1.  Recitation Id: 1.       Assignment Id: 1.       Acceptance: True.]


## Getting recitaion enrollment Info for any assignment:

#>>> assignment2.recitation_enrollment
#OUTPUT: [Recitation Enrollment Id: 2.   Student Id: 2.  Recitation Id: 2.       Assignment Id: 2.       Acceptance: True.]


######################  NOTE: This assures that the relationship is built correctly and works fine! ######################

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

## Assigning Recitaions to Staff (This is a One-To-Many Relationship; meaning that a specific staff can have at least one recitation, but a specific recitation must have only one staff) ##

#>>> staff1.recitations.append(recitation1)
#>>> staff1.recitations.append(recitation2)
#>>> staff2.recitations.append(recitation3)
#>>> db.session.commit()

# Notice the OUTPUT if we try to get the recitations that staff1 has:

#>>> staff1.recitations
# OUTPUT: [Recitation Id: 1.      Price: 100.     Number Of Seats: 20.
#          Recitation Id: 2.     Price: 200.     Number Of Seats: 30.]

# --> This means that a staff can have one or more recitations <-- #

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Getting the Staff Info of any Recitation:

#>>> recitation1.staff
#OUTPUT: Staff Id: 4.    Staff Name: Hazem.      E-mail: staff1@yahoo.com.       Country: Egypt.       Phone Number: 0111242.     Profile Picture: None.     Gender: True.       Password: staff111.     Activation: True.       Type: staff.

# Assigning recitation1 to another Staff (ex: staff2) and getting that Recitation's Staff Info again:

#>>> staff2.recitations.append(recitation1)
#>>> recitation1.staff
#OUTPUT: Staff Id: 5.    Staff Name: haitham.    E-mail: staff2@yahoo.com.       Country: Egypt.       Phone Number: 0123412.     Profile Picture: None.     Gender: True.       Password: staff222.     Activation: True.       Type: staff.

## Notice that recitation1 has a different staff but still just one staff. ##
# --> This means that a recitation can have only one staff <-- #

###############################################################################################################################################################################################################################################################

### This File is completely tested as well as all its related tables in the database and it works fine!.... ###