import random
number_random= random.randint(1,100)
player_guess=101
while player_guess!=number_random:
    player_guess= int(input("Please guess a number in 1-100: "))
    if player_guess > number_random:
        print("Your guess NO is higher bro!!")
    elif player_guess < number_random:
        print("Your guess NO is lower bro")
    else:
        print("Correct, gud job!!!!")






