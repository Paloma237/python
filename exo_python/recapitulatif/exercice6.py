#chapitre2-structures conditionnelles 
#Exercice 6 — Mention au bac
"""def mention_bac():
    note=float(input("entrez votre note au bac: "))
    if note >=0 and note <=20:
        if note < 10:
            return "echec"
        elif note < 12:
            return "passable"
        elif note < 14:
            return "assez bien"
        elif note < 16:
            return "bien"
        else:
            return "très bien"
    else:
        return "note invalide entrer une note entre 0 et 20"
print("votre mention est:", mention_bac())

#Exercice 7 — Calculateur de l'IMC
def calculer_imc():
    taille=float(input("entrez votre taille en mètres: "))
    poids=float(input("entrez votre poids en kg: "))
    if taille > 0:
        imc=poids/(taille**2)
        if imc < 18.5:
            return "sous-poids"
        elif imc < 25:
            return "poids normal"
        elif imc < 30:
            return "surpoids"
        else:
            return "obésité"
    else:
        return "taille invalide entrer une taille positive"
print("votre état nutritionnel est:", calculer_imc())

#Exercice 8 — Jeu de devinette simple
import random
def jeu_devinette():
    nombre_secret=random.randint(1,100)
    essai=int(input("devinez le nombre secret entre 1 et 100: "))
    while True:
        if essai < nombre_secret:
            print("trop bas")
        elif essai > nombre_secret:
            print("trop haut")
        else:        
            print("félicitations! vous avez deviné le nombre secret")
            break
        essai=int(input("essayez à nouveau: "))
print(jeu_devinette())

#Exercice 9 — Système de tarification
def calculer_prix():
    # on applique une réduction de 20% pour un abonné
    abonne=input("êtes-vous abonné? (oui/non): ")
    age=int(input("entrez votre âge: "))
    if age < 0:
        return "âge invalide entrer un âge positif"
    if abonne.lower() == "oui":
        if age < 12:
            return "prix: 5€, réduction de 20% appliquée: 4€"
        elif age < 25:
            return "prix: 8€, réduction de 20% appliquée: 6.4€"
        elif age < 65:
            return "prix: 10€, réduction de 20% appliquée: 8€"
        else:
            return "prix: 6€, réduction de 20% appliquée: 4.8€"
    elif abonne.lower() == "non":
        if age < 12:
            return "prix: 5€"
        elif age < 25:
            return "prix: 8€"
        elif age < 65:
            return "prix: 10€"
        else:
            return "prix: 6€"
    else:
        return "réponse invalide entrer 'oui' ou 'non'"
print(calculer_prix())  """

#Exercice 10 — Validateur de triangle
def valider_triangle():
    a = float(input("Entrez la longueur du premier côté: "))
    b = float(input("Entrez la longueur du deuxième côté: "))
    c = float(input("Entrez la longueur du troisième côté: "))
    
    if a + b > c and a + c > b and b + c > a:
       print("Les longueurs saisies peuvent former un triangle.")
       # On peut aussi déterminer le type de triangle
       if a == b == c:
           return "C'est un triangle équilatéral."
       elif a == b or a == c or b == c:
           return "C'est un triangle isocèle."
       else:           
           return "C'est un triangle scalène."
    else:
        return "Les longueurs saisies ne peuvent pas former un triangle."
print(valider_triangle())
