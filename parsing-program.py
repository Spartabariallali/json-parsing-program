import json
import pandas as pd 
from pandas.io.json import json_normalize
import csv 


json_data1 = '{"trace10": "25-04-2020 15:49:55,TailoringVariableResponse, Response reported by the user for tailoring variable 11 is Pleasant", "trace2": "25-04-2020 15:49:12,TailoringVariableResponse, Response reported by the user for tailoring variable 3 is Neither", "trace13": "25-04-2020 18:41:49,Location, Location Sensor Enabled", "trace8": "25-04-2020 15:49:43,TailoringVariableResponse, Response reported by the user for tailoring variable 9 is All of the Time", "trace0": "25-04-2020 15:48:55,TailoringVariableResponse, Response reported by the user for tailoring variable 1 is Agree", "trace14": "25-04-2020 18:41:49,Activity, Latest Activity:STILL START", "trace4": "25-04-2020 15:49:19,TailoringVariableResponse, Response reported by the user for tailoring variable 5 is Agree", "trace3": "25-04-2020 15:49:16,TailoringVariableResponse, Response reported by the user for tailoring variable 4 is Agree", "trace1": "25-04-2020 15:49:00,TailoringVariableResponse, Response reported by the user for tailoring variable 2 is Disagree", "trace9": "25-04-2020 15:49:46,TailoringVariableResponse, Response reported by the user for tailoring variable 10 is Some of the Time", "trace11": "25-04-2020 15:49:58,TailoringVariableResponse, Response reported by the user for tailoring variable 12 is Yes", "trace5": "25-04-2020 15:49:27,TailoringVariableResponse, Response reported by the user for tailoring variable 6 is Agree", "trace12": "25-04-2020 18:41:49,Location, Latest Location:LocationResult[locations: [Location[fused 51.581706,0.061787 hAcc=8 et=+4h17m24s714ms alt=89.16802978515625 vel=0.63 bear=1.0 vAcc=8 sAcc=1 bAcc=58 {Bundle[mParcelledData.dataSize=52]}]]]", "trace6": "25-04-2020 15:49:29,TailoringVariableResponse, Response reported by the user for tailoring variable 7 is Agree", "trace7": "25-04-2020 15:49:37,TailoringVariableResponse, Response reported by the user for tailoring variable 8 is Agree"}'

parsed_json1 = json.loads(json_data1)
print(type(parsed_json1)) #unsorted dictionary data 

parsed_json1_string = json.dumps(parsed_json1,sort_keys=True)

print(type(parsed_json1_string)) # sorted string data 

final_dictionary = json.loads(parsed_json1_string)

print(type(final_dictionary))

with open('second-test-data.json','w') as fp:
    json.dump(final_dictionary, fp)

with open('second-test-data.json') as f:
    data = json.load(f)

df = json_normalize(data)
print(df)   

value1 = df.transpose()
print(value1)

# df.to_csv('second-final-output.csv')
value1.to_csv('final-output1.csv', index=True)

