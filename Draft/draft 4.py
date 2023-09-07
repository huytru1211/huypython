number=float(input("Please enter a number: "))
list=[]
while True:
        if number>0:
            list.append(number)
            number = float(input("Please enter a number: "))
        else:
            print(list)
            break




