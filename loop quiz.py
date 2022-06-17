print("Enter the length of the list:")
n = int(input())
list1 = []
# for running the loop to n
for i in range(0, n):
    print("Enter a value to add in the list at index:", i)
    var1 = int(input())
    list1.append(var1)
print(list1)
for items in list1:
    if items > 6:
        print(items)
print("\n End List \n")
list2 = [" hell", 34, "ali", 8, 4, 38, ]
for item in list2:
    # str refers to the pointer
    if str(item).isnumeric() and item > 6:
        print(item)

