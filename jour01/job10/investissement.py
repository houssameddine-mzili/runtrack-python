# Initialisation des variables
montant_initial = float(input("Entrez le montant initial de l'investissement: "))
taux_rendement = float(input("Entrez le taux de rendement annuel (en %): "))

# Calcul du gain annuel initial
gain_annuel_initial = montant_initial * taux_rendement / 100
print(f"Gain annuel initial: {gain_annuel_initial} euros")

# Mise à jour du capital et du taux de rendement
montant_initial += 5000  
taux_rendement += 2  

# Calcul du nouveau gain annuel
nouveau_gain_annuel = montant_initial * taux_rendement / 100
print(f"Nouveau gain annuel: {nouveau_gain_annuel} euros")

# Retrait de 10% du montant total et diminution du taux de rendement de 1%
montant_apres_retrait = montant_initial - (montant_initial * 10 / 100)
taux_rendement -= 1  

# Calcul du montant final de l'investissement et du nouveau gain
montant_final = montant_apres_retrait * (1 + taux_rendement / 100)
nouveau_gain = montant_final - montant_apres_retrait
print(f"Montant final de l'investissement: {montant_final} euros")
print(f"Nouveau gain après retrait: {nouveau_gain} euros")
