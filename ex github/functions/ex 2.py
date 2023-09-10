import random

number_side= int(input("Please enter the side number wanting to have on the roll dice: "))
def number_dice(variable):
    a=0
    while True:
        roll = random.randint(1, variable)
        a=a+1
        print(f"roll value{a}: {roll}")
        if(roll == variable):
            break

number_dice(number_side)