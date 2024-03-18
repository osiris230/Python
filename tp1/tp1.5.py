def calculer_moyenne(nombres):
    if not nombres:
        return 0
    somme = sum(nombres)
    
    moyenne = somme / len(nombres)
    
    return moyenne

nombres = [4, 8, 15, 16, 23, 42]
moyenne = calculer_moyenne(nombres)
print("La moyenne des nombres", nombres, "est", moyenne)

# autre exemple

# Définir une fonction calculer_moyenne qui calcule la moyenne d'une liste de nombres
def calculer_moyenne(liste_nombres):
    if len(liste_nombres) == 0:
        return 0
    else:
        return sum(liste_nombres) / len(liste_nombres)

# Test de la fonction avec une liste de nombres de votre choix
liste_notes = [12, 15, 17, 14, 10]
print("La moyenne des notes est :", calculer_moyenne(liste_notes))