#Chapitre 4 — Fonctions
#Exercice 16 — Convertisseur de températures
"""def celsius_vers_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_vers_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celcius_vers_kelvin(celsius):   
    return celsius + 273.15
celsius=float(input("entrez une température en degrés Celsius: "))
print(f"{celsius}°C = {celsius_vers_fahrenheit(celsius)}°F")
print(f"{celsius}°C = {celcius_vers_kelvin(celsius)}K")
fahrenheit=float(input("entrez une température en degrés Fahrenheit: "))
print(f"{fahrenheit}°F = {fahrenheit_vers_celsius(fahrenheit)}°C")

#Exercice 17 — Fonction récursive — Puissance
def puissance(base, exposant):
    if exposant == 0:
        return 1
    elif exposant < 0:
        return 1 / puissance(base, -exposant)
    else:
        return base * puissance(base, exposant - 1)
    
print(puissance(2, 3))
print(puissance(5, -2))
print(puissance(3, 0))

#Exercice 18 — Fonctions avec *args et **kwargs
def statistiques(*args, **kwargs):
    if not args:
        print("Aucun nombre fourni.")
        return
    moyenne = sum(args) / len(args)
    minimum = min(args)
    maximum = max(args)
    print(f"Moyenne: {moyenne}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
statistiques(10, 20, 30,a=5,b="exemple",c=True)

#Exercice 19 — Fonctions lambda et map
#Utilise une fonction lambda pour doubler chaque élément d'une liste
nombres = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x * 2, nombres))
print(doubles)
#Utilise filter() avec un lambda pour garder uniquement les nombres pairs d'une liste.
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)
#Utilise sorted() avec un lambda pour trier des tuples par leur premier élément
tuples = [(3, 'b',1), (2, 'a',3), (0, 'c',2)]
sorted_tuples = sorted(tuples, key=lambda x: x[2])
print(sorted_tuples)"""


#Exercice 20 — Décorateur de chronomètre
import time
def chronometre(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Temps d'exécution de {func.__name__}: {end_time - start_time:.4f} secondes")
        return result
    return wrapper
@chronometre
def calculer_somme(n):
    return sum(range(1, n + 1))
print(calculer_somme(1000000))