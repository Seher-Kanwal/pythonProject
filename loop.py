list1 = ["ary", "Geo", "Public", "Government"]
for item in list1:
    if item == "Geo":
        print(item)

# list with in the list
list2 = [["candies", 2], ["Biscuits", 5], ["Lays", 5], ["Nimko", 7]]
# if we simply use one var it will display list but when we use two var it will display both elements of lsit
for snacks, quantity in list2:
    print("Snacks are:", snacks, " and the quantity is:", quantity)

# done using dictionary too, it will give us only the kwy value
dict1 = dict(list2)
for item in dict1:
    print(item)