#10.2 Write a program to read through the mbox-short.txt
#and figure out the distribution by hour of the day for each
#of the messages. You can pull the hour out from the 'From '
#line by finding the time and then splitting the string a
#second time using a colon.From stephen.marquard@uct.ac.za
#Sat Jan  5 09:14:16 2008 Once you have accumulated the
#counts for each hour, print out the counts,
#sorted by hour as shown below.

name =  input("Enter the File Name: ")
if not name:
    name = "mbox-short.txt"
try:
    fh = open(name)
except:
    print("fail File not Found:", name)
    quit()
tm = {}
for line in fh:
    if not line.startswith("From "):
        continue
    #print(line)
    words = line.split()
    #print(words)
    hour = words[5].split(":")
    #print(hour)
    tm[hour[0]] = tm.get(hour[0],0)+1
    #times2.append(times[0])
#print(times2)

#for key in times2:
    #print(key)
#    tm[key] = tm.get(key,0)+1
#print(tm)

for key,count in sorted(tm.items()):
    print(key, count)
