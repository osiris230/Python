class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.prix = prix

    # Getters
    @property #property nous renseigne que l'attribut titre est maintenant privé
    def titre(self):
        return self.__titre
    @property
    def auteur(self):
        return self.__auteur
    @property
    def genre(self):
        return self.__genre
    @property
    def prix(self):
        return self.__prix

    # Setters
    @titre.setter
    def titre(self, titre):
        self.__titre = titre
    @auteur.setter
    def auteur(self, auteur):
        self.__auteur = auteur
    @genre.setter
    def genre(self, genre):
        self.__genre = genre
    @prix.setter
    def prix(self, prix):
        if isinstance(prix, float) == False: # true ou false
            raise ValueError("Le prix ne peut être qu'un nombre entier ou décimal")
        self.__prix = prix
        

    def afficher_details(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Genre: {self.genre}")
        print(f"Prix: {self.prix}$")
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



"""
livre1 = Livre("Les Misérables", "Victor Hugo", "Roman", 15)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "Conte", 10)
livre3 = Livre("1984", "George Orwell", "Fiction", 12)

"""
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