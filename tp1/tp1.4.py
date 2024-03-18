jours = ("Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi")
for jour in jours:
    print(jour)

mois = ("Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre")
index = 0
while index < len(mois):
    print(mois[index])
    index += 1  

capitales = {
    "France": "Paris",
    "Italie": "Rome",
    "Allemagne": "Berlin"}

capitales["Canada"] = "Ottawa"

for pays, capitale in capitales.items():
    print("Capitale de ", pays, ":", capitale)
