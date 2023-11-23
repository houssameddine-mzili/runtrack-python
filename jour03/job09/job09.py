def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

note1 = float(input("Entrez un chiffre:" ))
note2 = float(input("Entrez un chiffre:" ))
note3 = float(input("Entrez un chiffre:" ))
moyenne_etudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_etudiant <= 20:
    message = "Très bon élève"
elif 11 <= moyenne_etudiant < 15:
    message = "Bon élève"
elif 8 <= moyenne_etudiant < 11:
    message = "Élève moyen"
elif 0 <= moyenne_etudiant < 8:
    message = "Élève devant faire des efforts"
else:
    message = "Moyenne invalide"

print(moyenne_etudiant, message)

