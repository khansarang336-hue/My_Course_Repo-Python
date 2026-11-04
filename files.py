#playing with files
fname = input('Enter File Name: ')
count = 0
fh = open(fname)
for line in fh:
    line = line.read()
    print(len.line)
