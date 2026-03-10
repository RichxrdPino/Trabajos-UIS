# Construir un programa que muestre los términos de la serie de Fibonacci que sean menores o iguales a
# un valor entero dado por el usuario.

# Solicitar el entero
n = int(input("Ingresa un número entero: "))

# Inicilizar los primeros dígitos de la sucesión y la lista donde van a guardarse.
a = 0
b = 1
lista = "0, 1"

#Empezar con i en 2 para empezar por el 3er elemento
i = 2

#Recorrer n posiciones
while i < n:
    suma = a + b #Sumar los 2 últimos elementos
    a = b #Guardar a como el último valor anterior
    b = suma # Guardar b como el último valor actual
    if b < n:
        lista = lista + ", " + str(b) # Agregar b a la lista siempre que sea menor que n
    i = i + 1

print(lista) # Imprimir la lista de números de la suceción menores que n