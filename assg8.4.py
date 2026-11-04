name = input("Enter the File Name : ")
if len(name)<1:
    name = "romeo.txt"
uw = []
fh = open(name)
for line in fh:
    words = line.split()
    #print(words)
    for word in words:
        if word not in uw:
            uw.append(word)
        else:
            continue
print("List\n",uw,"\n\n\n")
uw.sort()
print("Sorted List\n", uw)
