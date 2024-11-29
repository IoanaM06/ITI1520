# Student name: Ioana Marinescu
# Student number: 300242429

class CompteBancaire:
    def __init__(self, nom="Dupont", solde=1000):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        if somme > self.solde:
            print("Fonds insuffisants pour ce retrait.")
            print()
        else:
            self.solde -= somme

    def affiche(self):
        print(f"Titulaire: {self.nom}")
        print(f"Solde: {self.solde:.2f} €")
        print()

class CompteEpargne(CompteBancaire):
    def __init__(self, nom="Dupont", solde=1000, taux_interet=0.3):
        super().__init__(nom, solde)  # Appelle le constructeur de CompteBancaire
        self.taux_interet = taux_interet / 100  # Convertir le pourcentage en décimal

    def changeTaux(self, valeur):
        self.taux_interet = valeur / 100

    def capitalisation(self, nombreMois):
        print(f"Nombre de mois: {nombreMois}")
        print(f"Taux d'intérêt mensuel: {self.taux_interet * 100:.2f}%")

        self.solde = self.solde * (1 + self.taux_interet) ** nombreMois
    

    
# EXAMPLES    
compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
'''
Titulaire: Duchmol
Solde: 950.00 €
'''

compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()
'''
Titulaire: Dupont
Solde: 1025.00 €
'''

c1 = CompteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()
'''
Titulaire: Duvivier
Solde: 950.00 €
'''
c1.capitalisation(12)
'''
Nombre de mois: 12
Taux d'intérêt mensuel: 0.30%
'''
c1.affiche()
'''
Titulaire: Duvivier
Solde: 984.77 €
'''
c1.changeTaux(.5)
c1.capitalisation(12)
'''
Nombre de mois: 12
Taux d'intérêt mensuel: 0.50%
'''
c1.affiche()
'''
Titulaire: Duvivier
Solde: 1045.51 €
'''
