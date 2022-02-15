# Making database connection
import sqlite3
from sqlite3 import Error

def sql_conn():
  try:
    conn = sqlite3.connect('contries_db.db')     # Creating DB
    return conn
  except Error:
    print(Error)

def sql_table(conn, table, data):
  cursor_obj = conn.cursor()                     # Cursor object to execute statements
  cursor_obj.execute('CREATE TABLE IF NOT EXISTS ' + table + '(' + data + ')')
  conn.commit()

def sql_insert(conn, table, data, df):
  cursor_obj = conn.cursor()                     # Cursor object to execute statements
  for row in df.itertuples():                    # Insert dataframe rows one by one
    sql_sentence = f"INSERT INTO " + table + f"(" + data + f") VALUES({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}')"
    cursor_obj.execute(sql_sentence)
  conn.commit()
  print('We have inserted', row[0]+1, 'records to the table.')

# Making the connection
conn = sql_conn()
cursor_obj = conn.cursor()

# Creating table and columns
countries_table = 'countries'
data_table = 'id integer PRIMARY KEY, region text, city_name text, language text, time text'
data_table_names = 'id, region, city_name, language, time'

sql_table(conn, countries_table, data_table)

# Insert data into the table
sql_insert(conn, countries_table, data_table_names, df)
