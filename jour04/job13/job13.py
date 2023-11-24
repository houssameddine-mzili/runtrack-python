liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

liste_sans_doublons = []
for element in liste:
    if element not in liste_sans_doublons:
        liste_sans_doublons.append(element)

print(liste_sans_doublons)

