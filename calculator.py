from colorama import Fore

print(
    Fore.GREEN
    + r"""
 _____________________
|  _________________  |
| | SH           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

(Regular Calculator)
"""
    + Fore.RESET
)


print("welcome to py calculator program !! ".title())


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return round(n1 / n2, 4)


dict = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    num1 = float(input("Enter first number: "))
    for operation in dict:
        print(operation)
    flag = True
    while flag:
        dict_symbol = input("pick an operation from the line above: ")
        num2 = float(input("Enter next number: "))
        get_value_dict = dict[
            dict_symbol
        ]  # get the value; not key => from the dictionary
        answer = get_value_dict(num1, num2)
        print(f"{num1 } { dict_symbol} {num2} = {answer}")

        again = input(
            f"Type 'y' if you want to go with {answer} or type 'n' to start new calculation or type 'q' to quit: "
        ).lower()
        if again == "y":
            num1 = answer
            for operation in dict:
                print(operation)
        elif again == "q":
            flag = False
            exit()
        if again == "n":
            flag = False
            calculator()


calculator()
