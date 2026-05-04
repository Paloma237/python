#Chapitre 5 — Structures de données : Listes & Tuples
#Exercice 21 — Gestion d'une liste de tâches
#utilise switch case pour gérer les différentes options du menu
def gestion_taches():
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
#Implémente le tri à bulles (bubble sort) sans utiliser sort().
