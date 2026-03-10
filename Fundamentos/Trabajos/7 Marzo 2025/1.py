# CONVERTIR NÚMERO (N) EN REPRESENTACIÖN BASE b

n = int(input("Número a representar: "))
b = int(input("Base nueva en la que se desea representar: "))
m = 0
fact = 1
if 2 <= b & b < 10:
    print(n)
    while n > 0:
        z = int(n // 1)
        r = z % b
        print(r)
        n = z / b
        m = m + (fact * r)
        fact = fact * 10
    print (m)
else:
    print("La base debe ser un número de 2 a 9")