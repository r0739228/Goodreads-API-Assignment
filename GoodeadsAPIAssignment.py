from xml.etree import ElementTree
from columnar import columnar
import urllib.parse
import requests

#URL maken
basisUrl = 'https://www.goodreads.com/search/index.xml?'
CONSUMER_KEY = input('What is your authentication key? ')
book = input('Which book are you searching for? ')
url = basisUrl + urllib.parse.urlencode({'key' : CONSUMER_KEY, 'q' : book})

#API request
r = requests.get(url)
root =  ElementTree.fromstring(r.content)

#Arrays aanmaken
headers = ['Title', 'Author']
data = []

#Data samenvoegen
for i in root.iter('best_book'):
    work = []
    work.append(i.find('title').text)
    work.append(i.find('author').find('name').text)
    data.append(work)

#Tabel weergeven
table = columnar(data, headers, no_borders=False)
print(table)