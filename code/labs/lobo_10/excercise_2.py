# Student name: Ioana Marinescu
# Student number: 300242429

class Voiture:
    def __init__(self, marque="Ford", couleur="rouge"):
        self.marque = marque
        self.couleur = couleur
        self.pilote = "personne"
        self.vitesse = 0

    def choix_conducteur(self, nom):
        self.pilote = nom

    def accelerer(self, taux, duree):
        if self.pilote == "personne":
            print("Cette voiture n'a pas de conducteur !")
        else:
            self.vitesse += taux * duree

    def affiche_tout(self):
        print(f"Marque: {self.marque}")
        print(f"Couleur: {self.couleur}")
        print(f"Conducteur: {self.pilote}")
        print(f"Vitesse: {self.vitesse} m/s")

    def __repr__(self):
        return f"Voiture(marque='{self.marque}', couleur='{self.couleur}', pilote='{self.pilote}', vitesse={self.vitesse})"

    def __eq__(self, autre):
        return (
            self.marque == autre.marque
            and self.couleur == autre.couleur
            and self.pilote == autre.pilote
            and self.vitesse == autre.vitesse
        )

a1 = Voiture('Peugeot', 'bleue')
a2 = Voiture(couleur = 'verte')
a3 = Voiture('Mercedes')

a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')

a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11) # Cette voiture n'a pas de conducteur !

a2.affiche_tout()
'''
Marque: Ford
Couleur: verte
Conducteur: Juliette
Vitesse: 21.6 m/s
'''
a3.affiche_tout()
'''
Marque: Mercedes
Couleur: rouge
Conducteur: personne
Vitesse: 0 m/s
'''
