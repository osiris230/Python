class Librairie:
    def __init__(self):
        self.livres = {}

    def ajouter_livre(self, livre):
        self.livres[livre.get_titre()] = livre

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
            print(f"{titre} -> {livre.get_auteur()}, {livre.get_genre()}, {livre.get_prix()}")