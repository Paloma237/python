fruits = ["pomme", "banane"]

# append() — ajoute un élément à la fin
fruits.append("orange")
print(fruits)       # ["pomme", "banane", "orange"]

# extend() — ajoute plusieurs éléments à la fin
fruits.extend(["mangue", "ananas"])
print(fruits)       # ["pomme", "banane", "orange", "mangue", "ananas"]

# insert() — ajoute à une position précise
fruits.insert(1, "kiwi")
print(fruits)       # ["pomme", "kiwi", "banane", "orange", "mangue", "ananas"]

# pop() — retire et retourne le dernier élément
dernier = fruits.pop()
print(dernier)      # "ananas"

# pop(index) — retire à une position précise
fruits.pop(0)
print(fruits)       # ["kiwi", "banane", "orange", "mangue"]

# remove() — retire la première occurrence d'une valeur
fruits.remove("banane")
print(fruits)       # ["kiwi", "orange", "mangue"]

# sort() — trie dans l'ordre croissant
nombres = [3, 1, 4, 1, 5, 9, 2]
nombres.sort()
print(nombres)      # [1, 1, 2, 3, 4, 5, 9]

# sort(reverse=True) — trie dans l'ordre décroissant
nombres.sort(reverse=True)
print(nombres)      # [9, 5, 4, 3, 2, 1, 1]

# reverse() — inverse l'ordre
fruits.reverse()
print(fruits)       # ["mangue", "orange", "kiwi"]

# len() — nombre d'éléments
print(len(fruits))  # 3

# index() — position d'un élément
print(fruits.index("orange"))   # 1

# count() — nombre d'occurrences
print([1, 2, 2, 3, 2].count(2))  # 3

# clear() — vide la liste
fruits.clear()
print(fruits)       # []


#les tuples
# Création
coordonnees = (48.8566, 2.3522)
couleurs = ("rouge", "vert", "bleu")
singleton = (42,)       # tuple d'un seul élément — la virgule est obligatoire


#unpacking decalage
a, b, c = couleurs
print(a)     # "rouge"
print(b)     # "vert"
print(c)     # "bleu"

#ennumerate
fruits = ["pomme", "banane", "orange"]

# Sans enumerate — moins pratique
for i in range(len(fruits)):
    print(f"{i} : {fruits[i]}")

# Avec enumerate — plus pythonique
for i, fruit in enumerate(fruits):
    print(f"{i} : {fruit}")
# 0 : pomme
# 1 : banane
# 2 : orange

# Démarrer à 1 au lieu de 0
for i, fruit in enumerate(fruits, start=1):
    print(f"{i} : {fruit}")
# 1 : pomme
# 2 : banane
# 3 : orange
