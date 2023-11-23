#Programme Python pour générer une liste d'alphabets en utilisant les fonctions chr et ord
def print_alphabet():
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i), end=' ')
print_alphabet()
   
   