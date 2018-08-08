from app.models import Sensor_Data, Apartment
from app import app, db, window_start, window_end
from datetime import timedelta as TimeDelta
import datetime
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

@app.route('/reset')
def reset():
    global window_start
    global window_end
    window_start = datetime.datetime(2017, 10, 26, hour=16, minute=40, second=0, microsecond=0)
    window_end = window_start + TimeDelta(minutes=5)
    return jsonify({'status': 'successfully reset time to 2017-10-26T16:40:00'})
