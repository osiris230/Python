def pgcd(a, b):

    a = int(input("Entrez le premier nombre : "))
    
    b = int(input("Entrez le deuxième nombre : "))

    while b != 0:
        a, b = b, a % b
    return a

print("Le PGCD de de vos nombres est :", pgcd())