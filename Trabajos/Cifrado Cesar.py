# CIFRADO CESAR

frase = input("Ingresa una frase: ")

n = int(input("Orden del cifrado cesar: "))

separador = " "
nFrase = ""
palabra = ""


for letra in frase:
    ordLetra = ord(letra)
    if (65 < ordLetra < 90) or (97 < ordLetra < 122):
        if 90 < (ordLetra + n) < 96 or (ordLetra + n) > 122:
            nFrase = nFrase + chr((ordLetra + n) - 26)
        else:
            nFrase = nFrase + chr((ordLetra + n))
    else:
        nFrase = nFrase + letra

print(nFrase)
