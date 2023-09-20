names_set = set()

# Create a loop to continuously ask for names until an empty string is entered
while True:
    name = input("Enter a name (or press Enter to exit): ")

    # Check if the entered name is empty
    if name == "":
        break

    # Check if the name is already in the set
    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

# Print out the input names one by one
print("\nList of input names:")
for name in names_set:
    print(name)









