# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe obtient des notes d’étudiants de 
# l’utilisateur et calcule la moyenne, le maximum, et le minimum.

# Fonction qui calcule la moyenne, le maximum, et le minimum
def min_max_moyenne(notes) :
    # Initilization de min, max, et somme
    min = max = somme = notes[0]

    # Boucle itère à travers la liste
    for i in range (1, len(notes)) :
        # L'element a index i
        element = notes[i]

        # Si element est moins que min, il le remplace
        if element < min:
            min = element

        # Si element est plus que max, il le remplace
        elif element > max:
            max = element

        # Calcule la somme
        somme += element
    
    # Calcule la moyenne
    moyenne = somme / len(notes)
    # Imprime les resultates
    print(" moyenne: {} \n min: {} \n max: {}".format(moyenne, min, max))

# Appelle la fonction
min_max_moyenne([50, 97, 81, 74, 62, 56]) # Min = 50, Max =  97, Moyenne = 70
min_max_moyenne([7, 88, 71, 48]) # Min = 7, Max =  88, Moyenne = 53.5
