nmax = int(input("introduzca el número de términos:")) 
penultimo = 0
ultimo = 1
print(penultimo)
print (ultimo)
cont = 2
while cont < nmax :
    suma = ultimo + penultimo
    penultimo = ultimo 
    ultimo = suma 
    cont = cont + 1 
    print(ultimo)
print("fin")