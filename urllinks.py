#pulling the anchor tags with beautiful Soup Libarary

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ingore SSL certificate errors https
ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode = ssl.CERT_NONE
links = []
url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
x = BeautifulSoup(html,'html.parser')

#Retrieve all of the anchor tags in the HTML file
tags = x('a')
for tag in tags:
    links.append(tag.get('href',None))
    print(links[18])
