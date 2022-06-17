"""As the members of a set are not in any particular order, you can’t reference them with an index"""
# there are two ways of assigning the values
a = set()
# create a list and assign to the set
l_list = [1, 2, 3, 4, 5]
b = set(l_list)
a.add(3)
a.add(4)
a.add(7)
print("Union:", a.union(b))
print("Inter-Section:", a.intersection(b))
# length, max, min, disjoint all the operations can be performed with sets


