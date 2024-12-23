name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, the path has split where you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to to a river, you can walk aroud it or swim across? Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator!!!")
        print("Game Over!!!!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game!!!")
        print("Game Over!!!!")
    else:
        print("Not a valid option. You lose!!!")


elif answer == "right":
    answer = input("You arrived at a hanging bridge, looking all wobbly and old would you like to cross it? Type cross to cross it or back to head back. ")

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them? Yes or NO: ")
        if answer == "yes":
            print("You talk to the stranger and get gold")
            print("You Win!!!!")
        elif answer == "no":
            print("You ignore the stranger and try to walk away only to walk into the minefield")
            print("Game Over!!!!")
        else:
            print("Not a valid option. You lose!!!")

    elif answer == "back":
        print("You walked back to the main road, there you get hit by a car.")
        print("Game Over!!!!")
    else:
        print("Not a valid option. You lose!!!")
else:
    print("Not a valid option. You lose!!!")

print(f"Thank You for playing {name}")