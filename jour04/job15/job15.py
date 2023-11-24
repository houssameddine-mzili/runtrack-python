def arrondir_et_trier(liste):
    def arrondir(nombre):
        partie_entiere = 0
        while nombre >= 1:
            nombre -= 1
            partie_entiere += 1
        if nombre >= 0.5:
            return partie_entiere + 1
        else:
            return partie_entiere

    liste_arrondie = [arrondir(nombre) for nombre in liste]

    def trier(liste):
        for i in range(len(liste)):
            for j in range(i, len(liste)):
                if liste[j] < liste[i]:
                    liste[i], liste[j] = liste[j], liste[i]
        return liste

    return trier(liste_arrondie)

liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

liste_triee = arrondir_et_trier(liste)
print(liste_triee)

