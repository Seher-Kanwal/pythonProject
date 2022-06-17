# shorthand notation of if else
print("Enter two Values:")
v = int(input())
v2 = int(input())
"""  if condition is true then first statement will run"""
print(" a is greater than b") if v > v2 else print(" b is greater than a")


print("Enter two Values:")
var1 = int(input())
var2 = int(input())
if var1 > var2:
    print(var1, "is greater than", var2)
elif var1 == var2:  # for if else
    print("Equal...")
else:
    print(var2, "is greater than", var1)
a = [2, 4, 5, 6, 4, 34]
if 4 in a:
    print("True")
if 35 not in a:
    print("Not present")
