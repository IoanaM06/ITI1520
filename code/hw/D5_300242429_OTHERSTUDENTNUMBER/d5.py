# Student name: Ioana Marinescu
# Student number: 300242429
# Cette program reponde au questions du devoir 5
import math

# QUESTION 1
def triangle(nombre, compteur = 0):
    '''
    (int, int) --> vide
    Imprime une trigle des etoils
    '''
    # Si le compteur n'est pas plus que le nombre donne, imprime * compter fois
    if compteur <= nombre:
        for i in range(compteur):
            print("*", end=" ")
        print()
        # Appelle la fonction et augment le compteur
        triangle(nombre, compteur + 1)      

# QUESTION 2
def etoiles(nombre, compteur = 0):
    # if compteur <= nombre:
    #     for i in range(compteur):
    #         print("*", end=" ")
    #     print()
    #     etoiles(nombre, compteur + 1)

    
    
    triangle(nombre)



# QUESTION 3


###############################################
#                 CAS DE TEST                 #
###############################################

# Question 1
triangle(5)
print() # 
print() # 
print() # 

# Question 2
etoiles(3) # 
print() # 
print() # 

# Question 3
print() # 
print() # 
print() # 
