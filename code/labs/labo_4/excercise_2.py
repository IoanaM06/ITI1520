# Student name: Ioana Marinescu
# Student number: 300242429
# Cette programe imprime les numeros de 1 a N

# Fonction qui imprime les numeros de 1 a N
def compt(N) :
    '''
    (int) --> vide
    imprime au console
    '''
    # Boucle while pour compter
    i = 1
    while i != N + 1:
        print(i)
        i += 1

    print("")

    # Boucle for pour copmter
    for j in range (1, N + 1):
        print(j)

n_utilisateur = int(input("Donne moi un nombre: "))
# Appeler la fonction
compt(n_utilisateur)