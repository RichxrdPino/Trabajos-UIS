# Escribir un programa que determine si un número entero es positivo, negativo o cero. Después,
# modificar el programa para que reciba entradas de números enteros hasta que el número introducido
# sea 0. El programa debe dar el conteo de positivos y negativos y los respectivos promedios.

#Inicializar salir en False para ejecutar al menos 1 vez
salir = False

# Inicializar:
a = 0 # Contador de números positivos
b = 0 # Contador de números negativos
aSuma = 0 #Suma de los números positivos
bSuma = 0 #Suma de los números negativos

# Comprobar si se desea salir
while salir == False:
    
    n = int(input("Ingresa un número entero: ")) # Número actual
    
    # Comprobar si n es positivo, negativo o 0
    if n > 0:
        aSuma = n + aSuma # Sumar el número positivo actual
        a = a + 1 # Sumar 1 al contador de positivos
    elif n < 0:
        bSuma = n + bSuma # Sumar el número negativo actual
        b = b + 1 # Sumar 1 al contador de negativos
        
    # Si n es 0: 
    else:
        
        # Comprobar si hay o no positivos
        if a == 0:
            print(f"No hay números positivos")
        else:
            print(f"Hay {a} números positivos")
            print(f"Promedio: {aSuma/a}")
        
        # Comprobar si hay o no negativos
        if b == 0:
            print(f"No hay números negativos")
        else:
            print(f"Hay {b} números positivos")
            print(f"Promedio: {bSuma/b}")
            
        salir = True