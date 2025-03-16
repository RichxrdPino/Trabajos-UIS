# Usa series de taylor para calcular el seno de un ángulo dado por el usuario


# El valor para el seno en series de taylor está dado por la siguiente sumatoria:
#                (-1)**n
#    sum      ------------- * x**(2n+1)         Donde n toma valores de 0 hasta infinito
# n=0 -> inf     (2n + 1)!                      y x es el ángulo en radianes

# Solicitar el valor del ángulo al que aplicar seno
x = int(input("Ingresa el ángulo(en grados) al que deseas aplicar seno: "))

# Pasar grados a radianes
x = (x * 3.141592) / 180

# Inicializar el rango de aproximación de la serie y la suma donde se guardará el valor del seno
n = 100
suma = 0

# Contar desde 0 hasta el rango de aproximación
for i in range(n):
    
    # Calcular factorial del denominador actual (2*i + 1)
    fact = 1
    for j in range(1, (2*i) + 2): # Recorre todos los números desde 1 hasta (2*i + 1) y guarda sus productos
        fact = fact * j
        
    # Se aplica la fórmula para el orden del elemento actual y se agrega a la sumatoria
    suma = suma + (( (-1)**i ) / (fact)) * (x**((2*i) + 1))

# Se imprime el valor aproximado del seno para el ángulo ingresado
print(suma)

