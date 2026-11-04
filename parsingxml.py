import xml.etree.ElementTree as ET #importing the library of XML object

input = '''
<stuff>
        <users>
                <user x='2'>
                    <id>001</id>
                    <name>Sarang</name>
                </user>
                <user x='7'>
                    <id>002</id>
                    <name>Daneen</name>
                </user>
        </users>
</stuff>'''
names = []
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('user count : ', len(lst))

for item in lst:
    print(item.find('name').text)
    print(item.find('id').text)
    print(item.get('x'))
