from app import db

from app.models import Sensor_Data
from app.models import Apartment

Sensor_Data.query.filter_by(apartment='MP0055').delete()
Apartment.query.filter_by(aid='MP0055').delete()
db.session.commit()