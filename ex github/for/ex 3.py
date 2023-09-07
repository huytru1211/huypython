number= int(input("Please enter your number: "))
a=0
for i in range(1,number):
    if number%i==0:
        a=a+1
    else:
        a=a
if a==1:
    print("This is a prime number")
else:
    print("This is not a prime number")






