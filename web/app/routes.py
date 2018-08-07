from app.models import Sensor_Data, Apartment
from app import app
from flask import jsonify
from flask import request

@app.route('/api/data', methods=['GET'])
def get_sensor_data():
    result = {}
    for a in Apartment.query.all():
        print('for', a)
        result[a.aid] = a.sensor_data[0]
    return jsonify(result)

@app.route('/home')
def home():
    return "HELLO"