import json
from pandas.io.json import json_normalize
import csv



json_data1 = '{"a0": 1, "a1": 2, "a2": 3, "a3": 4, "a4": 5, "a5": 1, "a6": 2, "a7": 3, "a8": 4, "a9": 5, "a10": 1, "a12": 2, "a13": 3, "a14": 4, "a15": 5}'

parsed_json1 = json.loads(json_data1)
print(type(parsed_json1)) #unsorted dictionary data 

parsed_json1_string = json.dumps(parsed_json1,sort_keys=True)

print(type(parsed_json1_string)) # sorted string data 

final_dictionary = json.loads(parsed_json1_string)

print(final_dictionary)

print(final_dictionary.keys())
