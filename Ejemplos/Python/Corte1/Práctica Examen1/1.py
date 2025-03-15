# términos que tengan número de orden par de la sucesión de Fibonacci.

n = int(input("Ingresa un número entero: "))

a = 0
b = 1
lista = ""

for i in range(1,n+1):
    
    if i == 2:
        lista = "1"
    elif i % 2 == 0:
        lista = lista + ", " + str(b)
    
    sum = a + b
    a = b
    b = sum
    
print(lista)