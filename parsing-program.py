import json
import pandas as pd 
from pandas.io.json import json_normalize
import csv 


json_data1 = 

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

