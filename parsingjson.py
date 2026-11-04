import json

data = '''
 {
    "name" : "sarang",
    "phone" : {
        "type" : "intl",
        "number" : "0305-3183445"},
    "email" :  {
        "hide" : "yes"}
 }'''

info = json.loads(data)
print(info["name"])
print(info["phone"]["number"])
for i,j in info.items():
    print(i, j)
