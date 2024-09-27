# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe évalue quelle activite a faire

# Une fonction qui évalue quelle activite a faire
def activites(temp) :
    '''
    (float) --> int
    Retourne quelle activite a faire
    '''

    # Temperature pour Natation
    if temp >= 80:
        return 1
    
    # Temperature pour Soccer
    elif temp >= 60:
        return 2
    
    # Temperature pour Volleyball
    elif temp >= 40:
        return 3
    
    # Temperature pour Ski
    return 4

# Demander l'utilisateur pour leur age
temp_utilisateur = float(input("Quelle est la temperature? "))
resultat = activites(temp_utilisateur)

# Natation
if resultat == 1:
    print("Nataion")

# Soccer
elif resultat == 2:
    print("Soccer")

# Volleyball
elif resultat == 3:
    print("Volleyball")

# Ski
else:
    print("Ski")
