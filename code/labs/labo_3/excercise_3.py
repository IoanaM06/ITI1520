# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe évalue si une entier est divisible par 2 et/ou 3 ou non

# Une fonction qui évalue si une entier est divisible par 2 et/ou 3 ou non
def estDivisible(entier) :
    '''
    (float) --> int
    Retourne quelle si s'est divisible ou non
    '''

    # Divisible par 2 et 3
    if entier % 2 == 0 and entier % 3 == 0:
        return 1
    
    # Divisible par 2 ou 3
    elif entier % 2 == 0 or entier % 3 == 0:
        return 2
    
    # Pas divisible ni par 2, ni par 3
    return 3

# Demander l'utilisateur pour leur age
entier_utilisateur = int(input("Donne moi un nombre enteir: "))
resultat = estDivisible(entier_utilisateur)

# 2 et 3
if estDivisible == 1:
    print("Divisible par 2 et 3")

# 2 ou 3
elif resultat == 2:
    print("Divisible 2 ou 3")

# Pas divisible
elif resultat == 3:
    print("N'est pas divisible par 2 ou 3")
