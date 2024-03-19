class Student:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.courses = []
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError("L'âge ne peut être qu'un nombre entier.")
        self.__age = age
    
    @property
    def courses(self):
        return self.__courses
    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def add_cours(self, courses):
        self.courses.append(courses)

    def display_student_info(self):
        print(f"Nom : {self.nom}\nAge : {self.age}\nCours suivis :")
        i = 0
        for course in self.courses:
            print(f"{i+1}.{course.nom} ({course.credits} crédits)")
            i+=1
        print("--------------------------------")

    def info(self):
        print("------------------------------------------------------------")
        print(f"Nom : {self.__nom}")
        print(f"Age : {self.__age}")
        i = 0
        for course in self.courses:
            print(f"{i+1}.{course.nom}, Crédits : {course.credits}")
            i=+1
        print("------------------------------------------------------------")