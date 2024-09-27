# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe évalue si l’âge est entre 18 et 55 inclusivement

# Une fonction qui retourn si l'age est entre 18 et 55 inclusivement
def est_age(age) :
    '''
    (float) --> boolean
    Retourne True si age est entre 18 et 55 et False si non
    '''

    # age est entre 18 et 55
    if age >= 18 and age <= 55:
        return True
    
    # age n'est pas entre 18 et 55
    else:
        return False

# Demander l'utilisateur pour leur age
age_utilisateur = float(input("Quelle est votre age? "))

# L'age est entre 18 et 55
if est_age(age_utilisateur):
    print("Transaction acceptée")

# L'age n'est pas entre 18 et 55
else:
    print("Transaction refusée")
