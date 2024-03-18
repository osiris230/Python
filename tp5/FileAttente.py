class FileAttente:
    def __init__(self):
        self.file_prioritaire = []
        self.file_normale = []

    def ajouter_personne_en_attente(self, nom):
        self.file_normale.append(nom)
        print(f"{nom} a été ajouté(e) à la file d'attente normale.")

    def ajouter_personne_prioritaire(self, nom):
        self.file_prioritaire.append(nom)
        print(f"{nom} a été ajouté(e) à la file d'attente prioritaire.")

    def supprimer_personne_en_attente(self):
        if self.file_prioritaire:
            personne_supprimee = self.file_prioritaire.pop(0)
            print(f"{personne_supprimee} (prioritaire) a été retiré(e) de la file d'attente.")
        elif self.file_normale:
            personne_supprimee = self.file_normale.pop(0)
            print(f"{personne_supprimee} a été retiré(e) de la file d'attente normale.")
        else:
            print("La file d'attente est vide.")

    def afficher_file_attente(self):
        if self.file_prioritaire or self.file_normale:
            print("File d'attente :")
            for personne in self.file_prioritaire:
                print(personne + " (prioritaire)")
            for personne in self.file_normale:
                print(personne)
        else:
            print("La file d'attente est vide.")

file_attente = FileAttente()
file_attente.ajouter_personne_en_attente("Ginette")
file_attente.ajouter_personne_prioritaire("Bob")
file_attente.ajouter_personne_en_attente("David")
file_attente.afficher_file_attente()
file_attente.supprimer_personne_en_attente()
file_attente.afficher_file_attente()