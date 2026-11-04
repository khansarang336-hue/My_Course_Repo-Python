import urllib.request
from bs4 import BeautifulSoup

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

step = 0

while step < count:
    print("Retrieving:", url)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    links = soup('a')
    next_link = links[position - 1]

    url = next_link.get('href')

    step = step + 1

print("Last Retrieving:", url)
