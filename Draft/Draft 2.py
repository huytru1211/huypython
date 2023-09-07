while True:
    interger_no= int(input("Please enter an interger number: "))
    if interger_no <= 0:
        break
    factorial = 1
    new = 1
    while new<= interger_no:
        factorial= factorial*new
        new=new+1
    print(f"The factorial number {interger_no} is {factorial}")
print("Thanks and bye")


