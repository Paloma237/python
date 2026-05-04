#Exercice 1 — Calculatrice de base
def calculatrice():
    a=float(input("entrer un nombre: "))
    b=float(input("entrer un autre nombre: "))
    print(f"somme : {a+b}")
    print(f"différence : {a-b}")
    print(f"produit: {a*b}")
    if b == 0:
        print("division par zéro impossible")
    else:
        print(f"quotient: {a/b}")
        print(f"quotient entier: {a//b}")
        print(f"reste: {a%b}")
        
calculatrice()