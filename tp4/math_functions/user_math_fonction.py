from basic import factorielle
from advanced import puissance

while True:
    try:
        n = int(input("Entrez un nombre entier pour calculer sa factorielle : "))
        print(f"La factorielle de {n} est {factorielle(n)}.")
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

while True:
    try:
        base = float(input("Entrez la base (un nombre) : "))
        exposant = float(input("Entrez l'exposant (un nombre) : "))
        print(f"{base} élevé à la puissance {exposant} donne {puissance(base, exposant)}")
        break
    except ValueError:
        print("Veuillez entrer des nombres valides.")