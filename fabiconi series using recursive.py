def fabiconi(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fabiconi(n - 1) + fabiconi(n - 2)


x = int(input("Enter a number for which you want to find fibonacci: "))
print(fabiconi(int(x)))
i = 1
while i <= x:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print("\n", end="")
    i = i + 1




