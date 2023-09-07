import random
dice= int(input("Enter your number of dice you want to roll: "))
total_sum=0
for _ in  range(dice):
    number_random = random.randint(1,6)
    total_sum=total_sum+number_random
print(f"Sum of {dice} dice rolls is {total_sum}")




