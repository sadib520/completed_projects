import random
from colorama import Fore
from Blackjack_game_art import logo


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(
    cards,
):  # we will be passing user_cards and computer cards one by one as cards and get the user score and computer score
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def play_blackjack():

    user_cards = []
    computer_cards = []
    flag = True
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while flag:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Current_score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            flag = False
        else:
            another_card = input(
                Fore.CYAN + "Type 'y' to add another card or 'n' to pass: " + Fore.RESET
            )
        if another_card == "y":
            user_cards.append(deal_cards())
        else:
            flag = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    compare(user_score, computer_score)
    print(
        f"Dealer cards are: {computer_cards}, Dealer_score: {computer_score}"
        + Fore.RESET
    )


def compare(user_score, computer_score):
    print(Fore.GREEN)
    if user_score == computer_score:
        print("Draw 🤨" + Fore.RESET)
    elif user_score == 0:
        print("Win! with a blackjack. 🤑" + Fore.RESET)
    elif computer_score == 0:
        print("Lose, opponent has blackjack. 🙁" + Fore.RESET)
    elif user_score > 21 and computer_score < 21:
        print("Dealer wins 🥱" + Fore.RESET)
    elif computer_score > 21 and user_score < 21:
        print("You win 🤑" + Fore.RESET)
    elif user_score > computer_score and user_score < 21:
        print("You win 🤑" + Fore.RESET)
    elif computer_score > user_score and computer_score < 21:
        print("Dealer wins 🥱" + Fore.RESET)
    elif computer_score == 21:
        print("Lose, opponent has blackjack. 🙁" + Fore.RESET)
    elif user_score == 21:
        print("Win! with a blackjack. 🤑" + Fore.RESET)
    elif user_score > 21 and computer_score > 21:
        print("Nobody wins. Game over !! 🤨" + Fore.RESET)


play_blackjack()
