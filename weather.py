import requests
from bs4 import BeautifulSoup
import json

response = requests.get('http://pm25.in/hangzhou')

soup = BeautifulSoup(response.text, "html.parser")
tab = soup.find('table', attrs={'id':'detail-data'})
i = 0
rows = tab.find_all('tr')
list = []
for row in rows:    
    if (i == 0):
        i+= 1
        continue

    cols = row.find_all('td')[0:3]
    dict = {}
    print(cols[0].text.strip())
    dict['addr'] = cols[0].text.strip()
    dict['pm25'] = cols[1].text.strip()
    json_str = json.dumps(dict,skipkeys=True, ensure_ascii=False,indent=2)
    print json_str
    list.append(json_str)
    
    print('####################')
print list
