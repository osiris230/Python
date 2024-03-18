def demander_nombres():
    # Input des nombres
    chaine_nombres = input("Entrez les nombres séparés par des espaces : ")
    
   
    nombres_str = chaine_nombres.split()
    
    
    nombres = [float(nombre) for nombre in nombres_str]
    
    return nombres

nombres = demander_nombres()
moyenne = sum(nombres) / len(nombres) if nombres else 0
print(f"La moyenne des nombres entrés est : {moyenne}")

