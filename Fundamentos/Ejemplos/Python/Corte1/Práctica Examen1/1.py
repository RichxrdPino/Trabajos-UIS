# términos que tengan número de orden par de la sucesión de Fibonacci.

# Pedir número de elementos de la suceción a generar
n = int(input("Ingresa un número entero: "))

# Inicializar los valores iniciales de la sucesión y una cadena donde se van a ir guardando
a = 0
b = 1
lista = ""

#Contar elementos de 1 hasta n
for i in range(1,n+1):
    
    # Esta linea agrega el primer término sin la coma inicial: ", 1, 3..."
    if i == 2:
        lista = "1"
        
    # Preguntar si la posición actual es par o impar, si es par, agregar el último número a la lista.
    elif i % 2 == 0:
        lista = lista + ", " + str(b)
    
    # Reorganizar los valores, a como el último anterior y b como la suma de los 2 anteriores.
    sum = a + b
    a = b
    b = sum

# Imprimir la lista de números de la suceción con orden par
print(lista)