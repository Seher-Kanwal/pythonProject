x = input("Enter no: ")
y = input("Enter some data: ")
try:
    z = int(x) + int(y)
    print(z)
except Exception as e:
    print(e)

print("\n\n hello after the error code ")
