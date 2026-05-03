#1) Simuler une liste de médicaments (liste de dicts) : filtrer ceux dont stock < 10
medicaments = [
    {"nom": "Paracétamol", "stock": 5},
    {"nom": "Ibuprofène", "stock": 15},
    {"nom": "Aspirine", "stock": 8}
]
medicaments_bas_stock = [med for med in medicaments if med["stock"] < 10]
print("Médicaments avec un stock bas :")
for med in medicaments_bas_stock:
    print(f"- {med['nom']}: {med['stock']}")
    
#2) Dict comprehension : {nom: prix_ttc} à partir d'une liste de produits
"""calculer_prix_ttc(prod["prix"])
    produits = [
        {"nom": "Paracétamol", "prix": 10},
        {"nom": "Ibuprofène", "prix": 15},
        {"nom": "Aspirine", "prix": 8}
    ]
    prix_ttc = {prod["nom"]: calculer_prix_ttc(prod["prix"]) for prod in produits}
    print("Prix TTC des produits :")
    for nom, prix in prix_ttc.items():
        print(f"- {nom}: {prix:.2f}")"""
#3) Trier une liste de médicaments par prix avec sorted() + lambda → préfigure ORDER BY
medicaments_tries = sorted(medicaments, key=lambda x: x["stock"])
print("Médicaments triés par stock :")
for med in medicaments_tries:
    print(f"- {med['nom']}: {med['stock']}")