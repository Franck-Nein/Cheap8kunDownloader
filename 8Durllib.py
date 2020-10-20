import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib, os
import urllib.request
old = 'a'
myurl = input("Enter url:")
page = requests.get(myurl)
soup = BeautifulSoup(page.content, 'html.parser')
link = []
urls = soup.select("[href^='//media.8kun.top/']")
#urls = soup.select("[href^='//media.jthnx5wyvjvzsxtu.onion.pet/file_store/']")
title = soup.find('title')
idnumber = soup.find("a", {"class": "post_anchor"})
print(idnumber['id'])
print(title.string)
if not os.path.exists('Downloads/' + title.string + ' id=' + idnumber['id']):
 os.makedirs('Downloads/' + title.string + ' id=' + idnumber['id'])
for link in urls:
 link = (link.get('href'))
 if old != link:
  old = link
  filename = link.split('/')[-1].split('#')[0].split('?')[0]
  path = 'Downloads/' + title.string + ' id=' + idnumber['id'] + '/' + filename
  fulllink = ('https:'+link)
  if not os.path.exists(path):
   print('Downloading ' + filename)
   try:
    urllib.request.urlretrieve(fulllink, path)
   except:
    print('Failed, trying onion')
    try:
     olink = fulllink.replace("https://media.8kun.top", "http://media.jthnx5wyvjvzsxtu.onion.sh")
     urllib.request.urlretrieve(olink, path)
    except:
     print('404 :(')
  else:
   print('Not downloading ' + filename)

