for all_numbers in range(1, 101):
    result = ""
    if all_numbers % 3 == 0:
        result += "Fizz"
    if all_numbers % 5 == 0:
        result += "Buzz"
    if result == "":
        result = all_numbers
    print(result)
