class Course:
    def __init__(self, nom, credits):
        self.nom = nom
        self.credits = credits

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def credits(self):
        return self.__credits
    @credits.setter
    def credits(self, credits):
        if not isinstance(credits, int):
            raise ValueError("Crédit ne peut être qu'un nombre décimal.")
        self.__credits = credits
    