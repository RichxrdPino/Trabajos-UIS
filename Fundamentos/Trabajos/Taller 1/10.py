# Construir un programa que muestre el siguiente término de la serie de Fibonacci respecto a un valor
# entero dado por el usuario.

n = int(input("Ingresa un número entero: "))

# Inicilizar los primeros dígitos de la sucesión y la variable para salir del bucle
a = 0
b = 1
entrar = True

#Empezar con i en 2 para empezar por el 3er elemento
i = 2

#Recorrer n posiciones
while i < n and entrar:
    suma = a + b #Sumar los 2 últimos elementos
    a = b #Guardar a como el último valor anterior
    b = suma # Guardar b como el último valor actual
    
    # Si b es mayor que n, salir del bucle
    if b > n:
        entrar = False
    i = i + 1

print(b) # Imprimir el siguiente número de la suceción respecto a n