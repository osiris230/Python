def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

while True:
    try:
        n = int(input("Entrez un nombre entier pour calculer sa factorielle : "))
        if n < 0:
            print("Veuillez entrer un nombre positif ou nul.")
        else:
            break
    except ValueError:
        print("Ce n'est pas un nombre valide. Veuillez réessayer.")

print(f"La factorielle de {n} est {factorielle(n)}.")