from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ayat import db


program_skill = db.Table('program_skill', db.Model.metadata,
                         db.Column('program_skill_id', db.Integer, primary_key=True),
                         db.Column('program_id', db.Integer, db.ForeignKey('program.program_id')),
                         db.Column('skill_id', db.SMALLINT, db.ForeignKey('skill.skill_id')))

program_faqs = db.Table('program_faqs',  db.Model.metadata,
                        db.Column('program_faq_id', db.SMALLINT, primary_key=True),
                        db.Column('faq_id', db.Integer, db.ForeignKey('faq.faq_id')),
                        db.Column('program_id', db.Integer, db.ForeignKey('program.program_id')))

program_category = db.Table('program_category',  db.Model.metadata,
                            db.Column('program_category_id', db.SMALLINT, primary_key=True),
                            db.Column('category_id', db.Integer, db.ForeignKey('category.category_id')),
                            db.Column('program_id', db.Integer, db.ForeignKey('program.program_id')))

program_prerequisite = db.Table('program_prerequisite',  db.Model.metadata,
                        db.Column('prerequisite_id', db.SMALLINT, primary_key=True),
                        db.Column('dependency_id', db.Integer, db.ForeignKey('program.program_id')),
                        db.Column('program_id', db.Integer, db.ForeignKey('program.program_id')))


############################################################################
class Program(db.Model):
    __tablename__ = "program"
    program_id = db.Column(db.SMALLINT, primary_key=True)
    public_program_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    program_name = db.Column(db.VARCHAR(60), nullable=False)
    difficulty_level = db.Column(db.VARCHAR(30), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    program_picture = db.Column(db.VARCHAR(20), nullable=False)
    is_open_to_public = db.Column(db.Boolean, nullable=False)
    program_cover = db.Column(db.VARCHAR(20), nullable=False)
    program_description = db.Column(db.VARCHAR(255), nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    requirement_id = db.Column(db.SMALLINT, db.ForeignKey("requirement.requirement_id"), nullable=False)
    skills = db.relationship('Skill', secondary=program_skill, backref=db.backref('program', lazy='dynamic'))
    faqs = db.relationship('Faq', secondary=program_faqs, backref=db.backref('program', lazy='dynamic'))
    category = db.relationship('Category', secondary=program_category, backref=db.backref('program', lazy='dynamic'))
    courses = db.relationship('Course', backref=db.backref('program'))
    requirement = db.relationship("Requirement", backref=db.backref('program'))
    program_enrollment = db.relationship("ProgramEnrollment", back_populates="program")
    prerequisites = db.relationship(
        'Program',
        secondary=program_prerequisite,
        primaryjoin=program_id == program_prerequisite.c.dependency_id,
        secondaryjoin=program_id == program_prerequisite.c.program_id,
        backref=db.backref('program_prerequisite')
    )

    def __repr__(self):
        info_text = (f'program id: {self.program_id}.\t'
                     f'public program id: {self.public_program_id}.\t'
                     f'program name: {self.program_name}.\t'
                     f'difficulty level: {self.difficulty_level}.\t'
                     f'price: {self.price}.\t'
                     f'program_picture: {self.program_picture}.\t'
                     f'program cover: {self.program_cover}.\t'
                     f'program description: {self.program_description}.\t'
                     f'price: {self.price}.\t'
                     f'available: {self.available}.\t'
                     f'start date: {self.start_date}.\t'
                     f'end date: {self.end_date}.\t'
                     f'requirement id: {self.requirement_id}.\n')

        return info_text


class Skill(db.Model):
    __tablename__ = "skill"
    skill_id = db.Column(db.SMALLINT, primary_key=True)
    skill_name = db.Column(db.VARCHAR(30), nullable=False)

    def __repr__(self):
        info_text = (f'skill id: {self.skill_id}.\t'
                     f'skill name: {self.skill_name}.\n')

        return info_text


class Faq(db.Model):
    __tablename__ = "faq"
    faq_id = db.Column(db.SMALLINT, primary_key=True, unique=True)
    question = db.Column(db.VARCHAR(255), nullable=False)
    answer = db.Column(db.VARCHAR(255), nullable=False)

    def __repr__(self):
        info_text = (f'faq id: {self.faq_id}.\t'
                     f'question: {self.question}.\t'
                     f'answer: {self.answer}.\n')

        return info_text


class Course(db.Model):
    __tablename__ = "course"
    course_id = db.Column(db.SMALLINT, primary_key=True)
    public_course_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    program_id = db.Column(db.SMALLINT, db.ForeignKey("program.program_id"), nullable=False)
    course_name = db.Column(db.VARCHAR(60), nullable=False)
    course_description = db.Column(db.VARCHAR(255))  # may be deleted
    course_order = db.Column(db.SMALLINT, unique=True, nullable=False)
    lessons = db.relationship('Lesson', backref=db.backref('course'))

    def __repr__(self):
        info_text = (f'course id: {self.course_id}.\t'
                     f'public course id: {self.public_course_id}.\t'
                     f'program id: {self.program_id}.\t'
                     f'course name: {self.course_name}.\t'
                     f'course description: {self.course_description}.\t'
                     f'course order: {self.course_order}.\n')
        return info_text


class Lesson(db.Model):
    __tablename__ = "lesson"
    lesson_id = db.Column(db.SMALLINT, primary_key=True)
    public_lesson_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    course_id = db.Column(db.SMALLINT, db.ForeignKey("course.course_id"), nullable=False)
    lesson_name = db.Column(db.VARCHAR(60), nullable=False)
    lesson_description = db.Column(db.VARCHAR(255))  # may be deleted
    content = db.Column(db.JSON, nullable=False)
    lesson_order = db.Column(db.SMALLINT, unique=True, nullable=False)
    unlocked = db.Column(db.BOOLEAN, default=True)

    def __repr__(self):
        info_text = (f'lesson id: {self.lesson_id}.\t'
                     # f'public lesson id: {self.public_lesson_id}.\t'
                     f'course id: {self.course_id}.\t'
                     f'lesson name: {self.lesson_name}.\t'
                     f'lesson_description: {self.lesson_description}.\t'
                     f'content: {self.content}.\t'
                     f'lesson order: {self.lesson_order}.\t'
                     # f'program description: {self.program_description}.\t'
                     f'unlocked: {self.unlocked}.\n')
        return info_text


class Requirement(db.Model):
    __tablename__ = "requirement"
    requirement_id = db.Column(db.SMALLINT, primary_key=True)
    min_age = db.Column(db.SMALLINT, nullable=False)
    max_age = db.Column(db.SMALLINT, nullable=False)
    gender = db.Column(db.VARCHAR(60), nullable=False)

    def __repr__(self):
        info_text = (f'requirement id: {self.requirement_id}.\t'
                     f'min age: {self.min_age}.\t'
                     f'max age: {self.max_age}.\t'
                     f'gender: {self.gender}.\n')
        return info_text


class Category(db.Model):
    __tablename__ = "category"
    category_id = db.Column(db.SMALLINT, primary_key=True)
    category_name = db.Column(db.VARCHAR(30), unique=True)

    def __repr__(self):
        info_text = (f'category id: {self.category_id}.\t'
                     f'category name: {self.category_name}.\n')
        return info_text
