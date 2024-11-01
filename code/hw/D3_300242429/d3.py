# Student name: Ioana Marinescu
# Student number: 300242429
# Cette program reponde au questions du devoir 2
import math

# QUESTION 1
def compte100(liste) :
    ''''
    ([int]) --> int
    retourne le nombre des elements superieurs a 100 dans la liste
    '''
    # vaiables
    compteur = 0

    # Boucle itere dans la liste pour chaque element
    for i in liste:
        # Si l'element est superieure que 100, ajouter le a la somme
        if i > 100:
            compteur += 1

    # Retourne la somme
    return compteur


# QUESTION 2
def sommeListeDiv2(liste) :
    '''
    ([float]) --> float
    retourne la somme des entiers qui sont pair
    '''

    # variables
    somme = 0

    # Boucle itere dans le String pour chaque element
    for i in liste:
        # Si l'entier est pair
        if i % 2 == 0:
            somme += i
    
    # Retourne la somme
    return somme
    

# QUESTION 3
def triples(s) :
    '''
    (str) --> bool
    retourn True ou False s'il y a trois characteres consecutifs egaux
    '''

    # Boucle itere dans le String pour chaque element et les duex elements suivants
    for i in range(0, len(s) - 2):
        # characteres
        ch1 = s[i]
        ch2 = s[i + 1]
        ch3 = s[i + 2]

        # Si les caractere sonts les memes, retourne True
        if ch1 == ch2 and ch1 == ch3:
            return True
    
    # Les cahracteres ne sont pas les memes, retourne False
    return False
        
# QUESTION 4
def momo(s) :
    '''
    (str) --> str
    Retourne le nombre des characteres consecutifs
    '''
    
    # Variables
    resultat = ""
    premier_caractere = s[0]
    compteur = 1
    
    # Boucle itere dans s (apres le premiere caractere)
    for i in s[1:]:
        # Si le caractere est le meme que le premiere nouveau caractere
        if i == premier_caractere:
            compteur += 1
        else:
            # Ajouter le caractere et compteur au resultat
            resultat += premier_caractere + str(compteur)
            premier_caractere = i
            compteur = 1
    
    # Ajouter le dernier caractere et compteur
    resultat += premier_caractere + str(compteur)
    
    return resultat

# QUESTION 5
def noDup(s) :
    '''
    (str) --> str
    Retourne une chaine de caracteres sans repetitions des caracteres consecutifs
    '''
    # Variables
    premier_caractere = s[0]
    resultat = premier_caractere

    # Boucle itere dans s pour chaque element
    for i in s[1:]:
        # Si les characteres ne sont pas les memes
        if premier_caractere != i:
            # Ajouter le caractere et reiniialiser premier_caractere
            premier_caractere = i
            resultat += premier_caractere

    # Retourne le resultat
    return resultat

###############################################
#                 CAS DE TEST                 #
###############################################

# Question 1
print(compte100([1,102,-3.5, 104])) # 2
print(compte100([1,99,-3.5,-7])) # 0
print(compte100([])) # 0

# Question 2
print(sommeListeDiv2([1,4,3,8,5])) # 12
print(sommeListeDiv2([])) # 0
print(sommeListeDiv2([4, -10, 7])) # -6

# Question 3
print(triples("abbbcdeeggggg")) # True
print(triples("abc2eee")) # True
print(triples("a23xxxxx")) # True
print(triples("abaacd")) # False

# Question 4:
print(momo("a")) # a1
print(momo("aabbbccccx")) # a2b3c4x1
print(momo("aaa1111")) # a314
print(momo("aaabcaax")) # a3b1c1a2x1

# Question 5:
print(noDup("a")) # a
print(noDup("aabbbccccx")) # abcx
print(noDup("aaa1111")) # a1
print(noDup("aaabcaax")) # abcax
