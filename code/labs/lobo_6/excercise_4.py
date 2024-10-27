# Student name: Ioana Marinescu
# Student number: 300242429

def compte1(c, s) :
    # Methode 1 - count    
    return s.count(c)

def compte2(c, s) :
    # Methode 2 - boucle for 
    comptoir = 0
    # Pour chaquele element en s
    for i in s:
        # Si element actuel est le meme que c
        if c == i:
            # Augment comptoir
            comptoir += 1

s = input('')
