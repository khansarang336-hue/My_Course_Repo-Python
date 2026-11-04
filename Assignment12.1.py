import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL = ")
html = urllib.request.urlopen(url, context=ctx)
x = BeautifulSoup(html, 'html.parser')
tags = x('span')
total = 0
count = 0
for tag in tags:
    str = ("contents: ", tag.contents[0])
    numbers = int(str[1])
    total = total+numbers
    count = count+1
print("Total = ", total, "\nCount = ", count)
