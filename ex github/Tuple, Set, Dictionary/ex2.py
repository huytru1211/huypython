# namelist= set()
# name = input("Enter your name: ")
# def list(name):
#     while True:
#         if name != "":
#             if name in namelist:
#                 print("It is already exist in the list")
#             else:
#                 namelist.add(name)
#                 print(f"{name} is added")
#                 print(f"The name has been typed: {namelist}")
#             name = input("Enter your name: ")
#         else:
#             print(f"Here the list {namelist}")
# list(name)

namelist= set()
name = input("Enter your name: ")
def list(name):
    while True:
        if name != "":
            if name in namelist:
                print("Existing name")
            else:
                namelist.add(name)
                print(f"{name} is a new name")
            name= input("Enter your name")
        else:
            print(f"Here the list: {namelist}")
            break
list(name)








