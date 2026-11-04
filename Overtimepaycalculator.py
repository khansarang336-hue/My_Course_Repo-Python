hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hrs = int(hrs)
    rate = float(rate)
except:
    print("Enter Numerical Values")
    exit()
#print(hrs, rate)
if hrs>40:
    pay = (40*rate) + ((hrs-40)*(rate*1.5))
    print("Total Pay with OT",pay)
else:
    pay = hrs*rate
    print("Total Pay", pay)