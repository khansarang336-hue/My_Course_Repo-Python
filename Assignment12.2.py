
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ingore SSL certificate errors https
ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL - ")
count = int(input("Enter Count : "))
position = int(input("Enter Position : "))

i = 0

while i < count:
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    x = BeautifulSoup(html,'html.parser') #beautifulsoup will grap the html from the given url
    #Retrieve all of the anchor tags in the HTML file
    tags = x('a') #will get all the anchor tags from the url
    url = tags[position-1].get('href',None)  #will get the url from the given position
    i = i+1
print("Retrieving:", url)
