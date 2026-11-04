name = input("Enter the File Name : ")
if len(name) < 1:
    name = "words.txt"
fh = open(name)
for line in fh:
    line.strip()
    print(line.upper())
