from colorama import Fore

print(Fore.GREEN + "Welcome to BMI calculator program !! ".title() + Fore.RESET)

weight = int(input("Enter your weight : "))
if weight == 0 or weight < 0:
    print("Weight cant be zero nor negative.")
    exit()

height = int(input("Enter your height in ft. "))
inch = int(input("what about inch. "))
if height != 0 and inch != 0:
    height_in_meter = (height * 0.3048) + (inch * 0.0254)

bmi = (weight) / (height_in_meter * height_in_meter)

if bmi < 18.5:
    print("you are underweight: " + str(round(bmi, 4)))
elif bmi > 18.5 and bmi <= 25:
    print("Your BMI is normal: " + str(round(bmi, 4)))
elif bmi > 25 and bmi < 30:
    print("You are oversized: " + str(round(bmi, 4)))
