# json is essentially a string with a special format

import json

data = [{"name": "Dashan", "age": 11}, {"name": "Dachui", "age": 13}]
# convert to json 
json_str = json.dumps(data)
print(type(json_str))
print(json_str)

# json to python list
s = '[{"name": "Dashan", "age": 11}, {"name": "Dachui", "age": 13}]'
l = json.loads(s)
print(type(l))
print(l)