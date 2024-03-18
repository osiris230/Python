noms = ["Pierre", "Marie", "Bob", "Karen"]
ages = [36, 18, 42, 70]
personnes = dict(zip(noms, ages))
print(personnes)

while(True):
    try:
        nouveau_nom = str(input("Entrez un nouveau nom : "))
        nouvel_age = int(input("Entrez son age : "))
        if nouvel_age < 0:
            print("Entrer un age valide")
        else:
            break
    except ValueError:
        print("Entré invalide")
personnes[nouveau_nom] = nouvel_age
print(personnes)