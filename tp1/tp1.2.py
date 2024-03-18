# Demande à l'utilisateur de saisir son âge
age = input("Veuillez entrer votre âge: ")

try:
    age = int(age)
    if age < 0:
        print("Erreur: L'âge ne peut pas être inférieur à 0.")
    elif age >= 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")
except ValueError:
    print("Erreur: Veuillez entrer un nombre valide.")