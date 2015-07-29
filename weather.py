import requests
from bs4 import BeautifulSoup
response = requests.get('http://pm25.in/hangzhou')
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.tbody.tr.td)     
