# Construir un programa que lea un número variable de valores enteros. El resultado que entregara el
# programa es la media de los números pares de entre los leídos, es decir, la suma de todos los valores
# pares dividida por el número de estos.

#Definir el número de elementos a promediar.
n = int(input("¿Cuántos valores numéricos desea ingresar? "))

# Inicialzar la variable donde se guarda la suma de los pares y la cantidad de estos.
suma = 0
a = 0

#Recorrer la cantidad de elementos que se desean evaluar
for i in range(1,n+1):
    
    #Definir el valor en la posición i y guardarlo temporalmente
    x = int(input(f"valor {i}: "))
    
    #Identificar si x es par. Si lo es, se agrega a la suma y se aumenta el contador de pares en 1
    if x % 2 == 0:
        suma = suma + x
        a = a + 1

#Hacer el promedio y mostrarlo
promedio = suma / a
print ("El promedio de los números pares que ingresaste es: " + str(promedio))