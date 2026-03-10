# Construir un programa que permita escoger entre dos operaciones, usando un
# menú. La primera, leer un número n y determinar si es par o impar. La segunda,
# leer un número n y determinar si es primo o no. n debe ser un número entero
# positivo. El programa debe detectar si la opción escogida es o no válida.

# Inicializar entrar en True para que ingresa automáticamente al menú
entrar = True

# Mientras entrar sea True
while entrar:
    print("===================================")
    print("")
    n = int(input("Ingresa un número entero positivo: ")) # Preguntar un número entero positivo
    
    if n > 0: # Confirmar que el número ingresado sea positivo

        # Mostrar opciones del menú
        print("")
        print("¿Qué deseas hacer con este número?")
        print("")
        print("1: Determinar si es par o impar")
        print("2: Determinar si es primo o no")
        print("0: Salir")
        # Solicitar la acción a realizar
        x = input("SELECCIÓN: ")
        
        # Si la selección es 1
        if x == "1":

            # Determinar si n es par o impar e imprimirlo.
            if n % 2 == 0:
                print(f"{n} es un número par")
            else:
                print(f"{n} es un número impar")
        
        # Si la selección es 2
        elif x == "2":

            # Inicializar los divisores de n en 0
            div = 0

            # Recorrer todos los números de 0 hasta n y comprobar si es un divisor
            for i in range(1,n+1):
                # Si i es divisor, se agrega 1 al contador de divisores
                if n % i == 0:
                    div = div + 1

            # Si n tiene más de 2 divisores, no es primo, si tiene 2 o menos, es primo. Imprimir el resultado
            if div > 2:
                print(f"{n} no es un número primo")
            else:
                print(f"{n} es un número primo")
            
        # Si la selección es 0
        elif x == "0":

            # Cambiar valor de entrar para no ejecutar el bucle del menú
            entrar = False
            print("======FIN DE LA EJECUCIÓN======") # Notificar que se ha finalizado la ejecución

        # Si la selección no coincide con ningún valor solicitado, notificar un error.            
        else:
            print("Debes ingresar un valor de selección válido(1,2 o 0)")

        # Siempre que la selección sea distinta de 0, se vuelve a preguntar n y qué se desea hacer con n
    
    else: # Si no es positivo, notificar un error
        print("el valor debe ser un número entero positivo")