while True:
    try:
        interger = int(input("Please enter an interger number: "))
        if interger <=0:
            print("Invalid value")
            break
        factorial=1
        for index in range(1,interger+1):
            factorial=factorial*index
            # 1
            # 1*2
            # 1*2*3
            # 1*2*3*4
        print(f"the factorial number of {interger} is {factorial}")
    except ValueError:
        print("You have type empty or not number")










