import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter Location: ')
if len(url)<1:
    url = "http://py4e-data.dr-chuck.net/comments_2427149.xml"

fh = urllib.request.urlopen(url)
data = fh.read()

print('Retrieving' url)
print('Retrieved', len(data), 'characters')

numbers = list()

tree = ET.fromstring(data)
counts = tree.findall('comments/comment/count')

for r in counts:
    numbers.append(int(r.text))
print('Counts: ', len(numbers))
print('SUM:', sum(numbers))
