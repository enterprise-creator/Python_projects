import random

roll_dice = input("Do you want to roll the dice? ")

while roll_dice.lower() == 'yes' or roll_dice.lower() == 'y':

    n1 = random.randint(1,6)
    n2 = random.randint(1,6)

    print(f"Your numbers are {n1} & {n2}")

    roll_dice = input("Do you want to roll again? ")

