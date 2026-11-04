def computepay(hr, r):
#print(hr, rate)
    if hr>40:
        pay = (40*r)+(hr-40)*(r*1.5)
    else:
        pay = hr*r
    return(pay)
x = None
while True:
    hour = input("Enter Hours : ")
    rate = input("Enter Rate : ")
    try:
        hour = float(hour)
        rate = float(rate)
        print(computepay(hour,rate))
        break #this is the addition by AI
    except:
        print("Error! Enter Numeric Values...")
        choice = input("Press y if want to continue")
        if choice.lower() != "y": #changed the condition
            print("good bye")
            exit()
