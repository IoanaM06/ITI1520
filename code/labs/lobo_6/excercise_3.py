# Student name: Ioana Marinescu
# Student number: 300242429


# Variable de l'exercice
s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''
print()

# Reponse pour a
nS = s.replace('.', ' ').replace(',', ' ').replace(';', ' ')
print(nS)
print()

# Reponse pour b
nS = nS.strip()
print(nS)
print()

# Reponse pour c
nS = nS.lower()
print(nS)
print()

# Reponse pour d
d = nS.count('de')
print(d)
print()

# Repnose pour e
nS = nS.replace('était', 'est')
print(nS)
