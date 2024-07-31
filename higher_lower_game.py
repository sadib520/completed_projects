from colorama import Fore
import random as rn
from higher_lower_game_data import data
from higher_lower_game_art import logo, vs, welcome


print(logo)
print()
print(welcome)

score = 0
game_continue = True
B = rn.choice(data)


def get_info(info_a, info_b):
    account_name_a = info_a["name"]
    account_des_a = info_a["description"]
    country_a = info_a["country"]

    account_name_b = info_b["name"]
    account_des_b = info_b["description"]
    country_b = info_b["country"]

    print(f"Compare A: {account_name_a}, a {account_des_a}, from {country_a}.")
    print(vs)
    print()
    print(f"Compare B: {account_name_b}, a {account_des_b}, from {country_b}.")


def Compare(comp_a, comp_b, guess):
    flag = True
    global score
    global game_continue
    check_followers_a = comp_a["follower_count"]
    check_followers_b = comp_b["follower_count"]

    if check_followers_a > check_followers_b and guess == "A":
        score += 1
    elif check_followers_b > check_followers_a and guess == "B":
        score += 1
    else:
        game_continue = False

    if check_followers_a > check_followers_b and guess == "B":
        print(
            Fore.RED
            + f"Wrong guess! game over !! final score: {score}".title()
            + Fore.RESET
        )
        game_continue = False
    elif check_followers_b > check_followers_a and guess == "A":
        print(
            Fore.RED
            + f"Wrong guess! game over !! final score: {score}".title()
            + Fore.RESET
        )
        game_continue = False
    else:
        print(Fore.GREEN + f"You're right. Current score: {score}" + Fore.RESET)


while game_continue:
    A = B
    B = rn.choice(data)

    while A == B:
        B = rn.choice(data)
    get_info(A, B)
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    Compare(A, B, guess)
