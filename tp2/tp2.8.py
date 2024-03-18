def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

n = int(input("Entrez un nombre entier pour calculer sa factorielle : "))
print(f"La factorielle de {n} est {factorielle(n)}.")