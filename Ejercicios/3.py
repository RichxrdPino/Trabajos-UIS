#SEPARAR PALABRAS POR ESPACIOS

frase = input("Ingresa la frase a separar: ")

n = len(frase)
separador = " "
palabra = ""

for i in range(n):
    if frase[i] == separador:
        print(palabra)
        palabra = ""
    else:
        palabra = palabra + frase[i]
print(palabra)