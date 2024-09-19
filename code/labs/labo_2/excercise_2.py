# Student name: Ioana Marinescu
# Student number: 300242429
# Cette program transforme de Celcius en Fahrenheit

# fonction calcule de Celcius en Fahrenheit
def celcius_en_fahrenheit(temp_celcius) :
    '''
    (float)-->float
    retourne le temperature en Fahrenheit
    '''

    # calcule pour trouver la temperature en Fahrenheit
    temp_fahrenheit = (temp_celcius * 9.0 / 5.0) + 32

    # afficher
    print("{}°C est {}°F".format(temp_celcius, temp_fahrenheit))

# appeler la fonction
celcius_en_fahrenheit(4.0) # devrait retourner 39.2
celcius_en_fahrenheit(-2.0) # devrait retourner 28.4
celcius_en_fahrenheit(500.0) # devrait retourner 932.0
