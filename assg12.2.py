import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


url = input("Enter URL - ")
count = int(input("Enter Count - "))
pos = int(input("Enter Position - "))
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Ohran.html"

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    print(tags[pos-1].get('href',None))
    url = tags[pos-1].get('href', None)
