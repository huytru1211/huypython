def number(even_number):
    return[x for x in even_number if x%2==0]
list_of_interger= [1,2,3,4,5,6,7,8,9,10,11,12]
result = number(list_of_interger)
print(f"The even numbers are {result}")
print(f"The original list: {list_of_interger}")


    