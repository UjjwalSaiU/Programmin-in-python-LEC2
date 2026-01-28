c = int(input("Enter an integer "))
if c%5==0:
    print("Number is divisible by 5 ")
    if c%7==0:
        print("NUmber is divisible by 7")
    else:
        print("Not divisible by 7")
else:
    print("Not divisible by 5")
    if c%7==0:
        print("divisible by 7 ")
    else:
        print("Not divisible by 7")