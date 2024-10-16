# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe calcule la moyenne des elements

# Fonction qui calcule la moyenne d'une list des entiers
def moyenne_element(x) :
    somme = 0

    # Calcule la somme des entiers
    for i in range (0, len(x)) :
        somme += x[i]

    # Calcule la moyenne
    moyenne = somme / len(x)

    # Imprime la moyenne
    print(moyenne)

# Liste de test et appelle la fonction
moyenne_element([1, 2, 3, 4, 5]) # Devrait retourner 3.0
moyenne_element([4, 17, 5, 7]) # Devrait retourner 8.25
