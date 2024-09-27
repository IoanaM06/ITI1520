# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe évalue combien de racines q'une equation quadratique a
import math

# Une fonction qui évalue combien des racines q'une equation quadratique a
def racines(a, b, c) :
    '''
    (float, float, float) --> int
    Retourne combien des racines q'une equation quadratique a
    '''

    # Calculer le discriminant
    disciminant = math.pow(b, 2) - 4 * a * c

    # 2 racines
    if disciminant > 0:
        return 2
    
    # Pas de racine
    elif disciminant < 0:
        return 0
    
    # 1 racine
    return 1

# Demander l'utilisateur pour leur age
a = float(input("Quele est la valuer de a: "))
b = float(input("Quele est la valuer de b: "))
c = float(input("Quele est la valuer de c: "))
print(racines(a, b, c))
