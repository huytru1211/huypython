thistuple= ("Spring","Summer","Autumn","Winter")
while True:
    for x in thistuple:
        month = int(input("Please enter a month here: "))
        if 3 <= month <= 5:
            print(f"{thistuple[0]}")
        elif 6 <= month <= 8:
            print(f"{thistuple[1]}")
        elif 9 <= month <= 11:
            print(f"{thistuple[2]}")
        else:
            print(f"{thistuple[-1]}")





