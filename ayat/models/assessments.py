
from ayat.__init__ import db
from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSON
import uuid
from users import *


class AssessmentResults(db.Model):
    __tablename__ = 'assessment_results'
    enrollment_id = db.Column(db.Integer, primary_key=True)
    public_assessment_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.exam_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=False)
    grade = db.Column(db.SMALLINT, nullable=False)

    db.UniqueConstraint(exam_id, student_id, staff_id)
    student = db.relationship("Student")
    exam = db.relationship("Exam")
    staff = db.relationship("Staff")

    def __repr__(self):
        Info_text = f'Grade: {self.grade}\n'

        return Info_text


class Exam(db.Model):
    __tablename__ = 'exam'
    exam_id = db.Column(db.Integer, primary_key=True)
    public_exam_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    qusetion = db.Column(ARRAY(JSON))
    assessment_results = db.relationship("AssessmentResults", back_populates="exam")

    type = db.Column(db.VARCHAR(15))
    __mapper_args__ = {
        'polymorphic_identity': 'exam',
        'polymorphic_on': type
    }

    def __repr__(self):
        Info_text = f'Qusetion: {self.qusetion}\t'\
                     f'Assessment Results: {self.assessment_results}\n'

        return Info_text


class ProgramExam(Exam):
    __tablename__ = 'program_exam'
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.exam_id'), primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'), unique=True)
    program = db.relationship('Program', backref='program_exam', uselist=False, lazy=True)
    __mapper_args__ = {
        'polymorphic_identity': 'program_exam'
    }

    def __repr__(self):
        self.Super().__repr__()


class CourseExam(Exam):
    __tablename__ = 'course_exam'
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.exam_id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), unique=True)
    course = db.relationship('Course', backref='course_exam', uselist=False, lazy=True)
    __mapper_args__ = {
        'polymorphic_identity': 'course_exam'
    }

    def __repr__(self):
        self.Super().__repr__()


class LessonExam(Exam):
    __tablename__ = 'lesson_exam'
    course_exam_id = db.Column(db.Integer, db.ForeignKey('exam.exam_id'), primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.lesson_id'))
    lesson = db.relationship('Lesson', backref='lesson_exam', uselist=False, lazy=True)
    __mapper_args__ = {
        'polymorphic_identity': 'lesson_exam'
    }

    def __repr__(self):
        self.Super().__repr__()


class ProgramEnrollment(db.Model):

    __tablename= 'program_enrollment'
    program_enrollment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'), nullable=False)
    is_accepted = db.Column(db.Boolean, nullable=False)
    join_date = db.Column(db.Date, nullable=False)

    db.UniqueConstraint(student_id, program_id)
    student = db.relationship("Student")
    program = db.relationship("Program")

    def __repr__(self):
        Info_text = f'Is Accepted?: {self.is_accepted}\t'\
                     f'Join Date: {self.join_date}\n'

        return Info_text
