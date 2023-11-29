import random

def generate_combination(digits, min_value, max_value):
    combination = []
    for _ in range(digits):
        digit = random.randint(min_value, max_value)
        combination.append(str(digit))
    return combination
combination1 = generate_combination(3, 0, 9)
combination2 = generate_combination(4, 1, 6)
print("Combination 1:", ''.join(combination1))
print("Combination 2:", ''.join(combination2))
