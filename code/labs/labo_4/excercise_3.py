# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe divine une nombre aleatoire
import random

# Fonction qui verifie si les deux nombres sonts les memes
def devine(nombre) :
    # Genere un nombre
    rand = random.randint(1, 10)

    # Retourne False s'ils ne sont pas egal et True s'ils sont
    return rand == nombre   

# Compt
i = 1
# Boucle While infinit
while True:
    # Demand une numbre de l'utilisateur
    nombre = int(input("Devine un nombre entre 1 et 10: "))
    
    # Si les nombres sont les memes
    if devine(nombre):
        print("C'est bon! Tu as deviné {} nombres.".format(i + 1))
        # Break boucle
        break

    # Message a dire que c'est pas correct
    print("Pas le bon nombre!")
    i += 1
