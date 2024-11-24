# Student name: Ioana Marinescu
# Student number: 300242429
# Cette program reponde au questions du devoir 4
import math

# Variable globale (dictionaire)
d = {"apple":"pomme", "banana":"banane", "pear": "poire", "plum":"prune"}

# QUESTION 1
def transl(d, s) :
    '''
    (dictionnaire, chaine des caracteres) --> chaine des caracteres
    Si s est en anglais, la fonction retourne la traduction en français.
    Si s est en français, la fonction retourne la traduction en anglais
    '''

    # Si s est un mot anglais
    if s in d:
        return d[s] 
    
    # Si s est un mot francais
    elif s in d.values():
        return next((k for k, v in d.items() if v == s))
    
    # Si c'est ni en francais ni en anglais
    else:
        return "Unknown"

# QUESTION 2
def setOp(list_1, list_2):
    '''
    (list, list) --> list
    Retourn une liste qui est un combination des duex listes sans repetition des elements.
    '''
    # Liste qui va etre retourner
    liste_finale = []

    for i in range(len(list_1)):
        element = list_1[i]

        if element not in list_1[i + 1:]:
            list_finale.append(element)

    for i in range(len(list_2)):
        element = list_2[i]

        if (element not in list_2[i + 1:]) and (element not in list_finale):
            list_finale.append(element)

    return list_finale

# QUESTION 3


###############################################
#                 CAS DE TEST                 #
###############################################

# Question 1
print(transl(d, "pear")) # "poire"
print(transl(d, "poire")) # "pear"
print(transl(d, "appricot")) # "Unknown"

# Question 2
print(setOp([4, 7, 93], [])) # 
print() # 
print() # 

# Question 3
print() # 
print() # 
print() # 
