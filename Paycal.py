hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hrs = int(hrs)
    rate= float(rate)

    if hrs>40:
        extra = hrs-40
        pay = (hrs*rate)+(extra*rate*1.5)
    else:
        pay = hrs*rate
except:
    print("Error, Please Enter Numeric Values")
    #print(hrs, rate)
    exit()
print("Total Salary",pay)
