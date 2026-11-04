try:
    hr = input("Enter Hours : ")
    rate = input("Enter Rate per Hour : ")
    print(hr, rate)
    hr = float(hr)
    rate = float(rate)
    if hr>40:
        pay = (40*rate)+(hr-40)*(rate*1.5)
    else:
        pay = hr*rate
        print(pay)
except:
    print("Error: Please enter valid numbers for hours and rate.")
