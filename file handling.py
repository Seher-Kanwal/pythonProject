"""
r : read mode ----default mode
w : write mode
+ : both read and write
a : append at the last of the file
t : text mode ----default mode
b : binary mode
x : create a file if not exists

"""

# as usual return a fd, text file is created in that folder
fd1 = open("text", "rt")
cntnt = fd1.read()
print("\n\n", cntnt)

""" If we read a file once, the fd become empty """

fd = open("text", "rt")
# if we want to read specific no of characters
content = fd.read(5)
print(content)

# if I call again then it will read next characters
content = fd.read(5)
print(content)

fd.close()
fd1.close()

"""print("read a file as a list\n")
hell = open("text", "rt")
print(hell.newlines())
hell.close()"""

# in order to read a file line by line
print("\n\n,read line by line\n")
fd2 = open("text", "rt")
print(fd2.readline())
print(fd2.readline())
print(fd2.readline())
fd2.close()
