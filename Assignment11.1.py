import re
#print( sum( [ int(x) for x in re.findall('[0-9]+', open('Actual Data.txt').read()) ] ) )
#Above is the one liner for below code. read it from right to left
#description: open the file and read it after reading find the integers from 0 to 9 + 1 or more digits and put
#into x variable after that convert the string in x into integer and sum them all and take the printout.

name = input("Enter the file name : ")
if len(name)<1:
    name = "Actual Data.txt"
total = 0
try:
    fh = open(name)
except FileNotFoundError:
    print("Error, specified file name not found")
    exit()
for line in fh:
    str = fh.read()
    numbers = re.findall(r"[0-9]+",str)

for n in numbers:
    numbers = int(n)
    total = total+numbers
print("The Total Sum of All Found Integers is = ",total)
exit()
