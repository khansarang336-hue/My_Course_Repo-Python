try:
    score = input("Enter Score B/w 0.0 to 1.0 :")
    score = float(score)
    if score > 1.0 or score < 0.0:
        print("Error! The Score is Out of Range Please Enter Numbers From 0.0 to 1.0")
    elif score >= 0.9:
        print("Grade A")
    elif score >= 0.8:
        print("Grade B")
    elif score >= 0.7:
        print("Grade C")
    elif score >= 0.6:
        print("Grade D")
    else:
        print("Grade F")
except:
    print("Please enter a valid numerical number")
