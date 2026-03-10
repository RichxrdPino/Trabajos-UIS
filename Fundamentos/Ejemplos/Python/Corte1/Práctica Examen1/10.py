# Agrega un 0 en cada dígito de un número entero dado por el usuario

n = int(input("Ingresa un número entero: "))
numero = str(n)

x = len(numero)
z = ""

for i in range(x-1):
    z = z + numero[i] + "0"
    
z = z + numero[-1]
print(z)