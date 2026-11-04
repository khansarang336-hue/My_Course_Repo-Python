#My first regex
import re
text = "I love python programming"
result = re.search("python", text)
print(result)

if re.search("python", text):
     print("Found")
else:
     print("Not Found")

text2 = "cat bat pat cat"
result2 =  re.findall("cat", text2)
print(result2)

text3 = "Room 101 Sarang 3 202 2"
print(re.findall(r"\D", text3))
print(re.findall(r"\D", text2))

text4 = "Python _3"
print(re.findall(r"\w",text4))

text5 = "Python@1!"
print(re.findall(r"\W",text5))

text6 = "I love Python  "
print(re.findall(r"\s",text6))

text7 = "cat pat bat"
print(re.findall(r".t", text7))

print(re.findall(r"[cbp]at",text7))

text8 = "apple banana orange"

print(re.findall(r"[aeiou]", text8))

tex9t = "abc123"

print(re.findall(r"[^0-9]", tex9t))
