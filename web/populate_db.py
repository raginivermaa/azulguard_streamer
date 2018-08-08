import csv
from app import db
from app.models import Sensor_Data
from app.models import Apartment

import os

directory = r'./sensor'
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           f = file
           data = []
           date_times = []
           print('registering data for ', f)
           apartment = Apartment(aid=f[:-4])
           contents = csv.DictReader(open('sensor/'+f))
           sensor_data = [sd for sd in contents]
           for sd in sensor_data:
               print('file: ', f, ' | timestamp: ', sd['datetime'])
               data_line = Sensor_Data(beacon=sd['beacon'], \
                           d_01 = sd['d-01'],\
                           m_01 = sd['m-01'],\
                           m_02 = sd['m-02'],\
                           m_03 = sd['m-03'],\
                           m_04 = sd['m-04'],\
                           minutes = sd['minutes'],\
                           day = sd['day'],\
                           datetime = sd['datetime'],\
                           apartment = f[:-4])
               db.session.add(data_line)
           db.session.add(apartment)
           db.session.commit()