import math
me = "Seher"
a = "this is %s" % me
print(a)

# . string formatting

b = "kanwal"
c = "this is {} {}"
d = c.format(me, b)
print(d)
print("\nby changing numbering in the parameters:")
c = "this is {1} {0}"
d = c.format(me, b)
print(d)

# f Strings
a = f"this is {me} {b}  using fstrings also using cos fn of math module: {math.cos(45)} "
print(a)
