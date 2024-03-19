class CompteBanquaire:
    def __init__(self, titulaire, solde_initiale=0):
        self.titulaire = titulaire
        self.solde = solde_initiale
    
    def depot(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Vous avez déposé {montant}$. Votre nouveau solde est de {self.solde}$.")
        else:
            print("Le montant du dépot doit être positif.")
    
    def retrait(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Vous avez retiré {montant}$. Votre solde restant est de {self.solde}$.")
        else:
            print("Solde insuffisant pour effectuer ce retrait.")

    def verifier_solde(self):
        print(f"Le solde de votre compte est de {self.solde}$.")

compte_bob = CompteBanquaire("bob", 1000)

compte_bob.depot(500)
compte_bob.retrait(150)
compte_bob.verifier_solde()