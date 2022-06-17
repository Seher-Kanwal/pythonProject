veg = ["bind", "okra", "carrot", "radish", "chilli"]
print(veg[4])
# You can replace a slice of your list with another sequence using list[i:j:step]
# start from 0 index and then enter after 1 location
veg[::2] = ["ali", "alia", "alina"]
print(veg)
# The keyword del can be used to remove entire variables or slices of a list.
del veg[4:]
veg.remove("ali")
print(veg)

num = [2, 3, 7, 1, 9]
print(num)
# for sorting the string
num.sort()
# for reversing the string, they change original string
num.reverse()
print(num)
# slicing in the List it does not change the original list
print(num[0:3])
# append insert at the end
num.append(23)
# insert enter at the specific location
num.insert(4, 65)
print(num)
# max min fn are available here
print(max(num))
# pop del the value in the last and return the value too,
# removing a specific index is  done using list.pop(i)
print(num.pop())
# in order to change value
num[3] = 100
print(num)
