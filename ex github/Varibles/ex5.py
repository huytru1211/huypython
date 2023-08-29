talent_to_pound  = 20
pound_to_lot  = 32
lot_to_gram = 13.3
talents = a = int(input("Enter the number of talents: "))
pounds = b = int(input("Enter the number of pounds: "))
lots = c = float(input("Enter the number of lots: "))
grams= a*20*32*13.3 + b*32*13.3 + c*13.3
kilograms = grams / 1000
grams %= 1000
print("The mass is equivalent to", kilograms, "kilograms and", grams, "grams.")

