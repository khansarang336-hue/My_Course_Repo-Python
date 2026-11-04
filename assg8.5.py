name = input("Enter the file name : ")
if len(name)<1:
    name = "mbox-short.txt"
fh = open(name)
my_list = []
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    count = count+1
    my_list = line.split()
    print(my_list[1])
print(count)
