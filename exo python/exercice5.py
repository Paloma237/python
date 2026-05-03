#2) Afficher les multiples de 3 entre 1 et 50 avec for + continue
for i in range(1, 51):
    if i % 3 != 0:
        continue
    print(i)