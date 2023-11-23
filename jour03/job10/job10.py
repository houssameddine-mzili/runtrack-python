def verifier_nombre_pair_impair(nombre):
    """
    Cette fonction vérifie si un nombre est pair ou impair.
    Elle vérifie également si le nombre est un entier positif.
    """
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return f"Le nombre {nombre} est pair."
        else:
            return f"Le nombre {nombre} est impair."
    else:
        return "Veuillez entrer un chiffre entier positif."


resultats = [
    verifier_nombre_pair_impair(4),
    verifier_nombre_pair_impair(7),
    verifier_nombre_pair_impair(-3),
    verifier_nombre_pair_impair(15.5)
]

print(resultats)

