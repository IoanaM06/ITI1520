# Student name: Ioana Marinescu
# Student number: 300242429
# Cette fonction calcule la surface du triangle
import math
from math import ceil

# Fonction qui calcule la surface du triangle
def calc_surface_triangle(cote1, cote2, cote3) :
    '''
    (float, float, float) --> float
    retourne la sourface d'une traingle
    '''

    # Calculer
    p = (cote1 + cote2 + cote3) / 2
    surface = math.sqrt(p * (p - cote1) * (p - cote2) * (p - cote3))

    # Afficher
    print("La surface de cette triangle est", surface)

# Appeler la fonction
calc_surface_triangle(1, 2, math.sqrt(3)) # Devrait retourner 0.866...
