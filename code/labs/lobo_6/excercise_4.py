# Student name: Ioana Marinescu
# Student number: 300242429

def compte1(s, c) :
    # Methode 1 - count    
    return s.count(c)

def compte2(s, c) :
    # Methode 2 - boucle for 
    comptoir = 0
    # Pour chaquele element en s
    for i in s:
        # Si element actuel est le meme que c
        if c == i:
            # Augment comptoir
            comptoir += 1

    # Retourne le resulatat
    return comptoir

for i in range(0, 2):
    s = input('Donnez-moi un ensemble de caractères: ')
    print(compte1(s, 'a'))
    print(compte2(s, 'a'))
