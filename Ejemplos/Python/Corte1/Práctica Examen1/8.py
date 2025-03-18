# Escriba un código que pida un número entero e
# imprima el número más cercano divisble entre 2, 3 y 5. (Sea mayor, menor o igual)

n = int(input("Ingresa un número entero: "))

n1 = n
n2 = n
mayor = 0
menor = 0
        
if (n % 2 == 0) and (n % 3 == 0) and (n % 5 == 0):
    print(n)
    
else:
    
    Nodiv235 = True
    while Nodiv235:
        if (n1 % 2 == 0) and (n1 % 3 == 0) and (n1 % 5 == 0):
            mayor = n1
            Nodiv235 = False
        else: 
            n1 = n1 + 1

    Nodiv235 = True
    while Nodiv235:
        if (n2 % 2 == 0) and (n2 % 3 == 0) and (n2 % 5 == 0):
            menor = n2
            Nodiv235 = False
        else: 
            n2 = n2 - 1
    
    if mayor - n > n - menor:
        print(menor)
    elif mayor - n == n - menor:
        print(f"{n} está a la misma distancia entre {menor} y {mayor}")
    else:
        print(mayor)