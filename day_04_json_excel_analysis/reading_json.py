# Reading JSON data

data = pd.read_json('/content/json_data/1.json')
data.head()

# Reading a json file as it is written
data_with_records = pd.read_json('/content/json_data/1.json', lines=True)
data_with_records.head()

# importing the json module of standard library
import json
# open and load the data in json
with open('/content/json_data/nested.json') as f:
    data = json.load(f)
print(data)

# print in a formatted way

from pprint import pprint
pprint(data)