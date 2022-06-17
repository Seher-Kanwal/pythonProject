n = int(input("Enter the value for which you want to display table:"))
t = int(input("Enter no for table:"))
i = 0
while i < n:
    if i >= 10:
        break
    i += 1
    # if i=6 0r 9 it's will not display table
    if i == 6 or i == 9:
        continue
    print(t, "*", i, "=", t * i)
