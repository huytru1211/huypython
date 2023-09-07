while True:
    inches=float(input("Please enter a length inches including a negative value: "))
    if inches < 0:
        print("the program is end")
        break
    else:
        centimeters= inches*2.54
        print(f" your length converts to centimeters is {centimeters}" )




