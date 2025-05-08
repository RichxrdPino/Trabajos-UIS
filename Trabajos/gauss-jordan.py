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
                print(f"Fila fija = {i}")
                print(A[j, :])
                if A[j, i] != 0:
                    factor = (-1) * (A[i, i] / A[j, i])
                    # multiplicar fila completa en j por factor y sumar fila en i
                    filatemp = A[i, :] + (factor) * A[j, :]
                    print(filatemp)
                    A[j, :] = filatemp
        print(f"Cambios después de fijar la fila {i}")
        print(A)
        
    # divir la fila completa de referencia por el valor en la diagonal para convertir en 1
    for i in range(filas):
        A[i, :] /= (A[i, i])

    print("Reducción:")
    print(A)
    
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
matriz1 = np.array([[ 3.,  5.,  0., 12.],  [ 3.,  6.,  2.,  6.],  [ 3.,  2.,  1.,  0.]])
matriz2 = np.array([[ 3.,  5.,  0., 1, 0, 0],  [ 3.,  6.,  2.,  0,1,0],  [ 3.,  2.,  1.,  0, 0, 1]])

print("Matriz inicial")
print(matriz1)
print("Matriz igualada a la identidad")
print(matriz2)

# proceso para reorganizar filas en caso de que un elemento en la diagonal principal sea 0

# invocar la función gauss jordan
matriz_r = ReduccionGaussJordan(matriz1)
matriz_inv = ReduccionGaussJordan(matriz2)

print(matriz_r)
print(matriz_inv)
            
print()
print()
print()
print()

print(f"x = {matriz_r[0][3]}, y = {matriz_r[1][3]}, z = {matriz_r[2][3]}")
for i in range(filas):
    print(matriz_inv[i][-3:])