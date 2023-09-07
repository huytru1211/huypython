name_city= input("Please enter the name of city: ")
list= []
a=1
list.append(name_city)
while a<5:
    name_city= input("Please enter the name of city: ")
    a = a + 1
    list.append(name_city)
print(list)
for index, b in enumerate(list,start=1):
    print(f"{index}: {b}")



