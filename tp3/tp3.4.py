"""
etudiants = [
            {"nom": "Alice", "note": 12},
            {"nom": "Bob", "note": 8},
            {"nom": "Steve", "note": 15},
            {"nom": "Charlotte", "note": 9}
            ]

print("Étudiants ayant obtenu une note supérieure ou égale à 10 :")
for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(etudiant["nom"])
"""

etudiants = []  

nombre_etudiants = int(input("Combien d'étudiants souhaitez-vous ajouter ? "))

for i in range(nombre_etudiants):
    nom = input(f"Entrez le nom de l'étudiant {i+1} : ")
    note = int(input(f"Entrez la note de l'étudiant {i+1} : "))
    etudiant = {"nom": nom, "note": note}
    etudiants.append(etudiant)

print("Étudiants ayant obtenu une note supérieure ou égale à 10 :")
for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(etudiant["nom"])

print(etudiants)