#Programme Python pour générer une liste d'alphabets à l'envers
def print_alphabet_reversed():
    for i in range(ord('z'), ord('a') - 1, -1):
        print(chr(i), end=' ')
print_alphabet_reversed()