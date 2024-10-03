# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe calcule le factoriel de n

# Fonction qui calcule le factoriel de n
def calculeFact(n) :
    # Valeur initial
    fact = 1
    # Boucle For pour calculer factoriel
    for i in range(n, 1, -1) :
        fact *= i
    
    # Retourne le factoriel
    return fact

# Demande un nombre non negatif
nombre = int(input("Donne moi un nombre non-negatif: "))

# L'utilisateur n'as pas entrer un nombre valid et demand un nombre non negatif encore
while nombre < 0:
    print("Invalide")
    nombre = int(input("Donne moi un nombre non-negatif: "))

# Appeler le fonction
print(calculeFact(nombre))
