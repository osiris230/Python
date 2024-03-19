
class Personne:
    """
    Cette class personne nous permet de représenter la conception dune personne
    """
    # constructeur
    def __init__(self, nom,prenom, age): #-> None:
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    #acceder a l'attribut age a l'extérieur de la classe    
    def get_age(self):
        return self.__age
    
    # mutateur de lattribut age
    def set_age(self, age):
        self.age = age
    
    print("personne crée : cela veut dire qu'un objet personne a été crée ou instanciation")
    def infos(self):
        print (f"nom: {self.__nom}, prénom: {self.__prenom}, age: {self.__age}")

# Main
#Instanciation de la classe personne --> creation d'un objet
p1 = Personne("Diallo", "Abdou", 40)
p1.infos()
#print(p1.__doc__)  