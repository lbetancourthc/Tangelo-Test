# Making and download JSON file from data dict
import json

data_json = json.dumps(dict_data)     # Dict to JSON
json_file = open('data.json', 'w')    # Creating the file
json_file.write(data_json)            # Writing data
json_file.close()                     # Saving data JSON as data.json
print(data_json)                      # Displaying data.json
