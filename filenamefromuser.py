#prompt the file name from user
fname = input("Enter the File Name to Open:")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Writing"):
      count = count+1
print('There were', count, 'writing lines in', fname)
