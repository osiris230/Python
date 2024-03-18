def addition():
    while True:
        try:
            a = int(input("Entrez le premier nombre : "))
            break
        except ValueError:
            print("Ce n'est pas un nombre valide, réessayer.")
    while True:
        try:
            b = int(input("Entrez le deuxième nombre : "))
            break
        except ValueError:
            print("Ce n'est pas un nombre valide, réessayer.")
    return a + b

print(f"La somme des deux nombres est {addition()}.")

def multiplication():
    while True:
        try:
            a = int(input("Entrez le premier nombre : "))
            break
        except ValueError:
            print("Ce n'est pas un nombre valide, réessayer.")
    while True:
        try:
            b = int(input("Entrez le deuxième nombre : "))
            break
        except ValueError:
            print("Ce n'est pas un nombre valide, réessayer.")
    return a * b

print(f"Le produit des deux nombres est {multiplication()}.")
