from colorama import Fore
from Find_treasure_art import logo


print("WELCOME TO TREASURE ISLAND GAME ! ! ! ".title())
print("Your mission is to find the treasure. ")

choice1 = input(
    "You are at a crossroad, where do you want to go? Type 'left' or 'right': "
).lower()

if choice1 == "left":
    choice2 = input(
        "You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim':\n"
    ).lower()
elif choice1 == "right":
    print(Fore.RED + "Game over ! ! " + Fore.RESET)
    exit()


if choice2 == "swim":
    print(Fore.RED + "You are attacked by trout. Game over !" + Fore.RESET)
    exit()
elif choice2 == "wait":
    choice3 = input(
        "You arrived at the island unharmed. There is a house with 3 doors. One 'red', one 'yellow' and one 'blue'. Which color do you choose? "
    ).lower()

if choice3 == "red":
    print("Burned by fire. Game over ! ! ")
elif choice3 == "blue":
    print("Eaten by beasts. Game over ! ! ")
elif choice3 == "yellow":
    print(Fore.GREEN + "Congrats! You found the treasure.".title() + Fore.GREEN)
else:
    print(Fore.RED + "Choose door wisely. Game over ! ! " + Fore.RESET)
