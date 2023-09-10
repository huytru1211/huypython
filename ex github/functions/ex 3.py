def volume_liters(x):
    liters = gallon*3.7854
    return liters
while True:
    gallon= int(input("Enter volume in gallon: "))
    result=volume_liters(gallon)
    if result>0:
        print(f"the volume converts from {gallon} gallon to liters is {result} liters: ")
    else:
        result<0
        print("Invalid value")
        break