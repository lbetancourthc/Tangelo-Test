# Getting and displaying data from REST Countries
import requests

url = 'https://restcountries.com/v3.1/all'  # This is a link of rest country API
data_url = requests.get(url)                # Request data to URL
data = data_url.json()                      # JSON data for display

print(data[0])                              # Displaying data content
print(data[0].keys())                       # Duisplaying keys for data content
