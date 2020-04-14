from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event_Address(db.Model):
	__tablename__ = "event_address"
	event_address_id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.VARCHAR(30), nullable=False)
	__mapper_args__ = { 'polymorphic_identity': 'event_address',
	'polymorphic_on': type}

	def __repr__(self):
		Info_text = (f'{self.__class__.__name__} Id: {self.event_address_id}.')

		return Info_text

#############################################################################################################

class Physical_Address(Event_Address):
	__tablename__ = "physical_address"
	event_address_id = db.Column(db.Integer, db.ForeignKey("event_address.event_address_id"), primary_key=True)
	country_name = db.Column(db.VARCHAR(30), nullable=False)
	address_details = db.Column(db.VARCHAR(150),nullable=False)

	def __repr__(self):
		Info_text = (f'{super().__repr__()}.\n'
			f'Country Name: {self.country_name}.\n'
			f'Address Details: {self.address_details}.')

		return Info_text
#############################################################################################################

class Web_Address(Event_Address):
	__tablename__ = "web_address"
	event_address_id = db.Column(db.Integer, db.ForeignKey("event_address.event_address_id"), primary_key=True)
	url = db.Column(db.String, nullable=False)

	def __repr__(self):
		Info_text = (f'{super().__repr__()}.\n'
			f'URL: {self.url}.')

		return Info_text