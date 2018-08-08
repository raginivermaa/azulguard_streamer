from app.models import Sensor_Data, Apartment
from app import app, db, window_start, window_end
from datetime import timedelta as TimeDelta
from flask import jsonify

@app.route('/api/data', methods=['GET'])

def get_sensor_data():
    global window_start
    print(window_start)
    global window_end
    print(window_end)

    result = {}
    for a in Apartment.query.all():
        print('for', a)
        data = (Sensor_Data.query.filter(Sensor_Data.datetime > window_start, \
                                                  Sensor_Data.datetime < window_end, \
                                                  Sensor_Data.apartment == a.aid)).all()
        if len(data) > 0:
            data_object = data[0].__dict__
            data_object.pop('_sa_instance_state', None)
            result[a.aid] = data_object
    window_start = window_end
    window_end = window_start + TimeDelta(minutes=5)
    return jsonify(result)

@app.route('/home')
def home():
    return "HELLO"