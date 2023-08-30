year=int(input("Please enter the year which is a leap year: "))
if year%4==0 or year%100==0 and year%400==0:
    print("This is a leap year")
else:
    print ("This is not a leap year")

