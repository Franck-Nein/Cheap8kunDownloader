import requests
from bs4 import BeautifulSoup
import urllib, os
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
 if old != link: os.system ("wget -nc --retry-on-http-error=502 --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 " +'https:'+link+ " -P 'Downloads" + title.string + ' id=' + idnumber['id'] + "/'" )
 old = link
 

