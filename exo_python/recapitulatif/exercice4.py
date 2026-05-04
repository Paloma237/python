#Exercice 4 — Opérateurs logiques avancés
#système de connexion fictif
def verifier_identifiants():
    username=input("entrez votre nom d'utilisateur: ")
    password=input("entrez votre mot de passe: ")
    if (username == "admin" and password == "admin123") or (username == "user" and password == "user123"):
        return True
    else:
        return False
print("accès autorisé :", verifier_identifiants())