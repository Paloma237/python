# les listes
# fonction pour calculer la moyenne des notes d'un étudiant dans une liste de notes
def calculate_average(notes_list):
    return sum(notes_list) / len(notes_list) if notes_list else 0

# exemple d'utilisation
notes = [12, 10, 14, 8, 16]
moyenne = calculate_average(notes)
print(f"La moyenne des notes est : {moyenne:.2f}")



etudiants = ["Alice", "Bob", "Charlie", "Diana"]
notes = [15.5, 12.0, 18.0, 9.5]

print("Classement :")
resultats = list(zip(etudiants, notes))
resultats.sort(key=lambda x: x[1], reverse=True)

for rang, (etudiant, note) in enumerate(resultats, start=1):
    mention = "reçu" if note >= 10 else "recalé"
    print(f"{rang}. {etudiant} — {note}/20 — {mention}")