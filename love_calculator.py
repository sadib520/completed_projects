from colorama import Fore

print(
    Fore.YELLOW
    + r"""

 _                      ____      _            _       _             
| |    _____   _____   / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |   / _ \ \ / / _ \ | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_) \ V /  __/ | |__| (_| | | (__| |_| | | (_| | || (_) | |   
|_____\___/ \_/ \___|  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

"""
    + Fore.RESET
)

print("Welcome to love calculator program !! ")
name1 = input("What is your name? ")
name2 = input("What is your lover name? ")

name = name1 + name2
lower_case = name.lower()

c = 0

for char in lower_case:
    if ("t") in char:
        c += 1
    elif ("r") in char:
        c += 1
    elif "u" in char:
        c += 1
    elif "e" in char:
        c += 1

c1 = 0
for char1 in lower_case:
    if ("l") in char1:
        c1 += 1
    if ("o") in char1:
        c1 += 1
    if ("v") in char1:
        c1 += 1
    if ("e") in char1:
        c1 += 1

print(Fore.GREEN + "Your love score is: " + str(c) + str(c1) + " %")
print(Fore.RESET)
