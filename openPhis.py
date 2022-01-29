from curses.ascii import isspace
import requests
from bs4 import BeautifulSoup


file_write = open('openPhis_domains.txt','w')
url = requests.get('https://openphish.com/').content

beautify = BeautifulSoup(url, 'html.parser')

data = beautify.find_all('table')

for i in  data:
    tr = i.find_all('tr')
    for j in tr:
        if not isspace(j):
            data = j.text
            file_write.write(data)
            
