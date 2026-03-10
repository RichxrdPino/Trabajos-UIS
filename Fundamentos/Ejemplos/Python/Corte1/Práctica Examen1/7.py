# Escriba un código que recorra un número entero positivo de elementos de la 
# sucesión de Fibonacci e imprima únicamente los de orden primo

n = int(input("Ingresa un número entero: "))

a = 0
b = 1

lista = ""

for i in range(1,n+1):
    
    # Comprobar la cantidad de divisores de la posición actual
    div = 0
    for j in range(1,i+1):
        if i % j == 0:
            div = div + 1
            
    # Si la posición es prima, agregar a la lista
    if i == 1:
        lista = "0"
    elif div == 2:
        lista = lista + ", " + str(a)
    
    sum = a + b
    a = b
    b = sum

print(lista)