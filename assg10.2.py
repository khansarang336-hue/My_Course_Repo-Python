name = input("Enter the File Name : ")
if len(name)<1:
    name = "mbox-short.txt"
fh = open(name)
tm = {}
for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    hour = words[5].split(":")
    tm[hour[0]] = tm.get(hour[0],0)+1
for key,count in sorted(tm.items()):
    print(key, count)
