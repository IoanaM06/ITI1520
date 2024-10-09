# Student name: Ioana Marinescu
# Student number: 300242429
# Cette program reponde au questions du devoir 2
import math

# QUESTION 1
def patinage(epaissur, temp_moyenne) :
    ''''
    (float, float) --> bool
    retourne une bool pour represnter si le canal est ouvert ou non
    '''

    # Verifie si l'epaisseur et temperature sont bon
    if epaissur >= 30 and temp_moyenne <= -10:
        return True
    
    # Le glace n'est pas assex epaisse et c'est n'est pas assez de foid
    return False 

# QUESTION 2
def alphaNote(entier) :
    '''
    (float) --> String
    retourne une note alphabetique (A+ - F)
    '''

    # Note numerique a note alphabetique
    if entier >= 90 :
        return "A+"
    
    elif entier >=85:
        return "A"
    
    elif entier >= 80 :
        return "A-"
    
    elif entier >= 75:
        return "B+"
    
    elif entier >= 70:
        return "B"
    
    elif entier >= 65:
        return "C+"
    
    elif entier >= 60:
        return "C"
    
    elif entier >= 55:
        return "D+"
    
    elif entier >= 50:
        return "D"
    
    elif entier >= 40:
        return "E"
    
    else:
        return "F"

# QUESTION 3
def alphaNoteVerif() :
    '''
    (vide) --> String
    '''
    while True:
        # Demande pour une valeur
        valuer = float(input("SVP entrez la note finale (de 0 a 100): "))
        
        # L'usager a donner une valuer valid
        if valuer <= 100 and valuer >= 0:
            # Appeler la fonction qui calcule la note alphabetique
            lettre = alphaNote(valuer)

            # Si c'est reussi
            if lettre != "E" or lettre != "F":
                return lettre + "\nReussi"
            
            # Si c'est echoue
            return lettre + "\nEchoue"
        
# QUESTION 4
def boucles(n) :
    '''
    (int) --> vide
    imprime les numeros de 1 a n (et n a 1) en sautants une numbre chaque fois
    '''

    # boucle pour 1 a n
    for i in range(1, n + 1, 2):
        print(i, end = ' ')

    print()

    # boucle pour n a 1
    for i in range(n, 0, -2): 
        print(i, end = ' ')

    print()

# QUESTION %
def facteursDeN(n) :
    '''
    (int) --> bool
    Calcule les factuers et si la somme est plus que n
    '''
    # Initiliation du somme
    somme = 0

    print("Factuers de {} =".format(n), end=" ")

    # boucle pour trouver les factuers
    for i in range(2, n) :
        # trouve la somme
        if n % i == 0:
            # calule la somme
            somme += i
            # imprime les factuers
            print(i, end=" ")
    print()
    # retourne True ou False
    return somme < n

# QUESTION 6
def carreParfait(x):
    '''
    (int) --> bool
    retourne True si x est un nombre carre parfait et False si non
    '''
    # Trouve la racine
    racine = math.sqrt(x)
    # bool reprent si x est un nombre carre parfait
    est_carre_parfait = racine % int(racine) == 0

    # Reponse si x est un carre parfait
    if est_carre_parfait:
        print("{} est un carre parfait et sa racine carree est {}".format(x, int(racine)))

    # Response si x n'est pas un carre parfait
    else:
        print("{} n'est pas un carre parfait".format(x))

    # Retourne bool
    return est_carre_parfait

# QUESTION 7
def maFun(n):
    '''
    (int) --> float
    retourne la solution pour l'equation (-1)^n/(2n + 1)
    '''
    return (math.pow(-1, n))/(2 * n + 1)

# Question 8
def maFun_bis(n) :
    '''
    (int) --> float
    retourne une approximation de pi
    '''

    # Initiliation du somme
    somme = 0

    # Calcule le somme de maFun n fois
    for i in range(0, n + 1):
        somme += maFun(i)

    # retourne l'approximation de pi
    return somme * 4

###############################################
#                 CAS DE TEST                 #
###############################################

# Question 1
print(patinage(30, -10)) # True
print(patinage(25.4, -15)) # False
print(patinage(33, -5)) # False
print()

# Question 2
print(alphaNote(100)) # A+
print(alphaNote(89)) # A
print(alphaNote(56)) # D+
print(alphaNote(30)) # F
print()

# Question 3
# print(alphaNoteVerif())
# print(alphaNoteVerif())
# print()

# Question 4:
boucles(13)
boucles(10)
print()

# Question 5:
print(facteursDeN(12))
print(facteursDeN(9))
print(facteursDeN(5))
print()

# Question 6:
print(carreParfait(16))
print(carreParfait(15))
print()

# Question 7:
print(maFun(0))
print(maFun(1))
print(maFun(10))
print(maFun(2))
print()

# Question 8:
print(maFun_bis(10))
print(maFun_bis(100))
print(maFun_bis(1000))
print(maFun_bis(10000))
