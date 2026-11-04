import urllib.request, urllib.parse, urllib.error
mydict = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = (line.decode().split())
    for word in words:
        mydict[word] = mydict.get(word,0)+1
print(mydict)
