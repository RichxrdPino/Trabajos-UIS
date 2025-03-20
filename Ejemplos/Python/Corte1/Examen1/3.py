# Escribir un programa que lea un número entero y determine cuales de sus
# cifras son pares y cuales son impares. Además, el programa debe contar cuantas
# cifras tiene el número en total.

# Este código también acepta valores negativos

n = int(input("Ingresa un número entero: ")) # Solicitar número a comprobar cifras

# Si n es negativo, convertirlo en positivo
if n < 0:
    n1 = n * -1

# Convertir el número en un cadena y guardar su valor en num
num = str(n1)

# Inicializar las listas de pares e impares
lista1 = ""
lista2 = ""

# Recorrer cada caracter de num en direcció: --->
for i in num:
    # Comprobar si el dígito actual es par o no
    if int(i) % 2 == 0:
        # Si es par, agregarlo a la lista de pares
        lista1 = lista1 + " " + i
    else:
        # Si es impar, agregarlo a la lista de impares
        lista2 = lista2 + " " + i

# Imprimir ambas listas y la cantidad de cifras en total
print(f"las cifras pares de {n} son:{lista1}")
print(f"las cifras impares de {n} son:{lista2}")
print(f"El total de cifras de {n} son: {len(num)}")
