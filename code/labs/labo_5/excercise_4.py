# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe caclule l'ecart-type
import math

def ecart_type(valeurs) :
    # Initilisation de somme
    somme = 0

    # Calcules pour la moyenne
    for element in valeurs:
        somme += element
    moyenne = somme / len(valeurs)

    # Reinitialisation de somme
    somme = 0

    # Calcules pour trouver l'ecart type
    for element in valeurs:
        somme += (element - moyenne) ** 2
        print((element - moyenne) ** 2)

    s = math.sqrt(somme / (len(valeurs) - 1))

    # retourne l'ecart type
    return s

# Apelle fonction
print(ecart_type([3.5, 4, 2, 5.5])) # Devrait retourner 1.44