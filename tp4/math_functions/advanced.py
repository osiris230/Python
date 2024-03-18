def puissance(base, exposant):
    return base ** exposant

while True:
    try:
        base = float(input("Entrez un nombre : "))
        break
    except ValueError:
        print("Ce n'est pas un nombre valide pour la base.")

while True:
    try:
        exposant = float(input("Entrez l'exposant (un nombre) : "))
        # Si vous souhaitez restreindre l'exposant à un entier, utilisez int(input(...)) et ajustez en conséquence.
        break
    except ValueError:
        print("Ce n'est pas un nombre valide pour l'exposant.")

resultat = puissance(base, exposant)
print(f"{base} à la puissance {exposant} donne {resultat}")
