#Exercice 5 — Opérateurs bit-à-bit
#représentation binaire de chaque résultat avec bin()
def manipuler_bits():
    a=int(input("entrez un nombre entier: "))
    b=int(input("entrez un autre nombre entier: "))
    print(f"AND bit-à-bit: {bin(a & b)}")
    print(f"OR bit-à-bit: {bin(a | b)}")
    print(f"XOR bit-à-bit: {bin(a ^ b)}")
    print(f"NOT de a: {bin(~a)}")
    print(f"NOT de b: {bin(~b)}")
    print(f"Décalage à gauche de a de 2 positions: {bin(a << 2)}")
    print(f"Décalage à droite de b de 2 positions: {bin(b >> 2)}")
manipuler_bits()