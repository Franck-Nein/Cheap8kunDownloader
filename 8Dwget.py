import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib, os
import urllib.request
myurl = input("Enter url:")
page = requests.get(myurl)
soup = BeautifulSoup(page.content, 'html.parser')
link = []
asd = soup.select("[href^='//media.8kun.top/file_store/']")
title = soup.find('title')
idnumber = soup.find("a", {"class": "post_anchor"})
print(idnumber['id'])
print(title.string)
idnumber = soup.find("a", {"class": "post_anchor"})
if not os.path.exists('Downloads/' + title.string + ' id=' + idnumber['id']):
    os.makedirs('Downloads/' + title.string + ' id=' + idnumber['id'])
with open('wget.sh', 'w') as f:
 sys.stdout = f
 print("wget -nc --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i urls.txt -P 'Downloads" + title.string + ' id=' + idnumber['id'] + "/'" )
with open('urls.txt', 'w') as f:
 sys.stdout = f
 for link in asd:
  link = (link.get('href'))
  print('https:'+link)
os.system ("./wget.sh")
