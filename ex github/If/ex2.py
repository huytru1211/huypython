cabin_class = input("Please enter the cabin class (LUX,A,B or C): ")

if cabin_class =="LUX" :
        print("Welcome to Lux, it is an upper-deck cabin with a balcony. ")

elif cabin_class == "A":
        print("Welcome to class A, it is above the car deck and equipped with a window.")

elif cabin_class == "B":
        print("Welcome to class B, it is a windowless cabin above the car deck.")

elif cabin_class == "C":
        print("Welcome to class C, it is a a windowless cabin below the car deck.")

else:
        print("Invalid cabin class. Please enter LUX, A, B, or C.")
