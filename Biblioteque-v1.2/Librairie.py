class Librairie:
    def __init__(self):
        self.livres = {}

    def ajouter_livre(self, livre):
        self.livres[livre.titre] = livre

    def supprimer_livre(self, titre):
        if titre in self.livres:
            del self.livres[titre]
            print(f"Le livre '{titre}' a été supprimé.")
        else:
            print(f"Le livre '{titre}' n'est pas dans la librairie.")

    def chercher_livre(self, titre):
        if titre in self.livres:
            print("Détails du livre recherché :")
            self.livres[titre].afficher_details()
        else:
            print(f"Le livre '{titre}' n'est pas dans la librairie.")
    
    def afficher_librairie(self):
        for titre,livre in self.livres.items():
            print(f"{titre} -> {livre.auteur}, {livre.genre}, {livre.prix}")

    def modifier_livre(self, livre):
        titre = livre.titre.lower()
        if titre in self.livres:
            livre_edit = self.livres[titre]
            livre_edit.auteur = livre.auteur # c'est la meme chose que : livre_edit.set_auteur(auteur)
            livre_edit.genre = livre.genre # livre_edit.set_genre(genre)
            livre_edit.prix = livre.prix
            print(livre_edit)
            self.ajouter_livre(livre_edit)
        else:
            print(f"Le livre {livre.titre} n'est pas trouvé dans notre librairie.")