fname = input("Enter the File Name: ")
if len(fname)<1: fname = "clown.txt"
fhand = open(fname)

many = dict()

for line in fhand:
    line  = line.rstrip()
    wds = line.split()
    print(wds)
    for w in wds:
        many[w] = many.get(w,0)+1
#Finding  the top 5 word by frequency
#print(many.items())
tmp = dict()
newlist = list()
for k,v in many.items():
    newtup = (v,k)
    #print(newtup)
    newlist.append(newtup)
#print(newlist)
srt = sorted(newlist, reverse=True)
#print(srt)

for v,k  in srt[:5]:
    print(k, v)
