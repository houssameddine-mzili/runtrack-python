try:
    number_N = int(input("Entrez un entier supérieur à zéro (N): "))
    if number_N <= 0:
        print("Le nombre doit être supérieur à zéro. Veuillez réessayer.")
    else:
        for i in range(1, 11):
            print(number_N, 'x', i, '=', number_N * i)
except ValueError:
    print("Entrée invalide. Veuillez entrer un nombre entier.")
