from ayat.__init__ import db


class Appointment(db.Model):
    __tablename__ = 'appointment'
    appointment_id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer, nullable=False)
    start_hour = db.Column(db.Date, nullable=False)
    end_hour = db.Column(db.Date, nullable=False)
    event_address_id = db.Column(db.Integer, db.ForeignKey('event_address.event_address_id'), nullable=False)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.schedule_id'), nullable=False)
    db.UniqueConstraint('day', 'start_hour', 'end_hour', 'event_address_id')

    schedule = db.relationship("Schedule")
    event_address = db.relationship("EventAddress")

    def __repr__(self):
        Info_text = f'Day {self.day}\t' \
                    f'Start Hour {self.start_hour}\t' \
                    f'End Hour {self.end_hour}\n'

        return Info_text


class Schedule(db.Model):
    __tablename__ = 'schedule'
    schedule_id = db.Column(db.Integer, primary_key=True)
    recurrent = db.Column(db.Boolean, nullable=False)
    online = db.Column(db.Boolean, nullable=False)
    appointment = db.relationship("Appointment", back_populates="schedule")

    def __repr__(self):
        Info_text = f'Is recurrent?? {self.recurrent}\t' \
                    f'Is online?? {self.online}\n'

        return Info_text


class EventAddress(db.Model):
    __tablename__ = "event_address"
    event_address_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.VARCHAR(30), nullable=False)
    appointment = db.relationship("Appointment", back_populates="event_address")

    type = db.Column(db.VARCHAR(20), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'event_address',
                       'polymorphic_on': type}

    def __repr__(self):
        Info_text = f'{self.__class__.__name__} Id: {self.event_address_id}.'

        return Info_text


##############################################################################################


class PhysicalAddress(EventAddress):
    __tablename__ = "physical_address"
    event_address_id = db.Column(db.Integer, db.ForeignKey("event_address.event_address_id"), primary_key=True)
    country_name = db.Column(db.VARCHAR(30), nullable=False)
    address_details = db.Column(db.VARCHAR(150), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'physical_address'}

    def __repr__(self):
        Info_text = f'{super().__repr__()}\t' \
                    f'Country Name: {self.country_name}\t' \
                    f'Address Details: {self.address_details}\n'

        return Info_text


##################################################################################################


class WebAddress(EventAddress):
    __tablename__ = "web_address"
    event_address_id = db.Column(db.Integer, db.ForeignKey("event_address.event_address_id"), primary_key=True)
    url = db.Column(db.String, nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'web_address'}

    def __repr__(self):
        Info_text = f'{super().__repr__()}\t' \
                    f'URL: {self.url}\n'

        return Info_text
