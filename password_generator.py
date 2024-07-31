from colorama import Fore
import random

# Unique advanced password generator program


letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "Q",
    "W",
    "E",
    "R",
    "T",
    "Y",
    "U",
    "I",
    "O",
    "P",
    "A",
    "S",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "B",
    "V",
    "C",
    "X",
    "Z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "&", "*", "_", "^"]

print(Fore.YELLOW + "Welcome to Py_password generator !" + Fore.RESET)
platform = input("For which platform you're generating the password:\n")
l = int(input("How many letters would you like in your password?\n"))
n = int(input("How many numbers would you like in your password?\n"))
s = int(input("How many symbols would you like in your password?\n"))

# passwd = ""  #this is an empty string. we can store sting value in it
passwd = []
for _ in range(1, l + 1):
    a = random.choice(letters)
    passwd += a

for _ in range(1, n + 1):
    b = random.choice(numbers)
    passwd += b

for _ in range(1, s + 1):
    c = random.choice(symbols)
    passwd += c

random.shuffle(passwd)

password = ""
for char in passwd:
    password += char
print(Fore.GREEN + f"Your password for {platform} is: {password}" + Fore.RESET)
with open("password_save.txt", mode="a") as file:
    file.write(f"{platform} password: {password}\n")
