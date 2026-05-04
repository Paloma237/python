#1) Fonction calculer_prix_ttc(prix, taux=0.19) avec valeur par défaut
def calculer_prix_ttc(prix, taux=0.19):
    prix_ttc = prix + (prix * taux)
    return prix_ttc
#2) Fonction verifier_stock(medicament, quantite) → True/False (anticipation du projet)
def verifier_stock(medicament, quantite):
    # Implementation for stock verification (simplified)
    return quantite > 0
#3) Utiliser datetime.date.today() → manipuler les dates comme Django (DateField)
import datetime
def afficher_date_prochaine():
    date_prochaine = datetime.date.today() + datetime.timedelta(days=1)
    print(f"La date prochaine est : {date_prochaine}")
#afficher la date d'hier
def afficher_date_hier():
    date_hier = datetime.date.today() - datetime.timedelta(days=1)
    print(f"La date d'hier était : {date_hier}")
# Test the functions
p = calculer_prix_ttc(200)
print(f"Le prix TTC est : {p:.2f}")
stock_disponible = verifier_stock("Paracétamol", 0)
print(f"Le stock de Paracétamol est disponible : {stock_disponible}")
afficher_date_prochaine()
afficher_date_hier()