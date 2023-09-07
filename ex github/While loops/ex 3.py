numbers = input("Please enter your number here: ")
lowest = float(numbers)
highest = float(numbers)
while numbers != "":
    numbers = float(numbers)
    if numbers > highest:
        highest = numbers
    if numbers < lowest:
        lowest = numbers
    numbers = input("Please enter your number here: ")
print(f" the highest number is {highest:.2f}\n the lowest number is {lowest:.2f}")


