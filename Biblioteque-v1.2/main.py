#import Livre as Livre
#import Librairie as Librairie

from Librairie import Librairie
from Livre import Livre


ma_librairie = Librairie()

def saisie_livre():
    livre = {}
    titre  = input("Donner le titre du livre: ")
    auteur = input("Donner l'auteur du livre: ")
    genre  = input("Donner le genre/catégorie du livre: ")
    try:
        prix   = input("Donner le prix du livre: ") # controle de saisi à venir.
        livre = Livre(titre, auteur, genre, prix)
    except ValueError as e:
        return (f"Erreur : {e}")    
    return livre

def menu():
    while True:
        print("1. Ajouter un livre")
        print("2. Chercher un livre")
        print("3. Supprimer un livre")
        print("4. Afficher la librairie")
        print("5. Modifier un livre")
        print("6. Quitter")
        
        choix = input("Entrer votre choix : ")

        if choix == '1':
            
            
            livre = saisie_livre()
            if not isinstance(livre, str):
                ma_librairie.ajouter_livre(livre)
            else:
                print(livre)
            #titre = input("Titre du livre : ")
            #auteur = input("Auteur du livre : ")
            #genre = input("Genre du livre : ")
            #try:
             #   prix = input("Prix du livre : ")
            #except ValueError as e:
             #   print(e,"allo")
            #livre = Livre(titre, auteur, genre, prix)
        elif choix == '2':
            titre = input("Entrez le titre du livre à chercher : ")
            ma_librairie.chercher_livre(titre)
        elif choix == '3':
            titre = input("Entrez le titre du livre à supprimer : ")
            ma_librairie.supprimer_livre(titre)
        elif choix == '4':
            ma_librairie.afficher_librairie()
        elif choix == '6':
            print("Au revoir !")
            break
        elif choix == '5':
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            genre = input("Genre du livre : ")
            try:
                prix = float(input("Prix du livre : "))
            except ValueError:
                print("ValueError")
            livre = Livre(titre, auteur, genre, prix)
            ma_librairie.modifier_livre(livre)
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