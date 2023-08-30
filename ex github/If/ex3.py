gender=input("Please enter your the biological gender: ")
hemo_value=a=float(input("Please enter your hemoglobin value: "))
if gender == "females":
    if a<117:
        print("The hemoglobin value is low")
    elif a>155:
        print("The hemoglobin value is high")
    else:
        print("The hemoglobin value is normal" )
else:
    if gender == "males" and a<134:
        print("The hemoglobin value is low")
    elif a>167:
        print("The hemoglobin value is high")
    else:
        print("The hemoglobin value is normal")



