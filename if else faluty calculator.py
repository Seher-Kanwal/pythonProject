print("Enter two numbers:")
a = int(input("Enter First Number:"))
b = int(input("Enter Second numer"))
op = input("Enter An operator(+,-,*,/):")
if op == "+":
    if (a == 56) and (b == 9):
        print(77)
    else:
        print(a+b)
elif op == "-":
    if (a == 56) and (b == 9):
        print(40)
    else:
        print(a-b)
elif op == "*":
    if (a == 45) and (b == 3):
        print(555)
    else:
        print(a*b)
elif op == "/":
    if (a == 56) and (b == 6):
        print(4)
    else:
        print(a/b)
else:
    print("invalid Operator....")

