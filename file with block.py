with open("text2", "rt") as fd:
    print(fd.read(46))
print("\n\n second file\n\n")
fd2 = open("text")
a = fd2.read()
print(a)
