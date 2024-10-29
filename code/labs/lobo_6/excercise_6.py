# Student name: Ioana Marinescu
# Student number: 300242429

def coder(s):
    # List pour le message coder
    resultat = ''

    # Boucle pour trouver les deux characteres
    for i in range(0, len(s)-1, 2):
        ch1 = s[i]
        ch2 = s[i + 1]

        # Ajoute les deux characteres echangees
        resultat += ch2
        resultat += ch1

    # Si s est de longeur impair
    if len(s) % 2 == 0:
        # Le charactere est le meme
        resultat += s[len(s) - 1]

    # Retourne le resultat
    return resultat

# Appeler la fonction
print(coder('example'))
        