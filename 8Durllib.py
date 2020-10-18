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
for link in asd:
 link = (link.get('href'))
 filename = link.split('/')[-1].split('#')[0].split('?')[0]
 path = 'Downloads/' + title.string + ' id=' + idnumber['id'] + '/' + filename
 print(path)
 print(filename)
 fulllink = ('https:'+link)
 print(fulllink)
 urllib.request.urlretrieve(fulllink, path)

