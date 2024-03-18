class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher(self):
        print("---------------------------------------")
        print(f"Nom : {self.nom}, Age : {self.age}")
        print("---------------------------------------")

class ListePersonne:
    def __init__(self):
        self.liste_personne = []

    def ajouter_personne(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        self.liste_personne.append(nouvelle_personne)

    def afficher_personne(self):
        for personne in self.liste_personne:
            personne.afficher()

    def rechercher_personne(self, nom):
        nom_recherche = nom.lower()
        for personne in self.liste_personne:
            if personne.nom.lower() == nom_recherche:
                print(f"Personne trouvée : {nom}")
                personne.afficher()
                return
        print("Personne non trouvée.")

    def filtrer_personne_par_age(self, min_age, max_age):
        personne_trouvee = False  
        for personne in self.liste_personne:
            if min_age <= personne.age <= max_age: 
                personne.afficher()  
                personne_trouvee = True  
        if not personne_trouvee:  
            print("Aucune personne trouvée dans cet intervalle d'âge.")  


liste_personne = ListePersonne()
liste_personne.ajouter_personne("Ginette", 64)
liste_personne.ajouter_personne("Bob", 52)
liste_personne.ajouter_personne("David", 38)
liste_personne.ajouter_personne("Marie", 22)
liste_personne.afficher_personne()
liste_personne.rechercher_personne("Ginette")
liste_personne.rechercher_personne("Charlie")
liste_personne.filtrer_personne_par_age(18, 40)