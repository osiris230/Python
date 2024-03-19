class Etudiant:
    # création dun constructeur, instanciation de la classe
    # self désigne l'objet courrant
    etudiant_cree = 0 # Variable de classe
    def __init__(self, nom_e, prenom_e, age_e, niveau_e):
        self.nom = nom_e
        self.prenom = prenom_e
        self.age = age_e
        self.niveau = niveau_e
        Etudiant.etudiant_cree += 1
        print(f"Création de l'étudiant {Etudiant.etudiant_cree}...")
    def infos(self):
        print (f"nom: {self.nom}, prénom: {self.prenom}, age: {self.age} ans, niveau d'étude: {self.niveau}")

# céation d'un objet/ étudiant
e1 = Etudiant("Labrie", "Stéphane", 40, "AEC")
# (f"nom: {e1.nom}, prénom: {e1.prenom}, age: {e1.age} ans, niveau d'étude: {e1.niveau}")
e1.infos()

e2 = Etudiant("Diallo", "Abdou", 40, "Maitrise")
e2.infos()

e3 = Etudiant("Bijou", "Jojo", 40, "Bacc")
e3.infos()