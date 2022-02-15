# Making DataFrame
import time
import hashlib
import pandas as pd

dict_data = {}              # Dictionary to save data
list_region = []            # List to add the data of the region
list_city_name = []         # List to add the data of the city name
list_language = []          # List to add the data of the language
list_time = []              # List to add the data of the time it takes to create a row like a string for visualization
list_time_num = []          # List to add the data of the time it takes to create a row like a float for getting max, min and average

for i in range(len(data)):  
  start_time = time.time()  # Time to calculate the creation of a row 
  
  if data[i].get('languages') == None:              # Key validation
    lang = 'Not Found'                              # Add default value
  else:
    lang = list(data[i]['languages'].values())[0]   # If key exist add real value
  
  time_num = (time.time() - start_time) * 1000      # Time convertion to miliseconds (ms)

  list_region.append(data[i]['region'])                                # Add region to list
  list_city_name.append(data[i]['name']['common'])                     # Add common name to list
  list_language.append(hashlib.sha1(lang.encode("utf-8")).hexdigest()) # Encrypting data and using hexdigest() to display 
  list_time_num.append(time_num)                                       # Add time to list -> float for calculate max, min and average
  list_time.append(str(time_num)[:6] + ' ms')                          # Add time to list -> str to add 'ms'

# Add data to dict
dict_data['Region'] = list_region
dict_data['City Name'] = list_city_name
dict_data['Language'] = list_language
dict_data['Time'] = list_time

df = pd.DataFrame(dict_data)    # Making DataFrame
