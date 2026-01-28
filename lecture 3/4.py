a = int(input("Enter an integer a "))
b = int(input("Enter an integer b "))
c = input("Enter the operation  + , -,*,% ")

if c=="+":
    print(f"sum of numbers is {a+b}")
elif c=="-":
    print(f"Subtraction of a and b is {a-b}")
elif c=="*":
    print(f"Multiplication of a and b is {a*b}")
elif c=="%":
    print(f"remainder is {a%b}")
else:
    print("Invalid operator ")