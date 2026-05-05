#Chapitre 6 — Dictionnaires & Ensembles
#Exercice 27 — Compteur de fréquence de mots
#Demande une phrase à l'utilisateur.
#Compte la fréquence de chaque mot (insensible à la casse, sans ponctuation).
#Affiche les 5 mots les plus fréquents avec leur nombre d'occurrences.
phrase = input("Entrez une phrase: ")
mots = phrase.lower().split()
frequence = {}
for mot in mots:
    mot = mot.strip(".,;:!?")
    frequence[mot] = frequence.get(mot, 0) + 1
mots_tries = sorted(frequence.items(), key=lambda x: x[1], reverse=True)
print("Les 5 mots les plus fréquents:")
for i, (mot, count) in enumerate(mots_tries[:5]):
    print(f"{i+1}. {mot}: {count}")
    
#Exercice 28 — Opérations sur les ensembles
#Crée deux ensembles représentant des compétences de deux développeurs.
#Calcule et affiche : compétences communes (intersection), compétences de l'un mais pas de
#l'autre (différence), toutes les compétences (union), compétences exclusives (différence
#symétrique).
dev1 = {"Python", "JavaScript", "SQL", "Docker"}
dev2 = {"Python", "Java", "Kubernetes", "Docker"}
intersection = dev1.intersection(dev2)
difference_dev1 = dev1.difference(dev2)
difference_dev2 = dev2.difference(dev1)
union = dev1.union(dev2)
difference_symetrique = dev1.symmetric_difference(dev2)
print(f"Compétences communes: {intersection}")
print(f"Compétences de dev1 mais pas dev2: {difference_dev1}")
print(f"Compétences de dev2 mais pas dev1: {difference_dev2}")
print(f"Toutes les compétences: {union}")
print(f"Compétences exclusives: {difference_symetrique}")

#Exercice 29 — Dictionnaire imbriqué — École
#Crée un dictionnaire représentant une école avec des classes, des élèves et leurs notes.
#Écris une fonction moyenne_classe(classe) qui calcule la moyenne de chaque élève.
#Trouve l'élève avec la meilleure moyenne globale.
ecole = {
    "Classe A": {
        "Alice": [85, 90, 78],
        "Bob": [92, 88, 95],
        "Charlie": [70, 75, 80]
    },
    "Classe B": {
        "David": [88, 82, 91],
        "Eve": [95, 94, 98],
        "Frank": [80, 85, 87]
    }
}
def moyenne_classe(classe):
    moyennes = {}
    for eleve, notes in classe.items():
        moyennes[eleve] = sum(notes) / len(notes)
    return moyennes
meilleure_moyenne = 0
meilleur_eleve = ""
for classe, eleves in ecole.items():
    moyennes = moyenne_classe(eleves)
    print(f"Moyennes de {classe}: {moyennes}")
    for eleve, moyenne in moyennes.items():
        if moyenne > meilleure_moyenne:
            meilleure_moyenne = moyenne
            meilleur_eleve = eleve
print(f"L'élève avec la meilleure moyenne globale est {meilleur_eleve} avec une moyenne de {meilleure_moyenne:.2f}.")
