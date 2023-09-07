shop= []
item= input("Please enter your shopping list: ")
shop.append(item)
while True:
    item = input("Please enter your shopping list: ")
    if item == "done":
        break
    shop.append(item)
print("Your shopping list:\n")
for index, item in enumerate(shop,start=1):
    print(f"{index}: {item}")



