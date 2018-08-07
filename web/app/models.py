from app import db

class Sensor_Data(db.Model):
    __tablename__ = 'sensor_data'
    datetime=db.Column(db.String(128), index=True, primary_key=True)
    beacon=db.Column(db.String(64), index=True)
    d_01=db.Column(db.String(64), index=True)
    m_01=db.Column(db.String(64), index=True)
    m_02=db.Column(db.String(64), index=True)
    m_03=db.Column(db.String(64), index=True)
    m_04=db.Column(db.String(64), index=True)
    minutes=db.Column(db.String(64), index=True)
    day=db.Column(db.String(64), index=True)
    apartment=db.Column(db.ForeignKey('apartment.aid'), index=True)

    def __repr__(self):
        return '<Sensor_Data {}>'.format(self.datetime)

class Apartment(db.Model):
    __tablename__ = 'apartment'
    aid=db.Column(db.String(64), primary_key=True)
    sensor_data = db.relationship('Sensor_Data', backref='sensor_data')

    def __repr__(self):
        return '<Apartment {}>'.format(self.aid)
