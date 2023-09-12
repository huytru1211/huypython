def remove_odd_numbers(input_list):
    return [x for x in input_list if x % 2 == 0]

# Creating a list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calling the function to remove odd numbers
modified_list = remove_odd_numbers(original_list)

# Printing the original and modified lists
print("Original List:", original_list)
print("Modified List (odd numbers removed):", modified_list)