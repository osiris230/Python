personne = {
            "nom" : "Maxime", 
            "age" : 32, 
            "ville" : "Val-D'Or"
            }
print("Age : ",personne["age"])
print(personne)
personne["ville"] = "Paris"
print(personne)
personne["sexe"] = "Masculin"
del personne["ville"]
print(personne)
print("------------------------------------------------------")
for k,v in personne.items():
    print(f"{k} : {v}")