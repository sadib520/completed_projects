import random

print("Welcome to the guessing game ! ")
top = input("Enter top range of the number: ")

if top.isdigit():
    top = int(top)
else:
    print("Negative number and strings are not allowed !")
    exit()

if top == 0:
    print("Range should be greater than zero")
    exit()


r = random.randint(1, top + 1)

while True:
    user_guess = int(input("Make a guess: "))
    if user_guess == r:
        print("You got it !")
        break
    elif user_guess < 0 or user_guess == 0:
        print("Number should be greater than 0")
    elif user_guess not in range(1, top + 1):
        print(f"Number is out of range ")
    else:
        print("You got it wrong !")
