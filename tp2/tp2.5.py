def est_paire(a):
    
    return a % 2 == 0

while(True):
    try:
        a = int(input("Entrez un nombre : "))
        break
    except ValueError:
        print("Entrez un nombre valide")

print(est_paire(a))
