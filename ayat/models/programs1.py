from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()


class Program(db.Model):
    __tablename__ = "program"
    program_id = db.Column(db.SMALLINT, primary_key=True)
    public_program_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    program_name = db.Column(db.VARCHAR(60), nullable=False)
    difficulty_level = db.Column(db.VARCHAR(30), nullable=False)
    price = db.Column(db.Numeric(10.2), nullable=False)
    program_picture = db.Column(db.VARCHAR(20), nullable=False)
    program_cover = db.Column(db.VARCHAR(20), nullable=False)
    program_description = db.Column(db.VARCHAR(255), nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    requirement_id = db.Column(db.SMALLINT, db.ForeignKey("requirement.requirement_id"), nullable=False)

    def __repr__(self):
        info_text = (f'program id: {self.program_id}.\n'
                     f'public program id: {self.public_program_id}.\n'
                     f'program name: {self.program_name}.\n'
                     f'difficulty level: {self.difficulty_level}.\n'
                     f'price: {self.price}.\n'
                     f'program_picture: {self.program_picture}.\n'                     f'price: {self.price}.\n'
                     f'program cover: {self.program_cover}.\n'
                     f'program description: {self.program_description}.\n'                     f'price: {self.price}.\n'
                     f'available: {self.available}.\n'
                     f'start date: {self.start_date}.\n'
                     f'end date: {self.end_date}.\n'
                     f'requirement id: {self.requirement_id}.')

        return info_text


class Skill(db.Model):
    __tablename__ = "skill"
    skill_id = db.Column(db.SMALLINT, primary_key=True)
    skill_name = db.Column(db.VARCHAR(30), nullable=False)

    def __repr__(self):
        info_text = (f'skill id: {self.skill_id}.\n'
                     f'skill name: {self.skill_name}.')

        return info_text


class Program_Skill(db.Model):
    __tablename__ = "program_skill"
    program_skill_id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey("program.program_id"), nullable=False)
    skill_id = db.Column(db.SMALLINT, db.ForeignKey("skill.skill_id"), nullable=False)

    def __repr__(self):
        info_text = (f'program skill id: {self.program_skill_id}.\n'
                     f'program id: {self.program_id}.\n'
                     f'skill id: {self.skill_id}.')

        return info_text



class Program_Faqs(db.Model):
    __tablename__ = "program_faqs"
    program_faq_id = db.Column(db.SMALLINT, primary_key=True)
    faq_id = db.Column(db.Integer, db.ForeignKey("faq.faq_id"), nullable=False)
    program_id = db.Column(db.SMALLINT, db.ForeignKey("program.program_id"), nullable=False)

    def __repr__(self):
        info_text = (f'program faq id: {self.program_faq_id}.\n'
                     f'faq id: {self.faq_id}.\n'
                     f'program id: {self.program_id}.')

        return info_text



class Faq(db.Model):
    __tablename__ = "faq"
    faq_id = db.Column(db.Integer, primary_key=True, unique=True)
    question = db.Column(db.VARCHAR(255), nullable=False)
    answer = db.Column(db.VARCHAR(255), nullable=False)

    def __repr__(self):
        info_text = (f'faq id: {self.faq_id}.\n'
                     f'question: {self.question}.\n'
                     f'answer: {self.answer}.')

        return info_text
