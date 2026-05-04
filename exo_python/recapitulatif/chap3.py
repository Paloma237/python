#Chapitre 3 — Boucles for & while
#Exercice 11 — Table de multiplication
def table_multiplication(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
nombre=int(input("entrez un nombre pour afficher sa table de multiplication: "))
table_multiplication(nombre)

#Exercice 12 — Nombre de Fibonacci
n=int(input("entrez le nombre de termes de la suite de Fibonacci à afficher: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()


"""#Exercice 13 — Pyramide d'étoiles
n=int(input("entrez le nombre de lignes pour la pyramide d'étoiles: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    #maintenant on peut aussi faire une pyramide inversée
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1)) 
    
#Exercice 14 — Vérification de palindrome
chaine=input("entrez une chaîne de caractères à vérifier: ")
#on vérifie c   r   ctère par caractère sans utiliser de fonctions intégrées
def est_palindrome(s):
    s = s.replace(" ", "").lower()  # on ignore les espaces et la casse
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True
if est_palindrome(chaine):
    print(f"'{chaine}' est un palindrome.")
else:
    print(f"'{chaine}' n'est pas un palindrome.")

#Exercice 15 — Calculateur de factorielle avec garde-fou
def calculer_factorielle():
    n = int(input("Entrez un nombre entier pour calculer sa factorielle: "))
    if n < 0:
        return "Erreur: la factorielle n'est pas définie pour les nombres négatifs."
    elif n == 0 or n == 1:
        return "La factorielle de 0 ou 1 est 1."
    else:
    #Calcule n! avec une boucle while (sans utiliser math.factorial).
        result = 1
        i = 2
        while i <= n:
            result *= i
            i += 1
        return f"{n}! = {result}."
print(calculer_factorielle())"""11