import random as rnd

n = int(input("Ingresa el número de elementos aleatorios a los que quieres aplicar regresión lineal: "))
A = []

# Generar n elementos en la lista A
for i in range(n):
    A.append(rnd.randint(0,100))

# Comprobar que se generaron elementos
if len(A) == 0:
    print("|| ERORR || -- Debes pedir generar al menos 1 elemento")
else:
    #* Media / Promedio
    media = sum(A) / len(A)
    
    #* Mediana / Punto medio de los elementos ordenados de menor a mayor
    
    #Ordenar la lista
    for j in range(len(A)):
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                a = A[i]
                A[i] = A[i+1]
                A[i+1] = a
    
    # Comprobar si la cantidad de elementos es par
    if n % 2 == 0:
        mediana = A[int(n/2)-1] # Si sí, guardar el elemento del medio mayor
    else:
        mediana = A[int((n+1)/2)-1] # Si no, guardar el elemento del medio
    
    #* 