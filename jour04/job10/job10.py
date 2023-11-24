L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

produit = 1
for num in L:
    if 25 <= num <= 90:
        produit *= num

print(produit)