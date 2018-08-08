from app.models import Sensor_Data, Apartment
from app import app, db, window_start, window_end
from flask import jsonify
# import datetime
# from datetime import timedelta as TimeDelta

@app.route('/api/data', methods=['GET'])

def get_sensor_data():
    # window_start = datetime.datetime(2017, 10, 26, hour=16, minute=40, second=0, microsecond=0)
    # window_end = window_start + TimeDelta(minutes=5)

    result = {}
    for a in Apartment.query.all():
        print('for', a)
        list_of_objects = (Sensor_Data.query.filter(Sensor_Data.datetime > window_start, \
                                                  Sensor_Data.datetime < window_end, \
                                                  Sensor_Data.apartment == a.aid)).all()
        list = []
        for l in list_of_objects:
            list.append(l.__dict__)

        result[a.aid] = list
    return jsonify(result)

@app.route('/home')
def home():
    return "HELLO"