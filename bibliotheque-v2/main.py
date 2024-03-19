from Librairie import Librairie
from Livre import Livre


# Mian

# Menu : choix.
"""
    Creation livre
    Ajout livre dans la livrairie
    Chercher un livre
    Supprimer un livre
    Affichier tous les livres.
"""
# fonction option ... la saisie on demande a l'utilisateur des infos des livres 
# pour ajouter dans la librairie.
def choix_option():
    print("1. Créer un livre: ")
    #print("2. Ajout livre dans la livrairie: ")
    print("2. Chercher un livre: ")
    print("3. Supprimer un livre: ")
    print("4. Modifier un livre: ")
    print("5. Afficher tous les livres: ")
    print("6. Appuyer sur q pour quitter : ")
    choix = input("veuillez choisir parmi les options suivantes : ")
    return choix

def ajout_livre():
    titre  = input("Donner le titre du livre: ")
    auteur = input("Donner l'auteur du livre: ")
    genre  = input("Donner le genre/catégorie du livre: ")
    prix   = input("Donner le prix du livre: ") # controle de saisi à venir.
    return Livre(titre, auteur, genre, prix)

def saisie():
    librairie = Librairie()
    while True:
        option = choix_option()
        if option == "1":
            
            livre = ajout_livre()
            
            # livre.set_titre("php"), plus tot ==> livre.titre = "php"
            librairie.ajouter_livre(livre)
         
    
        elif option == "2":
            titre  = input("Donnez le titre du livre que vous cherchez : ")
            librairie.chercher_livre(titre)
        elif option == "3":
            titre  = input("Donnez le titre du livre que vous voulez supprimer : ")
            librairie.supprimer_livre(titre)   
        elif option == "4":
            livre = ajout_livre()
            librairie.modifier_livre(livre)
            librairie.afficher_librairie()
            print("-----------------------------------------------")
        elif option == "5":
            librairie.afficher_librairie()
            print("-----------------------------------------------")    
        elif option.lower() == "q":
            break
        else:
            print("Choix invalide !")        


saisie()
