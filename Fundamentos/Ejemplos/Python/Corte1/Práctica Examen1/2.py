# número primo mayor o igual al un número entero dado por el usuario
# Entrada mayor que 2

n = int(input("Ingresa un número entero mayor que 2: "))

div = 3

if n > 2:
    
    while div > 2:
        div = 0
        for i in range(1, n+1):
            if n % i == 0:
                div = div + 1
        n = n + 1
    print("El número primo mayor o igual más cercano es: " + str(n - 1))
    
else: 
    print("El número debe ser mayor que 2")