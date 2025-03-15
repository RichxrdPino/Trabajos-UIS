n = int(input("Número de elementos: "))
suma = 0
if n > 0:
    for i in range(n):
        elem = float(f"Valor del elemento {i}")
        suma = suma + elem
    promedio = suma / n
    print("El promedio de los números es ", promedio)
elif n <= 0:
    print("Valor de los elementos inválido")