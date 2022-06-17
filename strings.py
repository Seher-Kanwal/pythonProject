a = "Hello Seher To String "
# for displaying length
print(len(a))
# For slicing 0 is included but 4 is excluded
# as index start from 0 to till 5 we have got 0,1,2,3,4 indexes so
print(a[0:5])
# if I want to display string after leaving few characters than we give value in third filed
print(a[0:10:2])
# if we leave the first argument empty it will consider to start from zero, in case of two, it takes whole len
# and in the last, it will consider one

# negative index can access the value from the last of Strings
print("\n", a[-4: -2])

# for reversing the string
print(a[::-1])

print(a.upper())
# for only capitalize the first letter
print(a.capitalize())
# for finding something return 0 on success and -1 on failure
print(a.find("Hello"))

# replace fn
print(a.replace("To", "or"))

