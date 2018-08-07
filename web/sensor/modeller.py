from os import listdir, mkdir
from os.path import isfile, join, exists
import pandas as pd
import datetime

def get_record(last_seen, now):
    row = {}
    door = None
    for key, value in last_seen.items():
        if value != None:
            sec = (now - value).total_seconds()
            row[key] = [sec]
            #if key[0] == 'd':
            #    door = key
    #if door == None or row[door][0] == None:
    #    row['door_opened'] = None
    #else:
    #    row['door_opened'] = int(row[door][0] < 600)
    row['datetime'] = now.strftime('%Y-%m-%dT%H:%M:%S')
    row['minutes'] = (now - now.replace(hour=0, minute=0, second=0)).total_seconds()
    row['day'] = now.weekday()
    return row

root = r'C:\Users\Jianrong\Desktop'
#mp0026 having errors, skipped
#mp0033 having errors, skipped 
#mp0037 having errors, skipped
#mp0045 having errors, skipped
#start from 51
fileName = 'MP0001.csv'

modelPath = join(root, 'modelling')
filePath = join(root, 'combined_csv', fileName)
if not exists(modelPath):
    mkdir(modelPath)
df = pd.read_csv(filePath)
keys = set(df['key'].tolist())
last_seen = {key: None for key in keys}
record = pd.DataFrame(data={key: [] for key in keys})
start = datetime.datetime.strptime(df.iloc[0]['gw_timestamp'], '%Y-%m-%dT%H:%M:%S')
curr = start
pointer = 0
limit = df.count()[0]
print(curr)
for id, row in df.iterrows():
    time = datetime.datetime.strptime(row['gw_timestamp'], '%Y-%m-%dT%H:%M:%S')
    while curr < time:
        record = record.append(pd.DataFrame(get_record(last_seen, curr)), ignore_index=True)
        curr += datetime.timedelta(minutes=5)
        print(curr)
    if str(row['value']) in ['1', '255']:
        last_seen[row['key']] = time
        
record.to_csv(join(modelPath, fileName))
                