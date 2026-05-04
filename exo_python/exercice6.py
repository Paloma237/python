#3) Jeu : deviner un nombre (while + break)
import random
nombre_secret = random.randint(1, 100)
while True:
    nombre_devine = int(input("Devinez le nombre entre 1 et 100 : "))
    if nombre_devine < nombre_secret:
        print("Trop petit !")
    elif nombre_devine > nombre_secret:
        print("Trop grand !")
    elif nombre_devine == nombre_secret:
        print("Félicitations, vous avez deviné le nombre secret !")
        break
