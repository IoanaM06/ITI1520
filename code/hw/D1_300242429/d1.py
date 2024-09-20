# Student name: Ioana Marinescu
# Student number: 300242429
# Cette program reponde au questions du devoir 1
import math

# Cette fonction calcule le temps (en minutes) nessecaire pour traverser n km a m km/h.
def tempsVoyage(distance_a_conduire, vitesse) :
    '''
    (float, float) --> float
    retourne le temps du voyage en minutes
    '''

    # Calculer
    temps = (distance_a_conduire / vitesse) * 60

    # Retourner
    return temps


# Fonction qui calule la note final en donnant 5 notes
def noteFinale(labos, moyenne_devoirs, quiz, examen_partial, examen_final) :
    '''
    (flaot, float, float, float, float) --> float
    retourne la note final
    '''

    # Caclule
    note_final = (labos * 10 / 100) + (moyenne_devoirs * 25 / 100) + (quiz * 5 / 100) + (examen_partial * 20 / 100) + (examen_final * 40 / 100)

    # Retourner
    return note_final


# fonction qui format la bibliographie
def bibformat(auteur, titre, ville, maisonEdition, annee) :
    '''
    (str,str,str,str, int)-> str
    Retourne une chaine de caractères en format: auteur (annee). titre. ville: maisonEdition 
    '''

    # Format l'information
    bibliographie = "'{} ({}). {}. {}: {}'".format(auteur, annee, titre, ville, maisonEdition)
    
    # Retourner
    return bibliographie


# Fonction qui fait une bibliographie
def bibFormatPrint() :
    '''
    () --> None
    lit l'information nessecaire pour formater la bibliographie et l'imprime
    '''

    auteur = input("SVP entez l'auteur: ")
    titre = input("SVP entez le titre: ")
    ville = input("SVP entez la ville: ")
    maison_edition = input("SVP entez la maison d'edition: ")
    annee = input("SVP entez l'annee de publication: ")

    print('{} ({}). {}. {}: {}'.format(auteur, annee, titre, ville, maison_edition))


# Fonction qui resout l'equation 10^4y=x+3
def logFun(x) :
    '''
    (int) --> float
    retourne la valuer du y
    '''

    # Calcule
    y = math.log10(x + 3) / 4

    # Retourne
    return y


# Fonction teste si millesime d'une annee est bissextile ou non
def anneeBis(an) :
    '''
    (int) --> boolean
    retourne si une annee est bissextile ou non
    '''

    # an est divisible par 4
    if an % 4 == 0:
        return True

    else:
        # an est divisible par 100
        if an % 100 == 0:
            return True
        
        # an n'est pas bissectile
        return False


# Appeler tempsVoyage()
print(tempsVoyage(400,100)) # Devrait retourner 240.0
print(tempsVoyage(20.6, 60)) # Devrait retourner 20.6
print(tempsVoyage(90, 24)) # Devrait retourner 225.0

# Appler noteFinale()
print(noteFinale(100,100,100,100,100)) # Devrait retourner 100.0
print(noteFinale(50,90.5,60,80,70)) # Devrait retourner 74.625
print(noteFinale(60, 78, 99, 85, 90)) # Devrait retourner 83.45

# Appeler bibFormat()
print(bibformat("Antoine de Saint Exupery", "Le petit prince", "Paris", "Jeunesse", 1943))
# Devrait retourner 'Antoine de Saint Exupery (1943). Le petit prince. Paris: Jeunesse'
print(bibformat("Margaret Atwood", "The Handmaid's Tale", "New York", "Houghton Mifflin Harcourt Publishing Company", 1986))
# Devrait retourner 'Margaret Atwood (1986). The Handmaid's Tale. New York: Houghton Mifflin Harcourt Publishing Company'

# Appeler bibFormatPrint()
bibFormatPrint()

print()

# Appeler logFun()
print(logFun(7)) # Devrait retourner 0.25
print(logFun(20)) # Devrait retourner 0.3404319590043982
print(logFun(999999997)) # Devrait retourner 2.25
print(logFun(0.1)) # Devrait retourner 0.12284042345856817
print(logFun(9997)) # Devrati retourner 1.0

# Appeler anneeBis()
print(anneeBis(1904)) # Devrait retourner True
print(anneeBis(1928)) # Devrait retourner True
print(anneeBis(1950)) # Devrait retourner False
print(anneeBis(1990)) # Devrait retourner False
print(anneeBis(1932)) # Devrait retourner True 
