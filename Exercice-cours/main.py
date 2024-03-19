from Course import Course
from Student import Student



math = Course("Mathématiques", 4)
history = Course("Histoire", 3)
science = Course("Science", 5)
francais = Course("Français", 3)
informatique = Course("Informatique", 6)
algo = Course("Algorythme", 3)


alice = Student("Alice", 20)
bob = Student("Bob", 22)


alice.add_cours(math)
alice.add_cours(history)
alice.add_cours(francais)
bob.add_cours(science)
bob.add_cours(francais)
bob.add_cours(algo)


alice.display_student_info()
bob.display_student_info()