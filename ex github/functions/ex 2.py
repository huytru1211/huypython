import random
def number_dice(number):
    roll = random.randint(1, number)
    return roll
number_side= int(input("Please enter the side number wanting to have on the roll dice: "))
a=0
while True:
    result = number_dice(number_side)
    a=a+1
    print(f"roll {a}: {result}")
    if result == number_side:
        break
