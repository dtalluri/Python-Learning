sign = input("Enter a operator, + or -: ")
a1 = int(input("Enter a number: "))
a2 = int(input("Enter another number: "))
if sign == "+":
    print(a1, "+", a2, "=", a1+a2)
elif sign == "-":
    print(a1, "-", a2, "=", a1-a2)
else:
    print("Invalid Input")
