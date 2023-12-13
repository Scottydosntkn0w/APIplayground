#weather API
import requests
import json
baseURL = "http://api.weatherapi.com/v1"
#apiKey = open('OpenWeatherAPI_Key.txt', 'r').read()
#oPEN = "2cfc4cbc7215c3632d554495054460e9"

location = "Wichita"
lat = 33.44
lon = -94.04
#print(apiKey)
#result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}')
result = requests.get('http://api.weatherapi.com/v1/current.json?key=184d9ceb903a42af8b610443231312&q=Wichita&aqi=no')
result = json.loads(result.text)
location = result['location']
current = result['current']
condition = current['condition']
Key_values = {'Location':location['name'],'time':location['localtime'],'temp_f' : current['temp_f'], 'wind_mph':current['wind_mph'], 'humidity':current['humidity'],
              'UV Index':current['uv']}


dive = result['current']['condition']['text']
print(dive)
print(Key_values)