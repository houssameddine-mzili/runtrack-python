string = "abcdefghijklmnopqrstuvwxyz" * 20

pyramid = ""
row_length = 1
current_index = 0

while current_index + row_length <= len(string):
    pyramid += string[current_index:current_index + row_length] + "\n"
    current_index += row_length
    row_length += 1

print(pyramid)
