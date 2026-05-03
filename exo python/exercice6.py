#3) Jeu : deviner un nombre (while + break)
import random
nombre_secret = random.randint(1, 100)
for i in range(4):
    nombre_devine = int(input("Devinez le nombre entre 1 et 100 : "))
    if nombre_devine < nombre_secret:
        print("Trop petit !")
    elif nombre_devine > nombre_secret:
        print("Trop grand !")
    elif nombre_devine == nombre_secret:
        print("Félicitations, vous avez deviné le nombre secret !")
else:
    print(f"Désolé, vous avez épuisé vos tentatives. Le nombre secret était {nombre_secret}.")  
    
    