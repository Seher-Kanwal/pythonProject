def iterative(n):
    f = 1
    c = 1
    for i in range(n):
        f = f * c
        c = c + 1
    return f


def recursive(n):
    if n == 1 or n == 0:
        return 1;
    else:
        n = n * recursive(n - 1)
    return n


try:
    x = input("Enter a number for which you want to find factorial: ")
    y = iterative(int(x))
    z = recursive(int(x))
    print("factorial due to iterative: ", y)
    print("factorial due to recursive: ", z)
except Exception as e:
    print(e)
