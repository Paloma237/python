#1) Gérer une liste d'étudiants (ajout, suppression, tri) 
students = []

def add_student(name, age):
    students.append({"name": name, "age": age})

def remove_student(name):
    students.remove({"name": name, "age": next((s["age"] for s in students if s["name"] == name), None)})

def sort_students():
    students.sort(key=lambda x: x["name"])
#appel des fonctions
add_student("Alice", 20)
add_student("Bob", 22)
add_student("Charlie", 19)
print("Étudiants après ajout :")
for student in students:
    print(f"- {student['name']}, {student['age']} ans")     
remove_student("Bob")
print("\nÉtudiants après suppression de Bob :")
for student in students:
    print(f"- {student['name']}, {student['age']} ans")
sort_students()
print("\nÉtudiants triés par nom :")
for student in students:
    print(f"- {student['name']}, {student['age']} ans")     
    
#2) Unpacking d'un tuple coordonnées (x, y, z)
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Coordonnées : x={x}, y={y}, z={z}") 
#3) Utiliser zip() pour associer deux listes (noms et âges)
names = ["Alice", "Bob", "Charlie"]
ages = [20, 22, 19]
students_info = list(zip(names, ages))
print("\nInformations des étudiants :")
for name, age in students_info:
    print(f"- {name}, {age} ans")
    

