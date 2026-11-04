fhand = open("words.txt")
#count = 0
#for line in fhand:
#    count = count+1
#    print(line.rstrip())
#print("Line Count:", count)

#Reading the whole document with Read Function:-
#take all the character from handle in new variable

#filehandle = open("words.txt",'r')
#inp = filehandle.read()
#print(inp)
#print(len(inp))
#print(inp[:50])

#handling the character with startswith keyword

#for line in filehandle:
#    if line.startswith('Writing'):
#        print(line)

#for line in fhand:
#    line = line.rstrip()
#    if not line.startswith('Writing'):
#        continue
#    print(line)

for line in fhand:
    line = line.rstrip()
    if not 'Writing' in line:
        continue
    print(line)
