class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.__titre = titre
        self.__auteur = auteur
        self.__genre = genre
        self.__prix = prix

    # Getters
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_genre(self):
        return self.__genre

    def get_prix(self):
        return self.__prix

    # Setters
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_genre(self, genre):
        self.__genre = genre

    def set_prix(self, prix):
        self.__prix = prix

    def afficher_details(self):
        print("-----------------------------------------------------------")
        print(f"Titre: {self.__titre}")
        print(f"Auteur: {self.__auteur}")
        print(f"Genre: {self.__genre}")
        print(f"Prix: {self.__prix}$")
        print("-----------------------------------------------------------")
"""
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
"""




livre1 = Livre("Les Misérables", "Victor Hugo", "Roman", 15)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "Conte", 10)
livre3 = Livre("1984", "George Orwell", "Fiction", 12)
"""
ma_librairie = Librairie()

ma_librairie.ajouter_livre(livre1)
ma_librairie.ajouter_livre(livre2)
ma_librairie.ajouter_livre(livre3)
ma_librairie.chercher_livre("Les Misérables")
ma_librairie.chercher_livre("Le Petit Prince")
ma_librairie.chercher_livre("1984")
ma_librairie.afficher_librairie()
ma_librairie.chercher_livre("bob")
ma_librairie.supprimer_livre("1984")
ma_librairie.afficher_librairie()
"""