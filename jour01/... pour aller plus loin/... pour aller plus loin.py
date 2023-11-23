# Script pour déterminer si une chaîne de caractères contient le caractère 'e' et combien de fois

def count_e(text):
    count = text.count('e')
    if count > 0:
        print(f"Le caractère 'e' apparaît {count} fois dans le texte.")
    else:
        print("Le caractère 'e' n'apparaît pas dans le texte.")
text = "Bleach CFYOW, également connu sous le nom de Can't Fear Your Own World, est une série de romans."
count_e(text)

