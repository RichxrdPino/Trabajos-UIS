n = int(input("Ingresa un número entero: "))

num = str(n)
largo = len(num)
lista1 = ""
lista2 = ""
cifras = 0

i = 0
while i < largo:
    if num[i] == "-":
        if int(num[1]) % 2 == 0:
            lista1 = lista1 + " " + "-" + num[1]
            cifras = cifras + 1
        else:
            lista2 = lista2 + " " + "-" + num[1]
            cifras = cifras + 1
        i = i + 1
    else:
        if int(num[i]) % 2 == 0:
            lista1 = lista1 + " " + num[i]
            cifras = cifras + 1
        else:
            lista2 = lista2 + " " + num[i]
            cifras = cifras + 1
    i = i + 1
        
print(f"Cifras pares:{lista1}")
print(f"Cifras impares:{lista2}")
print(f"{n} tiene {cifras} cifra(s).")