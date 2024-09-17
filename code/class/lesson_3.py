def pre_function_lesson():
    # strings
    ch = 'Voici une phrase.'
    print(ch)
    ch = "j'ai change la variable"
    print(ch)

    # adding struff to strings
    ch = "example." + " Une autre example. "
    print(ch)

    x = 12
    # ch += x --> this will not work
    ch += str(x) #str() changes the variable type to a string
    print(ch)

    # formatting
    h = 12
    m = 50
    s = 20
    ch = "{} : {} : {}".format(h, m, s)
    print(ch)

    # boolean expressions
    print(5 == 2 + 3) # Should return True
    print(6 == 2 + 3) # Should return False

    x = float(input("entrer une etier: "))

# We're learning about functions!!!
def calcul (x):
    # (float) -> float
    # retourne x ** 2 + 3 * x + 2
    return x ** 2 + 3 * x + 2

def paire_impaire(x, y):
    return (x % 2 == 0) and (y % 2 == 1)

# reponse = float(input("Entrer une etier: "))
# print(calcul(reponse))

reponse1 = int(input("Entrer une etier: "))
reponse2 = int(input("Entrer une autre etier: "))
print(paire_impaire(reponse1, reponse2))

