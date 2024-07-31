from colorama import Fore
import random as rn
from Rock_paper_sci_art import logo, rock, paper, sci

print(logo)
game_continue = True
while game_continue:
    art = [rock, paper, sci]
    user_pick = input(
        "What do you choose? Type: \n>> 0 for Rock\n>> 1 for Paper\n>> 2 for Scissor\n>> 'q' to exit "
    )

    while user_pick not in ("0", "1", "2", "q"):
        print(Fore.RED + "Input is not valid. Try again.".title() + Fore.RESET)
        user_pick = input(
            "What do you choose? Type: \n>> 0 for Rock\n>> 1 for Paper\n>> 2 for Scissor\n>> 'q' to exit "
        )

    if user_pick == "q":
        exit()
    else:
        user_pick = int(user_pick)

    print(f"You choose: {art[user_pick]}")

    computer_pick = rn.randint(0, 2)
    print(f"Computer choose: {art[computer_pick]}")

    def compare():
        print(Fore.GREEN)
        if user_pick == computer_pick:
            print("Draw 🤨")
        elif user_pick == 0 and computer_pick == 1:
            print("Computer wins 🙂")
        elif user_pick == 0 and computer_pick == 2:
            print("You win 😙")
        elif user_pick == 1 and computer_pick == 0:
            print("You win 😙")
        elif user_pick == 2 and computer_pick == 1:
            print("You win 😙")
        elif user_pick == 2 and computer_pick == 0:
            print("Computer wins 🙂")
        elif user_pick == 1 and computer_pick == 2:
            print("Computer wins 🙂")
        print(Fore.RESET)

    compare()
