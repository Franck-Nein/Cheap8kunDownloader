import requests
from bs4 import BeautifulSoup
import urllib, os
import urllib.request
old = 'a'
retries = 3
myurl = input("Enter url:")
page = requests.get(myurl)
soup = BeautifulSoup(page.content, 'html.parser')
link = []
urls = soup.select("[href^='//media.8kun.top/']")
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
   while retries > 0 :
    try:
     urllib.request.urlretrieve(fulllink, path)
     retries = 3
    except:
     print("Failed, retry " + str(retries) + '/3 remaining')
     retries -= 1
     if retries == -1:
      print('Failed, trying onion')
      olink = fulllink.replace("https://media.8kun.top", "http://media.jthnx5wyvjvzsxtu.onion.sh")
      urllib.request.urlretrieve(olink, path)
      print('404 :(')
      break
     continue
    else:
     retries = 3
     break
   retries = 3
  else:
   print('Not downloading ' + filename)

