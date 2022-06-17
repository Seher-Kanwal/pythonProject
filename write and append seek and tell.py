fd = open("text", "a")
a = fd.write("Seher Your doing best....\n")
print("A contains the no of characters written in the file:", a)
fd.close()

# + for both read and write mode
# r before + indicate that we first read and then write
fd2 = open("text2", "r+")
print(fd2.read())
a = fd2.write("Seher You are best....\n")
print("A contains the no of characters written in the file:", a)
fd2.close()

# seek is used to set the position of the pointer where we want to start
# tell fn tells that where we actually are

fd3 = open("text2", "rt")
print("Where the pointer right now", fd3.tell())
print(fd3.readline())
print("Location of the pointer set at ", fd3.seek(45))
print(fd3.readline())
fd3.close()
