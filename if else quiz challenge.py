print("Enter Your Age:")
age = int(input())
if (age > 18) and (age <= 100):
    print("You can drive...")
elif age == 18:
    print("Come to the office, after examine we can decide... ")
elif age > 100:
    print("You Entered an invalid age....")
else:
    print("You Can't Drive")
