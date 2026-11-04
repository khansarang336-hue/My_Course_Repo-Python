#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter the File Name: ")
if not name:
    name = "mbox-short.txt"
try:
    fh = open(name)
except:
    print("Fail! File NOt FOund : {name} ")
sender = {}
maxsender = None
maxcount = 0

for line in fh:
    if not line.startswith("From "):
        continue
    parts = line.split()
    #print(parts)
    emails = parts[1]
    sender[emails] = sender.get(emails,0)+1

for  email, count in sender.items():
    if maxcount < count:
        maxsender = email
        maxcount = count
print(maxsender,maxcount)
