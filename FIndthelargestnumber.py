num = [40,5,6,95,10]
count = 0
total = 0
average = 0
largest_num = -1
smallest_num = num[0]
for i in num:
    count = count+1
    total = total+i
    if i>largest_num:
        largest_num = i
    #if smallest_num is None:
    if i < smallest_num:
        smallest_num = i
    #elif i < smallest_num:
    #    smallest_num = i
average = total/count
print( 'totc=',count,' totval=',total,' ave=',average,' LN=',largest_num)
print('smallest number = ', smallest_num)
