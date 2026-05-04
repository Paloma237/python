#Exercice 3 — Opérateurs de comparaison
def verifier_eligibilite():
    age=int(input("entrez votre âge: "))
    salaire=float(input("entrez votre salaire: "))
    anciennete=int(input("entrez votre ancienneté en années: "))
    if age >= 30 and salaire < 50000 and anciennete > 5:
        return True
    else:
        return False
p=verifier_eligibilite()
print("Éligible à la promotion :", p)