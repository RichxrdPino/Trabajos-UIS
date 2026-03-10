import numpy as np
import math as m

def ReduccionGaussJordan(A):
    filas, cols = A.shape    
    # proceso para fijar la fila de referencia y hallar el factor que anula el elemento correspondiente en la fila que se quiere reducir
    for i in range(filas):
        # i representa la fila que está siendo fijada
        for j in range(filas):
            # j representa la fila a comparar
            if i != j :
                
                if A[j, i] != 0:
                    factor = (-1) * (A[i, i] / A[j, i])
                    # multiplicar fila completa en j por factor y sumar fila en i
                    filatemp = A[i, :] + (factor) * A[j, :]
                    A[j, :] = filatemp
        
        
    # divir la fila completa de referencia por el valor en la diagonal para convertir en 1
    for i in range(filas):
        A[i, :] /= (A[i, i])
    
    return A
    #fin del def de gauss jordan

""" filas = int(input("introduzca el número de filas y columnas, o de ecuaciones: "))
cols = filas + 1

matriz = np.zeros((filas, cols))

for i in range(filas):
    for j in range(cols):
        matriz[i, j] = float(input(f"Introduzca el elemento para la posición {i + 1}, {j + 1} de la matriz: "))

print("La matriz es:")
print(matriz) """

filas = 3
cols = filas + 1
matriz = np.array([[ 3.,  5.,  0., 12.],  [ 3.,  6.,  2.,  6.],  [ 3.,  2.,  1.,  0.]])

# Crear la matriz inversa de A

I = I = np.zeros((filas, 2*filas)) #Crear una matriz de 0s para igualar la matriz a la identidad

## Crear matriz de coeficientes e igualarla a la identidad
for i in range(filas):
    for j in range(filas):
        I[i][j] = matriz[i][j] #Coeficientes
        if i == j:
            I[i][j+filas] = 1 #Identidad

# Aplicar reducción Gauss-Jordan para obtener matriz invertida
I_r = ReduccionGaussJordan(I)

# Extraer matriz inversa
matrizInv = np.zeros((filas, filas)) #Definir una matriz de mismas dimensiones

for i in range(filas):
    for j in range(filas):
        matrizInv[i][j] = I_r[i][j+filas]

print("Matriz inicial")
print(matriz)
print()

# Hallar determinante de una matriz nxn

# El determinante de una matriz nxn es la sumatoria de cada término de la primer fila 
# por el determinante de la sub matriz fuera de su columna y fila del término, intercalando los signos

def determinante(A):
    filas, cols = A.shape
    Acof = np.zeros((filas, filas)) #matriz de mismas dimensiones cuadradas
    for i in range(filas):
        for j in range(filas):
            Acof[i][j] = A[i][j] #Asignar coeficientes
    
    # Casos de determinante
    if filas == 1:
        return Acof[0,0]
    elif filas == 2:
        return (Acof[0,0]*Acof[1,1]) - (Acof[0,1]*Acof[1,0])
    else:
        det = 0
        for i in range(filas):
            a = Acof[0][i]    # <-- CORRECCIÓN AQUÍ
            subMatriz = np.zeros((filas-1, filas-1))
            
            # Recorremos filas de A (saltando la fila 0)
            sub_j = 0
            for j in range(1, filas):
                sub_i = 0
                # Recorremos columnas de A (saltando la columna i)
                for k in range(filas):
                    if k == i:
                        continue
                    subMatriz[sub_j][sub_i] = A[j][k]
                    sub_i += 1      # mover el sub_i+=1 aquí
                sub_j += 1          # y el sub_j+=1 aquí

            det += ((-1) ** i) * a * determinante(subMatriz)

        return det
    
Det = determinante(matriz)
print("Determinante")
print(Det)      
print()

# invocar la función gauss jordan en la matriz inicial
matriz_r = ReduccionGaussJordan(matriz)

print("Matriz Reducida Gauss-Jordan")
print(matriz_r)      
print()

print("Soluciones")
print(f"x = {matriz_r[0][3]}, y = {matriz_r[1][3]}, z = {matriz_r[2][3]}")
print()

print("Matriz Igualada")
print(I)
print()

print("Matriz Igualada reducida Gauss-Jordan")
print(I_r)
print()

print("Matriz Inversa")
print(matrizInv)
print()
