#a = int(input("Entrez la valeur de a"))
#b = int(input("Entrez la valeur de b"))
#x = -b/a
#print("Le resultat de l'operation est =", x)
a = 6
b = 5
def resolution_equation(z, t):
    if (z==0):
        print("Division par zéro impossible")
    else:
        x = -t/z 
    return x

x = resolution_equation(a,b) 
print(x)   