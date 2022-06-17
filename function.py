def fun(i, j, k):
    # doc String, which explain what a fun do
    """ this fn takes 3 parameters as an arguments and return sum"""
    x = a + b + c
    return x


a = int(input("Enter a no:"))
b = int(input("Enter a second no:"))
c = int(input("Enter the third no:"))
# calling fn to display its doc string
print(fun.__doc__)
# calling a function
y = fun(a, b, c)
print("sum is:", y)
