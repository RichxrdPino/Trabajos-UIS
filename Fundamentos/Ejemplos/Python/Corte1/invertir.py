entrada = input("Palabra a voltear: ")
print(entrada)
n = len(entrada)
salida = ""
for i in range(n):
    salida = entrada[i] + salida
print(salida)