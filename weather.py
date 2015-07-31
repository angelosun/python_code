import requests
from bs4 import BeautifulSoup
import json
from pymongo import MongoClient
import time


response = requests.get('http://pm25.in/hangzhou')

soup = BeautifulSoup(response.text, "html.parser")
tab = soup.find('table', attrs={'id':'detail-data'})
i = 0
rows = tab.find_all('tr')

client = MongoClient('localhost', 27017)
db = client['weather']
weather_hz = db.weather_hz

for row in rows:    
    if (i == 0):
        i+= 1
        continue

    cols = row.find_all('td')[0:3]
    dict = {}

    dict['datetime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    dict['addr'] = cols[0].text.strip()
    dict['pm25'] = cols[1].text.strip()
    weather_hz.insert_one(dict)
    #json_str = json.dumps(dict,skipkeys=True, encoding="utf-8")


