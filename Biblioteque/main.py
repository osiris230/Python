#import Livre as Livre
#import Librairie as Librairie

from Librairie import Librairie
from Livre import Livre

ma_librairie = Librairie()

def menu():
    while True:
        print("1. Ajouter un livre")
        print("2. Chercher un livre")
        print("3. Supprimer un livre")
        print("4. Afficher la librairie")
        print("5. Quitter")
        choix = input("Entrer votre choix : ")

        if choix == '1':
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            genre = input("Genre du livre : ")
            prix = float(input("Prix du livre : "))
            livre = Livre(titre, auteur, genre, prix)
            ma_librairie.ajouter_livre(livre)
        elif choix == '2':
            titre = input("Entrez le titre du livre à chercher : ")
            ma_librairie.chercher_livre(titre)
        elif choix == '3':
            titre = input("Entrez le titre du livre à supprimer : ")
            ma_librairie.supprimer_livre(titre)
        elif choix == '4':
            ma_librairie.afficher_librairie()
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

menu()

"""
livre1 = Livre("Les Misérables", "Victor Hugo", "Roman", 15)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "Conte", 10)
livre3 = Livre("1984", "George Orwell", "Fiction", 12)

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