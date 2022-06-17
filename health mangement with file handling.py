
# for entering data
x = 1
while x == 1:
    print("Enter the one name: Rohan, ali or Sara")
    user = input("Enter user name:")
    user.lower()
    print("Enter the one for entering data and two for view")
    choice = int(input("Enter the no:"))
    print("Enter the one for diet and two for exercise:")
    no = int(input("Enter the no:"))
    if choice == 1:
        # for entering data in diet
        if no == 1:
            if user == "rohan":
                fd = open("C:\\Users\\seher\\Desktop\\health\\rohan.txt", "a")
                data = input("Enter what you eat: ")
                fd.write("{0}\n".format(data))
                fd.close()
            elif user == "sara":
                fd = open("C:\\Users\\seher\\Desktop\\health\\sara.txt", "a")
                data = input("Enter what you eat: ")
                fd.write("{0}\n".format(data))
                fd.write("\n")
                fd.close()
            elif user == "ali":
                fd = open("C:\\Users\\seher\\Desktop\\health\\ali.txt", "a")
                data = input("Enter what you eat: ")
                fd.write("{0}\n".format(data))
                fd.close()
            else:
                print("You Enter invalid name...")
        if no == 2:
            if user == "rohan":
                fd = open("C:\\Users\\seher\\Desktop\\health\\rohanExercise.txt", "a")
                data = input("Enter the name of exercise: ")
                fd.write("{0}\n".format(data))
                fd.close()
            elif user == "sara":
                fd = open("C:\\Users\\seher\\Desktop\\health\\saraExercise.txt", "a")
                data = input("Enter the name of exercise: ")
                fd.write("{0}\n".format(data))
                fd.write("\n")
                fd.close()
            elif user == "ali":
                fd = open("C:\\Users\\seher\\Desktop\\health\\aliExercise.txt", "a")
                data = input("Enter what is the name of exercise: ")
                fd.write("{0}\n".format(data))
                fd.close()
            else:
                print("You Enter invalid name...")

# for viewing data
    elif choice == 2:
        # for viewing the diet data
        if no == 1:
            if user == "ali":
                fd = open("C:\\Users\\seher\\Desktop\\health\\ali.txt", "r")
                print(fd.read())
                fd.close()
            elif user == "rohan":
                fd = open("C:\\Users\\seher\\Desktop\\health\\rohan.txt", "r")
                print(fd.read())
                fd.close()
            elif user == "sara":
                fd = open("C:\\Users\\seher\\Desktop\\health\\sara.txt", "r")
                print(fd.read())
                fd.close()
            else:
                print("You Enter invalid name...")
        # view exercise data
        if no == 2:
            if user == "ali":
                fd = open("C:\\Users\\seher\\Desktop\\health\\aliExercise.txt", "r")
                print(fd.read())
                fd.close()
            elif user == "rohan":
                fd = open("C:\\Users\\seher\\Desktop\\health\\rohanExercise.txt", "r")
                print(fd.read())
                fd.close()
            elif user == "sara":
                fd = open("C:\\Users\\seher\\Desktop\\health\\saraExercise.txt", "r")
                print(fd.read())
                fd.close()
            else:
                print("You Enter invalid name...")
        else:
            print("You enter a wrong choice for diet and exercise....")
    else:
        print("You enter a wrong choice for entering and viewing the data....")
    x = int(input("IF you want to continue enter 1: "))
