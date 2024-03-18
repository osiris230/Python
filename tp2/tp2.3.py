def convertir_en_celsius():
    
    f = int(input("Entrez une température en fahrenheit: "))
    
    c = (f-32) * 5/9
    
    return c

print(f"Voici le résultat en celsius {convertir_en_celsius()}.")