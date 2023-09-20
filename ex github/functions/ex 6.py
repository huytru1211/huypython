import math
diameter1= float(input("Please enter the diameter of pizza 1 in centimeter: "))
diameter2= float(input("Please enter the diameter of pizza 2 in centimeter: "))
price1= float(input("Please enter the price of pizza 1: "))
price2= float(input("Please enter the price of pizza 2: "))
def number1(x):
    S1= math.pi * (diameter1/2)**2
    S1=S1*0.0001
    money1= price1/S1
    return money1

def number2(y):
    S2 = math.pi * (diameter2 / 2) ** 2
    S2 = S2 * 0.0001
    money2=price2/S2
    return money2

money1=number1(price1)
money2=number2(price2)
if money1>money2:
    print("The pizza 1 is more expensive than the pizza 2")
elif money2>money1:
    print("The pizza 2 is more expensive than the pizza 1")
else:
    print("Both pizza have the same value")












