import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter Url - ")
if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/comments_2427147.html"

html = urllib.request.urlopen(url)
for line in html:
    print(html)
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
total = 0
for tag in tags:
    num=int(tag.contents[0])
    total+=num

print("Total", total)
