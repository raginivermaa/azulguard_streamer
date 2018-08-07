import csv
from app import db

from app.models import Sensor_Data
from app.models import Apartment

#
# root = r'./'
# dirs = [f for f in listdir(root) if not isfile(join(root, f))]

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
               # data.append(data_line)
               # date_times.append(sd['datetime'])
           # apartment = Apartment(aid=f, sensor_data=data)
           db.session.add(apartment)
           db.session.commit()
#
# aid = csv.DictReader(open('sensor/granularity_ranking.csv'))
# granularity_rankings = [a for a in granularity_ranking_reader]
#
# for gr in granularity_rankings:
#     gran_rank = Granularity_Ranking(rank=gr['rank'], \
#                                     name=gr['name'])
#     db.session.add(gran_rank)
# db.session.commit()
#
# for d in dirs:
#     files = [f for f in listdir(path) if isfile(join(path, f))]
#     for f in files:
#         print('converting', f)
#         data = pd.read_hdf(join(path, f))
#         if data.empty:
#             continue
#         cond = (data['reading_type'] == 'door') \
#                 | (data['reading_type'] == 'beacon') \
#                 | (data['reading_type'] == 'motion')
#         sensor_data = data[cond]
#         misc_data = data[~cond]
#         csv_name = f.split('.')[0] + '.csv'
#         sensor_data.to_csv(join(sensorPath, csv_name))
#         misc_data.to_csv(join(miscPath, csv_name))
#         print(f, 'complete')
#     print(d, 'complete')
