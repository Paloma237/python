#Dictionnaires (CRUD, .keys(), .values(), .items(), .get()), sets (union, intersection, différence), dict comprehensions
#1) Annuaire téléphonique (ajouter/rechercher/supprimer)
annuaire = {}
def ajouter_contact(nom, numero):
    annuaire[nom] = numero  
    print(f"Contact '{nom}' ajouté avec le numéro {numero}")    
def rechercher_contact(nom):
    return annuaire.get(nom, "Contact non trouvé")
def supprimer_contact(nom):
    if nom in annuaire:
        del annuaire[nom]
        return f"Contact '{nom}' supprimé"
    else:
        return "Contact non trouvé"
#exemple d'utilisation
ajouter_contact("Alice", "123-456-7890")
ajouter_contact("Bob", "987-654-3210")
print(rechercher_contact("Alice"))  # "123-