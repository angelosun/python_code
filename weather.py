import requests
from bs4 import BeautifulSoup

response = requests.get('http://pm25.in/hangzhou')

soup = BeautifulSoup(response.text, "html.parser")
tab = soup.find('table', attrs={'id':'detail-data'})
i = 0
rows = tab.find_all('tr')
for row in rows:    
    if (i == 0):
        i+= 1
        continue

    cols = row.find_all('td')[0:3]
    for ele in cols:
        print(ele.text.strip())
    print('####################')

