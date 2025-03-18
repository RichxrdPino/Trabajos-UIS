entrar = True

while entrar:
    print("===================================")
    print("")
    n = int(input("Ingresa un número entero positivo: "))
    
    if n > 0:
        print("")
        print("¿Qué deseas hacer con este número?")
        print("")
        print("1: Determinar si es par o impar")
        print("2: Determinar si es primo o no")
        print("0: Salir")
        x = input("SELECCIÓN: ")
        
        if x == "1":
            if n % 2 == 0:
                print(f"{n} es un número par")
            else:
                print(f"{n} es un número impar")
                
        elif x == "2":
            div = 0
            for i in range(1,n+1):
                if n % i == 0:
                    div = div + 1
            if div > 2:
                print(f"{n} no es un número primo")
            else:
                print(f"{n} es un número primo")
                
        elif x == "0":
            entrar = False
            print("======FIN DE LA EJECUCIÓN======")
            
        else:
            print("Debes ingresar un valor de selección válido(1,2 o 0)")
    else:
        print("el valor debe ser un número entero positivo")