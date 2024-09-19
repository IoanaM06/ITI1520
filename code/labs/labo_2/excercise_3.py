# Student name: Ioana Marinescu
# Student number: 300242429
# Cette program calcule la note final

# Fonction calcule la note final d'une person
def calc_note_final(devoirs_moyenne, partial, examen) :
    '''
    (float, float, float) --> int
    retourne la note final
    '''

    # Calculer la note final
    note_final = int((devoirs_moyenne * 25 / 100) + (partial * 25 / 100) + (examen * 50 / 100))

    # Afficher
    print("Ta note final est", note_final)

# Appeler la fonction
calc_note_final(50, 80, 70) # Devrait retourner 67
