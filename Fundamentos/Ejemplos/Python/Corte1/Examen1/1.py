# Escribir un programa que lea un número entero y determine si este es un
# palíndromo, es decir, que se lee igual de izquierda a derecha que de derecha a
# izquierda. Estos números se conocen como como capicúas.

n = int(input("Ingresa un número entero: ")) # Pedir el número a comprobar

# Si n es negativo, se pasa a positivo para comprobar
if n < 0:
    n = n * -1

# Convertir el número en un cadena y guardar su valor en num
num = str(n)

# Inicializar la variable donde se guardará el número invertido
nInv = ""

# Recorrer cada caracter de la num en dirección: -->
for i in num:
    # colocar cada caracter a la izquierda para invertir el número
    nInv = i + nInv

# Si el número inicial y su inversión son iguales, es capicúa. De lo contrario, no lo es.
if num == nInv:
    print(f"{n} es capicúa") # Imprimir respuesta
else:
    print(f"{n} no es capicúa") # Imprimir respuesta