import hashlib
import pandas as pd
import requests
import sys
import time
sys.path.insert(1, '../')
import util as util

url='https://restcountries.com/v3.1/all'  # This is a link of rest country API
data_json = util.get_data_from_url(url)                    # JSON data for display

def making_df(data):            # Making DataFrame
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
        
        time_num = (time.time() - start_time) * 1000000      # Time convertion to miliseconds (ms)

        list_region.append(data[i]['region'])                                # Add region to list
        list_city_name.append(data[i]['name']['common'])                     # Add common name to list
        list_language.append(hashlib.sha1(lang.encode("utf-8")).hexdigest()) # Encrypting data and using hexdigest() to display 
        list_time_num.append(time_num)                                       # Add time to list -> float for calculate max, min and average
        list_time.append(str(time_num)[:6] + ' us')                          # Add time to list -> str to add 'ms'

        # Add data to dict
        dict_data['Region'] = list_region
        dict_data['City Name'] = list_city_name
        dict_data['Language'] = list_language
        dict_data['Time'] = list_time

        df = pd.DataFrame(dict_data)    # Making DataFrame
        col_time = df['Time']
        time_min = col_time.min()
        time_max = col_time.max()
        time_avr = str(sum(list_time_num) / len(list_time_num))[:6]

    return dict_data, df, time_max, time_min, time_avr    


if __name__ == "__main__":
    
    dict_data, df, time_max, time_min, time_avr = making_df(data_json)

    print(df)
    print('\n------------------------------------------------------------')
    print('Times:\n', '\tMax Time', time_max, '\n\tMin Time', time_min, '\n\tAvr Time', time_avr, 'us')
    print('\n------------------------------------------------------------\n')
    util.get_json_from_dict(dict_data)

    # Storing the data in the database
    conn = util.sql_conn()                  # Making the connection
    cursor_obj = conn.cursor()

    # Creating table and columns
    countries_table = 'countries'
    data_table = 'id integer, region text, city_name text, language text, time text'
    data_table_names = 'id, region, city_name, language, time'
    util.sql_table(conn, countries_table, data_table)

    # Insert data into the table
    util.sql_insert_df(conn, countries_table, data_table_names, df)

    # View table content from DB: If want to view the content uncomment the follow lines
    '''tab = cursor_obj.execute('SELECT * FROM ' + countries_table)
    for row in tab:
        print(row)'''
