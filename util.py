import json
import requests
import sqlite3
from sqlite3 import Error

def get_data_from_url(url):
    #url='https://restcountries.com/v3.1/all'  # This is a link of rest country API
    data_url = requests.get(url)              # Request data to URL
    data = data_url.json()                    # JSON data for display
    return data

def get_json_from_dict(dict_data):
    # Making and download JSON file from data dict
    data_json = json.dumps(dict_data)     # Dict to JSON
    json_file = open('data.json', 'w')    # Creating the file
    json_file.write(data_json)            # Writing data
    json_file.close()                     # Saving data JSON as data.json
    print('Downloading data JSON file...')
    #print(data_json)                      # Displaying data.json

def sql_conn():
    try:
        conn = sqlite3.connect('countries_db.db')     # Creating DB
        return conn
    except Error:
        print(Error)

def sql_table(conn, table, data):
    cursor_obj = conn.cursor()                     # Cursor object to execute statements
    cursor_obj.execute('CREATE TABLE IF NOT EXISTS ' + table + '(' + data + ')')
    conn.commit()

def sql_insert_df(conn, table, data, df):
    cursor_obj = conn.cursor()                     # Cursor object to execute statements
    for row in df.itertuples():                    # Insert dataframe rows one by one
        sql_sentence = f"INSERT INTO " + table + f"(" + data + f") VALUES({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}')"
        cursor_obj.execute(sql_sentence)
    conn.commit()
    print('We have inserted', row[0]+1, 'records to the table.')