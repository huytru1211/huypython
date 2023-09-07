number=int(input("Please enter the number: "))
list= []
while True:
    if number == "":
        break
    number=float(number)
    list.append(number)
    number=input("Please enter the number: ")
reverse=sorted(list, reverse=True)
print(f" 5 biggest numbers are", reverse[:5])


