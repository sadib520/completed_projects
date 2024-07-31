from colorama import Fore

print(
    Fore.YELLOW
    + r"""
 _____ _          ____      _            _       _             
|_   _(_)_ __    / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
  | | | | '_ \  | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | | | | |_) | | |__| (_| | | (__| |_| | | (_| | || (_) | |   
  |_| |_| .__/   \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
        |_|                                                    """
    + Fore.RESET
)

print("Welcome to tip calculator program !! ")


bill = float(input("What was the  total bill? $ "))
tip = int(input("What percentage tip would you like to give? $ 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

if bill != 0 and people != 0 and tip in (10, 12, 15):
    total_bill = bill + ((tip / 100) * bill)
    pay = total_bill / people
    print("Each person should pay: $" + str(round(pay, 2)))
else:
    print("Something's wrong triggered. Try again. ")
