import random

name = input("What is your name? ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go either left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You have come to a river, you can walk around it or swim across? Type walk to walk around it and swim to swim across: ")
    if answer == "swim":
        print("You swam across and were eaten by a fish")
    elif answer == "walk":
        print("You walk for to long, got tired and lost the game")

elif answer == "right":
    input("You have a come to a bridge and it looks weak. Do you want to walk it or head back? (cross/back) ")
    
    if answer == "back":
        print("You go back and you fell off a cliff, you lost!")
    elif answer == "cross":
        input("You crossed the bridge and met a stranger. Do you want to talk to them? ")

        if answer == "yes":
            print("You were nice and the give you gold. You won!")
        elif answer == "walk":
            print("You were rude and the shot you. You lose!")
else:
    print("Not a valid answer. You lose!")

# print("Thank you for trying", name, ".")
