#déclaration des variables
a=5
b=2
m=a/b
nom="batista"
# on peut aussi déclarer toutes les variables sur une seule ligne
c,d,e,prenom= 1, 2, 2.5, "paloma"
# recupération des variables
print(m)
print(nom)
print(prenom)
#afficher bonjour
print("bonjour tout le monde!")
#utilisation de input
age=int(input("quel est ton age? "))
print("ton age est: "+str(age))
#utilisation des f-strings
taille=float(input("quelle est ta taille ?"))
print(f"ta taille est {taille}")
prenom= input("quel est ton prénom:")
print("bonjour " +prenom)
#calculs
e=a+b
d=a//b
e=a%b
m=a-b
print(f"la somme est {e}")
print(f"la division entière est {d}")
print(f"le modulo est {e}")
print(f"le reste est {m}")

