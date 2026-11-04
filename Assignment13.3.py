import urllib.request, urllib.parse, urllib.error
import json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?' #declaring the service url where the user provided address will be searched this is a API


while True:
    address = input("Enter Location - ") #asking location from the user
    if len(address) < 1:
        break
    address = address.strip() #stiping the unnecessary spaces from the user provided address
    parms = dict() #declaring a dictionary
    parms['q'] = address #putting address in dictiony with key value q (q=query)
    url = serviceurl + urllib.parse.urlencode(parms) # encoding it in utf-8 so the q=address will go to the side instead of q:address
    fh = urllib.request.urlopen(url) #making the file handler
    data = fh.read().decode() #reading the data from hanlde and decoding it in unicode for python understanding
    print('Retrieving', url)
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) # loading the data in json format same as dictionay in python
    except:
        js = None
    if not js or 'features' not in js:
         print('==== Download error')
         print(data)
         break
    if len(js['features']) == 0:
         print('==== Object not found ====')
         print(data)
         break
    print('Plus_code', js['features'][0]['properties']['plus_code']) #parsing and printing the data in js dictionary or in json format
