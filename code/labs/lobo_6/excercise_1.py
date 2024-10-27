# Student name: Ioana Marinescu
# Student number: 300242429

# Variables de l'exercice
s1 = 'bon'
s2 = 'mauvais'
s3 = 'fou'

# Reponse pour a
a = 'ou' in s3

# Reponse pour b
b = ' ' not in s1

# Reponse pour c
c = s1 + s2 + s3

# Reponse pour d
d = ' ' in c

# Reponse pour e
e = ''
for i in range(0, 10) :
    e += s3

# Reponse pour f
f = len(c)

# Imprimer les resultats
print('{}\n{}\n{}\n{}\n{}\n{}'.format(a, b, c, d, e, f))
