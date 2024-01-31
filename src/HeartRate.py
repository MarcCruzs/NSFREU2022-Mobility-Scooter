import pandas as pd
import json
import copy

data = json.load(open('egg.json'))
df = pd.DataFrame(data["exercises"])
samples = df.pop('samples')
heartrate = []
for x,y in enumerate(samples):
    check=y.pop('heartRate')
    for a,b in enumerate(check):
        print(b)
        TimeStamp = copy.deepcopy(b)
        value = b.pop('value')
        heartrate.append(TimeStamp)
            
df = pd.DataFrame (heartrate)
df.to_csv('processed.csv')      




'''for x,y in enumerate(samples):
    check=y.pop('heartRate')
    print(check)
    heartrate.append(check)

df = pd.DataFrame (heartrate)
df.to_csv('processed.csv')'''