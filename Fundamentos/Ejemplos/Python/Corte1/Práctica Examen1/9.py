entrar = True

while entrar:
    print("======================")
    print("")
    frase = input("Ingresa una nueva frase: ")
    print("")
    
    print("¿Qué deseas hacer con esta frase?")
    print("1: Invertir orden de las palabras")
    print("2: Invertir orden de las letras")
    print("0: Salir")

    x = int(input("ELECCIÓN: "))

    n = len(frase)
    
    if x == 1:
        
        separador = " "
        palabra= ""
        inversion = ""

        for i in range(n-1,-1,-1):
            if frase[i] == separador:
                inversion = inversion + " " + palabra
                palabra = ""
            else:
                palabra = frase[i] + palabra
                
        inversion = inversion + " " + palabra
                
        print(inversion)
        
    elif x == 2:
        salida = ""
        for i in range(n):
            salida = frase[i] + salida
        print(salida)
        
    elif x == 0:
        print("====FIN DE LA EJECUCIÓN====")
        entrar = False
    else: 
        print("Debes ingresar alguna de las opciones (1 o 2).")