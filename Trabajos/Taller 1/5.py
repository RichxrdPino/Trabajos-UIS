# Escribir un programa que permita convertir un entero dado en base 2, 4, 8, 16.

n = int(input("Número a representar: "))

print("Seleccione una base para hacer la representación del número")
print("OPCIONES: 2 - 4 - 8 - 16")
b = int(input("Base: "))

m = 0
hexa = ""
fact = 1

if b == 2 or b == 4 or b == 8:
    while n > 0:
        z = int(n // 1)
        r = z % b
        n = z / b
        m = m + (fact * r)
        fact = fact * 10
    print (m)
elif b == 16:
    print("Hexadecimal")
    while n > 0:
        z = int(n // 1)
        r = z % b
        if r < 10:
            hexa = str(r) + hexa
        elif r == 10:
            hexa = "A" + hexa
        elif r == 11:
            hexa = "B" + hexa
        elif r == 12:
            hexa = "C" + hexa
        elif r == 13:
            hexa = "D" + hexa
        elif r == 14:
            hexa = "E" + hexa
        elif r == 15:
            hexa = "F" + hexa
        n = z // b
        
    print (hexa)
else:
    print("La base debe ser 2, 4, 8 o 16")