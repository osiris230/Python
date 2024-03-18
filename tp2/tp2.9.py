def tri_croissant(liste):
    return sorted(liste)

entree_utilisateur = input("Entrez une liste de nombres séparés par des espaces : ")

liste_nombres = [float(nombre) if '.' in nombre else int(nombre) for nombre in entree_utilisateur.split()]

liste_triee = tri_croissant(liste_nombres)

print("Liste triée :", liste_triee)