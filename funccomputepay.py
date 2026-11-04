def computepay(h, r):
    try:
        h = int(h)
        r = float(r)
        if h>40:
            pay = (40*r)+(h-40)*(r*1.5)
        else:
            pay = h*r
    except:
            print("Enter Numeric Value")
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

p = computepay(hrs, rate)
print("Pay",p)
