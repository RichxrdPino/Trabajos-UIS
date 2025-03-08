#CONVERTIR UNA PALABRA A PIG LATIN ("gato" -> "atogay")

palabra = input("Palabra a convertir: ")
n = len(palabra)
piglatin = ""

for i in range(n):
    if i == 0:
        l1 = palabra[i]
    else:
        piglatin = piglatin + palabra[i]

print(piglatin + l1 + "ay")