#Chapitre 7 — Programmation Orientée Objet (POO)
#Exercice 31 — Classe Compte Bancaire
"""class CompteBancaire:
    #Crée une classe CompteBancaire avec les attributs privés : __titulaire, __solde.
    def __init__(self, titulaire, solde=0):
        self.__titulaire = titulaire
        self.__solde = solde
    #implémente les méthodes : deposer(), retirer(), afficher_solde(),et_str_().
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"{montant}€ déposés. Nouveau solde: {self.__solde}€.")
        else:
            print("Le montant à déposer doit être positif.")
    def retirer(self, montant):
        if montant > self.__solde:
            print(" désolé, votre fonds est insuffisants pour ce retrait.")
        elif montant <= 0:
            print("Le montant à retirer doit être positif.")
        else:
            self.__solde -= montant
            print(f"{montant}€ retirés. Nouveau solde: {self.__solde}€.")
    def afficher_solde(self):
        print(f"Titulaire: {self.__titulaire}, Solde: {self.__solde}€.")
    def __str__(self):
        return f"CompteBancaire(titulaire='{self.__titulaire}', solde={self.__solde}€)"
compte = CompteBancaire("Alice", 1000)
print(compte)
deposer=int(input("Entrez le montant à déposer: "))
compte.deposer(deposer)
retirer=int(input("Entrez le montant à retirer: "))
compte.retirer(retirer)
compte.afficher_solde()

#Exercice 32 — Héritage — Catalogue Véhicules
#Crée une classe mère Vehicule avec : marque, modele, annee, prix.
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    def description(self):
        return f"Véhicule: {self.marque} {self.modele} ({self.annee}), Prix: {self.prix}€"
#Crée les sous-classes Voiture (nb_portes), Moto (type_guidon), Camion (charge_max).
#Chaque classe a une méthode description() qui utilise super() et ajoute ses propres infos.
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, nb_portes):
        super().__init__(marque, modele, annee, prix)
        self.nb_portes = nb_portes
    def description(self):
        return f"Voiture: {self.marque} {self.modele} ({self.annee}), Prix: {self.prix}€, Portes: {self.nb_portes}"
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, type_guidon):
        super().__init__(marque, modele, annee, prix)
        self.type_guidon = type_guidon
    def description(self):
        return f"Moto: {self.marque} {self.modele} ({self.annee}), Prix: {self.prix}€, Type de guidon: {self.type_guidon}"
class Camion(Vehicule):
    def __init__(self, marque, modele, annee, prix, charge_max):
        super().__init__(marque, modele, annee, prix)
        self.charge_max = charge_max
    def description(self):
        return f"Camion: {self.marque} {self.modele} ({self.annee}), Prix: {self.prix}€, Charge maximale: {self.charge_max} tonnes"
voiture = Voiture("Toyota", "Corolla", 2020, 20000, 4)
moto = Moto("Honda", "CBR600RR", 2019, 12000, "Sport")
camion = Camion("Volvo", "FH16", 2018, 80000, 25)
print(voiture.description())
print(moto.description())
print(camion.description())

#Exercice 33 — Méthodes spéciales (Dunder methods)
#Crée une classe Vecteur2D représentant un vecteur mathématique (x, y).
class vecteur2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #implémente les méthodes : __add__, __sub__, __mul__ (scalaire), __abs__ (norme), __eq__, __repr__.
    def __add__(self, other):
        return vecteur2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return vecteur2D(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        return vecteur2D(self.x * scalar, self.y * scalar)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"vecteur2D(x={self.x}, y={self.y})"
#Teste toutes les opérations entre vecteurs.
v1 = vecteur2D(3, 4)
v2 = vecteur2D(1, 2)
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"|v1|: {abs(v1)}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == vecteur2D(3, 4): {v1 == vecteur2D(3, 4)}")"""

#Exercice 34 — Classe abstraite — Formes géométriques
#Utilise le module abc pour créer une classe abstraite Forme avec les méthodes abstraites aire() et perimetre().
from abc import abstractmethod


class Forme:
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass
#Implémente les sous-classes : Cercle, Rectangle, Triangle.
import math
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)
class Triangle(Forme):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def aire(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetre(self):
        return self.a + self.b + self.c
#Crée une liste de formes et affiche l'aire et le périmètre de chacune de façon polymorphique.
formes = [
    Cercle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]
for forme in formes:
    print(f"{forme.__class__.__name__} - Aire: {forme.aire():.2f}, Périmètre: {forme.perimetre():.2f}")
    