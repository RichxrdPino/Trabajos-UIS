## Crear un algoritmo con funciones que determine la media, mediana, 
## varianza, variación desviación estandar y rango de un conjunto de datos.

# LIBRERÍAS
import random as rnd

# Solicitar cantidad de datos y definir lista de estos
n = int(input("Ingresa el número de datos aleatorios a los que quieres aplicar regresión lineal: "))
A = []

#*  Generar n elementos en la lista A
for i in range(n):
    A.append(rnd.randint(0,100))
    
#* Definir las funciones para calcular cada Valor estadístico

#* Media / Promedio
def media(datos):
    media = sum(datos) / len(datos)
    return media

#* Mediana / Punto medio de los elementos ordenados de menor a mayor
def mediana(datos):
    
    #Ordenar la lista
    for j in range(len(datos)):
        for i in range(len(datos)-1):
            if datos[i] > datos[i+1]:
                a = datos[i]
                datos[i] = datos[i+1]
                datos[i+1] = a
    
    print(datos)
    
    # Comprobar si la cantidad de elementos es par
    if n % 2 == 0:
        mediana = datos[int(n/2)-1] # Si sí, guardar el elemento del medio mayor
    else:
        mediana = datos[int((n+1)/2)-1] # Si no, guardar el elemento del medio
    
    return mediana

#* Varianza / Dispersión 1
def varianza(datos):
    
    sum = 0
    for i in datos:
        sum = sum + ((i - media(datos))**2)
    varianza = sum / (len(datos) - 1)
    
    return varianza

#* Desviación estandar
def desviacion(datos):
    desviacion = varianza(datos)**(1/2)
    
    return desviacion

def rango(datos):
    rango = max(datos) - min(datos)
    
    return rango

# Comprobar que se generaron elementos
if len(A) == 0:
    print("|| ERORR || -- Debes pedir generar al menos 1 elemento")
else:
    
    print(A)
    print("")
    print(f"Media: {media(A)}")
    print("")
    print(f"Mediana: {mediana(A)}")
    print("")
    print(f"Varianza: {varianza(A)}")
    print("")
    print(f"Desviación estandar: {desviacion(A)}")
    print("")
    print(f"Rango: {rango(A)}")