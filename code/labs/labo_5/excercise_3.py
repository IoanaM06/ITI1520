# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe calcule le distance d'une ballon lance a velocite v a Θ degres
import math

# Fonction qui calcule les distances chaque 10 degrees en donnent la velocite
def distance(velocite) :
    # liste
    distances = []

    # Boucle pour calculer theta et la distance
    for i in range (0, 90, 10) :
        # Calcule theta en rad
        theta = (math.pi / 180) * i
        # Calcule distance 
        distance = (2 * (velocite ** 2) * math.cos(theta) * math.sin(theta)) / 9.8
        distances.append(distance)
    
    # Retourne les distances
    return distances

# Appelle la fonction
print(distance(40)) # devrait retourner [0, 55.84, 104.94, 141.39, 160.78, 141.39, 55.84]
