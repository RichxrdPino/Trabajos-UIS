# Hallar el resultado de sumar las cifras de un número entero dado por el usuario.

n = int(input("Ingresa un número entero: "))
x = len(str(n))
sum = 0

if str(n)[0] == "-":
    
    sum = int(str(n)[0] + str(n)[1])
    
    for i in range(2,x):
        sum = sum + int(str(n)[i])
else:
    for i in str(n):
        sum = sum + int(i)


print("La suma de sus dígitos es: " + str(sum))