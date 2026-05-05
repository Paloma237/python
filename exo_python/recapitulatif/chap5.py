#Chapitre 5 — Structures de données : Listes & Tuples
#Exercice 21 — Gestion d'une liste de tâches
#utilise switch case pour gérer les différentes options du menu
"""def gestion_taches():
    #on utilise une liste pour stocker les tâches
    taches = []
    while True:
        #on utilse switch case pour gérer les différentes options du menu
        print("\nMenu:")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        choix = input("Choisissez une option: ")
        if choix == '1':
            tache = input("Entrez la tâche à ajouter: ")
            taches.append(tache)
            print(f"Tâche '{tache}' ajoutée.")
        elif choix == '2':
            if not taches:
                print("Aucune tâche à afficher.")
            else:
                print("Tâches:")
                for i, tache in enumerate(taches, 1):
                    print(f"{i}. {tache}")
        elif choix == '3':  
            if not taches:
                print("Aucune tâche à supprimer.")
            else:
                try:
                    index = int(input("Entrez le numéro de la tâche à supprimer: "))
                    if 1 <= index <= len(taches):
                        tache_supprimee = taches.pop(index - 1)
                        print(f"Tâche '{tache_supprimee}' supprimée.")
                    else:
                        print("Numéro de tâche invalide.")
                except ValueError:
                    print("Veuillez entrer un numéro valide.")
        elif choix == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option du menu.")
gestion_taches()

#Exercice 22 — Tri et recherche
#Implémente le tri à bulles (bubble sort) sans utiliser sort() ou sorted()
#Implémente la recherche binaire sur une liste triée.
#Compare les performances en affichant le nombre de comparaisons effectuées.
def tri_bulles(liste):
    n = len(liste)
    comparaisons = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaisons += 1
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return comparaisons
def recherche_binaire(liste, cible):
    gauche, droite = 0, len(liste) - 1
    comparaisons = 0
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        comparaisons += 1
        if liste[milieu] == cible:
            return milieu, comparaisons
        elif liste[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1, comparaisons
nombres = [64, 34, 25, 12, 22, 11, 90]
comparaisons_tri = tri_bulles(nombres)
print(f"Liste triée: {nombres}")
print(f"Nombre de comparaisons pour le tri à bulles: {comparaisons_tri}")
cible = int(input("Entrez un nombre à rechercher dans la liste triée: "))
index, comparaisons_recherche = recherche_binaire(nombres, cible)
if index != -1:
    print(f"Nombre {cible} trouvé à l'index {index}.")
else:
    print(f"Nombre {cible} non trouvé dans la liste.")
print(f"Nombre de comparaisons pour la recherche binaire: {comparaisons_recherche}")

#Exercice 23 — Compréhension de listes avancée
#Génère la liste des carrés des nombres pairs de 1 à 20 en une seule ligne.
carrés_pairs = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"Carrés des nombres pairs de 1 à 20: {carrés_pairs}")
#Aplatit une liste de listes en une seule liste via une compréhension imbriquée.
listes = [[1, 2], [3, 4], [5, 6]]
aplatisse = [item for sous_liste in listes for item in sous_liste]
print(f"Liste de listes: {listes}")
print(f"Liste aplatie: {aplatisse}")
#Crée une matrice identité 4x4 avec une compréhension de liste
matrice_identite = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
print("Matrice identité 4x4:")
for ligne in matrice_identite:
    print(ligne)"""

#Exercice 24 — Coordonnées GPS avec tuples
#Représente des villes par des tuples (nom, latitude, longitude).
#Écris une fonction distance(ville1, ville2) utilisant la formule de Haversine.
#Trie les villes par distance croissante par rapport à une ville de référence.
import math
def haversine(coord1, coord2):
    R = 6371  # Rayon de la Terre en kilomètres
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c
villes = [
    ("Paris", 48.8566, 2.3522),
    ("Londres", 51.5074, -0.1278),
    ("New York", 40.7128, -74.0060),
    ("Tokyo", 35.6895, 139.6917)
]
ville_reference = ("Paris", 48.8566, 2.3522)
villes_triees = sorted(villes, key=lambda ville: haversine((ville[1], ville[2]), (ville_reference[1], ville_reference[2])))
print("Villes triées par distance croissante par rapport à Paris:")
for ville in villes_triees:
    distance = haversine((ville[1], ville[2]), (ville_reference[1], ville_reference[2]))
    print(f"paris-{ville[0]}: {distance:.2f} km")