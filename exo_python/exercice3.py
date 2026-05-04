#11. Booléens : Demandez deux valeurs True/False et affichez "Les deux sont vrais" si c'est le cas.
valeur1 = bool(input("Entrez une valeur booléenne (True/False) : "))
valeur2 = bool(input("Entrez une autre valeur booléenne (True/False) : "))
if valeur1==True and valeur2==True:
    print("Les deux sont vrais")
elif valeur1==False or valeur2==False:
    print("Au moins une des valeurs n'est pas vraie")
else:
    print("Les deux sont faux")