no = 23
i = 1
print("\n\n*******************************Guess the Number Game************************")
print("You just have 5 turns for this game....")
while i <= 5:
    print("Turn no is: ", i)
    i += 1
    user = int(input("Enter Your guess Number:"))
    if 20 < user < 22:
        print("You're closer to the hint. \n You just need to increase  your guess no.... ")
    elif 24 <= user < 30:
        print("You're closer to the hint. \n You just need to decrease your guess no.... ")
    elif user <= 20:
        print("You need to update your guess a little bit... ")
    elif 30 <= user <= 40:
        print("You Enter a larger no. \n "
              "You just need to decrease your guess no by a factor between 10 to 20.... ")
    elif user >= 45:
        print("You Enter a larger no. \n "
              "You just need to decrease your guess no by a factor between 40 to 60.... ")
    elif user <= 15:
        print("You Enter a small no.\n "
              "You just need to increase  your guess no by a factor between 5 to 10....")
    elif user == no:
        i = 5
        print("you guess the right no...")
        if i <= 5:
            print("You turn is finished")
            print("if you want to continue Enter 1:")
            x = int(input())
            if x == 1:
                i = 1
        break
    if i == 5:
        print("You turn is finished")
        print("if you want to continue Enter 1:")
        x = int(input())
        if x == 1:
            i = 1



