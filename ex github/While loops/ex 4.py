import random
guess_no = int(input("Please enter your number here: "))
number_random= random.randint(1,10)
while guess_no != number_random:
    if guess_no > number_random:
        print("It's too high, please guess again.")
        guess_no = int(input("Please enter your number here: "))
    elif guess_no < number_random:
        print("It's too low, please guess again")
        guess_no = int(input("Please enter your number here: "))
if guess_no == number_random:
    print("Correct")









