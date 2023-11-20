# Classe pour gérer l'inventaire de produits
class Inventaire:
    def __init__(self, nom, prix_unitaire, quantite_en_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_en_stock = quantite_en_stock

    def afficher_informations(self):
        print(f"Produit: {self.nom}\n"
              f"Prix unitaire: {self.prix_unitaire:.2f} €\n"
              f"Quantité en stock: {self.quantite_en_stock}")

    def ajouter_stock(self, quantite):
        self.quantite_en_stock += quantite

    def vendre(self, quantite):
        if quantite <= self.quantite_en_stock:
            self.quantite_en_stock -= quantite
            print(f"{quantite} unité(s) de {self.nom} vendue(s).")
        else:
            print(f"Stock insuffisant. Il reste seulement {self.quantite_en_stock} unité(s) en stock.")

    def appliquer_inflation(self, pourcentage):
        self.prix_unitaire *= (1 + pourcentage / 100)

# Création d'un produit dans l'inventaire
produit = Inventaire("Ducky Channel One 2 Mini", 229.95, 300)

# Affichage informations du produit
produit.afficher_informations()

# Ajout de stock
produit.ajouter_stock(210)

# Vente de produits
quantite_achat = 120  # Quantité souhaitée par l'utilisateur
produit.vendre(quantite_achat)
produit.appliquer_inflation(10)
produit.afficher_informations()
