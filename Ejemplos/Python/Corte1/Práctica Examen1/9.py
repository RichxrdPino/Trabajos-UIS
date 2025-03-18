frase = input("Ingresa una frase: ")

n = len(frase)
separador = " "

palabra= ""
inversion = ""

for i in range(n-1,-1,-1):
    if frase[i] == separador:
        inversion = inversion + " " + palabra
        palabra = ""
    else:
        palabra = frase[i] + palabra
        
inversion = inversion + " " + palabra
        
print(inversion)