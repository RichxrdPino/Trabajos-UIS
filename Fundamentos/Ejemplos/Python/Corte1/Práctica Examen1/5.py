# Contar el número de cifras pares e impares de un número entero dado por el usuario.

n = int(input("Ingresa un número entero: "))

if n < 0:
    n = n * -1

a = 0
b = 0

for i in str(n):
    if int(i) % 2 == 0:
        a = a + 1
    else:
        b = b + 1
        
print(f"Impares: {b} - Pares: {a}")