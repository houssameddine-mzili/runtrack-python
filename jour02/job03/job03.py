all_numbers = range(0, 101)
exclude_set = {26, 37, 88}  # Interdir le passage pour 26, 37, 88
numbers = (num for num in all_numbers if num not in exclude_set)

for num in numbers:
    print(num)
