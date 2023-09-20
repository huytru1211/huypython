airportlist= {}
while True:
    print("1. Enter a new airport: ")
    print("2. Fetch your airport information: ")
    print("3. Quit")

    airport = input("Please choose an option (1/2/3): ")
    if airport == "1":
        ICAO= input("Enter the ICAO code: ")
        nameairport = input("Airport name: ")
        airportlist[ICAO]= nameairport
        print("Adding success")
    elif airport == "2":
        askIcao= input("Enter the ICAO code you want to find: ")
        print(f"Airport name: {airportlist[askIcao]}")
    elif airport == "3":
        print("Good bye")
        break
    else:
        print("Please choose again, the number is not value: ")





