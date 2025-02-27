nmax = int(input())
suma = 0
k = 0
while k < nmax:
    termino = -1 ** k / 2 * k + 1
    suma = suma + termino
    k = k + 1
print(suma * 4)