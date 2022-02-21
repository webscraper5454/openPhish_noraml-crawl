from curses.ascii import isspace
import requests
from bs4 import BeautifulSoup
import os

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


url2 = requests.get("https://openphish.com/feed.txt")
data = url2.content

soup2 = BeautifulSoup(data,"html.parser")
soup2.find("body")
file_write.write(str(soup2))

   



            
