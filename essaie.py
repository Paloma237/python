"""#déclaration des variables
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
e,d=a+b,a//b
e,m=a%b,a-b
print(f"la somme est {e}")
print(f"la division entière est {d}")
print(f"le modulo est {e}")
print(f"le reste est {m}")
#opérateurs logiques
age=20
bac=True
if(age>=18 and bac== True):
    print("vous etes éligibles pour composer")
if(age>=18 or bac==True):
    print("vous pouvez déposer votre candidature")
if(not bac): 
    print("impossible de composer")
else:
    print("vous pouvez déposer votre candidature")
#conversion
int(3.9)
int(True)
int (False)
#verifier si un nombre est pair ou impair   
nombre=int(input("entrez un nombre: "))
if(nombre%2==0):
    print("le nombre est pair")
else:
    print("le nombre est impair")
#utilisation de elif

note=int(input("entre ta note (de 0 à 20): "))
if(note<10):
    print("faible")
elif(note<12):
    print("passable")
elif(note<=14):
    print("bien")
elif(note<17):
    print("très bien")
else:
    print("excellent")
#utilisation des boucles
#afficher la table de multiplication de 1 à 10
print("récupération de 10 nombres:")
for nombre in range (0,11):
    n=nombre*10
    print(f"{nombre}*{10}={n}")
#déviner un nombre entre 1 et 100
import random
nombre_secret=random.randint(1,100)
tentatives=0
while tentatives != nombre_secret:
    tentatives=int(input("devinez le nombre entre 1 et 100: "))
    tentatives += 1
    if tentatives < nombre_secret:
        print("trop petit")
    elif tentatives > nombre_secret:
        print("trop grand")
    else:
        print(f"félicitations! vous avez deviné le nombre secret {nombre_secret} en {tentatives} tentatives.")
#dessiner un triangle avec les étoiles
hauteur=int(input("entrez la hauteur du triangle: "))
for i in range(1,hauteur+1):
    print("*"*i)    """
# fonction calculer la moyenne de 5 nombres   
def moyenne(notes):
    total = 0
    for note in notes:
        total += note
    moyenne = total / len(notes)
    print(f"la moyenne est: {moyenne}")
    return moyenne

