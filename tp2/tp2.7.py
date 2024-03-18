def est_present(liste, valeur):

    return valeur in liste

liste_test = ['pomme', 'banane', 'cerise', 'datte']

while True:
    valeur_a_chercher = input("Entrez le fruit à chercher dans la liste : ")
    if valeur_a_chercher and not valeur_a_chercher.isdigit():
        
        break
    else:
        print("Erreur : vous avez entré un chiffre ou rien du tout. Veuillez entrer un texte valide.")

print(est_present(liste_test, valeur_a_chercher))