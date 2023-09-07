user_name=input("User name: ")
password=input("Password: ")
python=0
while python<5:
    python=python+1
    if user_name == "python" and password == "rules":
        print("Welcome")
        break
    elif user_name != "python" and password != "rules":
        print("Please type again")
        user_name = input("User name: ")
        password = input("Password: ")
if python == 5:
        print("Access denided")



