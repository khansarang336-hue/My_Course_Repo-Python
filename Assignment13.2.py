import urllib.request, urllib.parse, urllib.error
import json, ssl

url = input('Enter URL - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2427150.json'

fh = urllib.request.urlopen(url)
data = fh.read()
numbers = []
count = 0
total = 0
js = json.loads(data)
print('Retrieving', url)
print('Retrieved', len(data), 'characters')
comments = js['comments']
for i in comments:
    numbers = int(i['count'])
    total = total + numbers
    count = count+1
print('Count: ', count)
print('Sum ', total)
