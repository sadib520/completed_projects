from colorama import Fore
from ceaser_art import logo

# print(f"{logo}{Fore.RESET}")

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
]  # an interesting encryption and decryption algorithm by ceaser cipher


print(Fore.RESET + "Welcome to ceaser-cipher encryption algorithm ~ !! ")
should_continue = True
while should_continue:

    type = input("Type 'encode' to encrypt, or type 'decode' to decrypt: \n").lower()
    msg = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    def encrypt(plain_msg, shift_amount):
        cypher = ""
        end = ""
        for char in plain_msg:
            if char in letters:
                position = letters.index(char)
                new_position = (position + shift_amount) % 26
                new_char = letters[new_position]
                cypher += new_char
            else:
                end += char
        print(Fore.GREEN + f"Your encrypted message is: {cypher}{end}" + Fore.RESET)

    def decrypt(plain_msg1, shift_amount1):
        cypher1 = ""
        end = ""
        for char in plain_msg1:
            if char in letters:
                position1 = letters.index(char)
                new_position1 = (position1 - shift_amount1) % 26
                new_char1 = letters[new_position1]
                cypher1 += new_char1
            else:
                end += char
        print(Fore.GREEN + f"Your decrypted message is: {cypher1}{end}" + Fore.RESET)

    if type == "encode":
        encrypt(plain_msg=msg, shift_amount=shift)
    elif type == "decode":
        decrypt(plain_msg1=msg, shift_amount1=shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
    if result == "no":
        should_continue = False
        print(Fore.RED + "Thank you, stay cool. " + Fore.RESET)
