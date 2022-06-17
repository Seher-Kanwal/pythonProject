
# tuple = little sealed packets of information

d_tuple = (2, 4, 7, 6)
# it is immutable means that we can't change the value, so the given statement will give an error
# d_tuple[4] = 5
# The sequence can be unpacked by doing the reverse:
a, b, c, d = d_tuple
print(a, b, c, d)

"""If you want to make a tuple that only contains one item, you must follow the item with a single 
comma (item,)."""
s_tuple = (2,)
print(s_tuple)
