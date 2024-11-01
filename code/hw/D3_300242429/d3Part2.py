# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]

     for i in range(len(p)):
        if i % 2 == 0:
            donneur.append(p[i])
        else:
            autre.append(p[i])
     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]
    valeur_counts = {}
    
    for carte in l:
        valeur = carte[:-1]
        if valeur in valeur_counts:
            valeur_counts[valeur] += 1
        else:
            valeur_counts[valeur] = 1
        
    
    for carte in l:
        valeur = carte[:-1]
        if valeur_counts[valeur] % 2 != 0:
            resultat.append(carte)
    
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    print(" ".join(p))
    

def entrez_position_valide(n):
    '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
    '''

    while True:
        try:
            position = int(input(f"Entrez la position d'une carte entre 1 et {n}: "))
            if 1 <= position <= n:
                return position - 1
            else:
                print(f"Veuillez entrer un nombre entre 1 et {n}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
     

def joue():
    '''()->None
     Cette fonction joue le jeu
    '''
    
    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]

    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    affiche_cartes(humain)
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()
    
    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)

    tour = 0
    
    while len(humain) > 0 and len(donneur) > 0:
        if tour == 0:
            print("\nVotre tour!")
            affiche_cartes(humain)
            print("Les cartes de Robot ont", len(donneur), "cartes. Choisissez une position.")
            position = entrez_position_valide(len(donneur))
            carte_piochee = donneur.pop(position)
            print(f"Vous avez pioché: {carte_piochee}")
            humain.append(carte_piochee)
            humain = elimine_paires(humain)
            tour = 1
        else:
            print("\nTour de Robot!")
            position = random.randint(0, len(humain) - 1)
            carte_piochee = humain.pop(position)
            print("Robot a pioché une de vos cartes.")
            donneur.append(carte_piochee)
            donneur = elimine_paires(donneur)
            tour = 0

    if len(humain) == 1:
        print("\nVous avez perdu! Vous êtes resté avec le pouilleux:", humain[0])
    elif len(donneur) == 1:
        print("\nBravo! Robot est resté avec le pouilleux:", donneur[0])
    else:
        print("\nAucun joueur n'a le pouilleux. Le jeu est terminé.")
    

	 
# programme principale
joue()
