n = int(input("Ingresa un número entero: "))

if n < 0:
    n = n * -1

num = str(n)
inver = ""

for i in num:
    inver = i+inver

if num == inver:
    print("Es capicúa (Palíndromo).")
else:
    print("No es capicúa (Palíndromo).")