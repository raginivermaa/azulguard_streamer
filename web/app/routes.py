from app.models import Sensor_Data, Apartment
from app import app, db, window_start, window_end, update_window
from flask import jsonify

@app.route('/api/data', methods=['GET'])

def get_sensor_data():

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
    return jsonify(result)
    update_window()

@app.route('/home')
def home():
    return "HELLO"