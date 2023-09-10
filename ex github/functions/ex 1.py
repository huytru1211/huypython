import random
def roll_dice():
    roll_dice= random.randint(1,6)
    return roll_dice
roll_no=0
while True:
    variable= roll_dice()
    print(f"Roll{roll_no}: {variable}")
    roll_no = roll_no + 1
    if variable==6:
        break







