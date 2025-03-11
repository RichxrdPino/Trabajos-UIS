# MENÚ CON OPERACIÓNES ARITMÉTICAS BÁSICAS, 
# QUE PUEDA SELECIONAR LA OPERACIÓN
# SALIR SOLO CUANDO SE SELECCIONE

salir = False

while salir == False:
    
    #MENU INICIAL
    print("¿Qué operación desea realizar?")
    print("Suma: +")
    print("Resta: -")
    print("Producto: *")
    print("División: /")
    print("Salir: x")
    operación = input()
    
    #SELECIONES
    if operación == "+":
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(n1 + n2)
    elif operación == "-":
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(n1 - n2)
    elif operación == "*":
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(n1 * n2)
    elif operación == "/":
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(n1 / n2)
    elif operación == "x" or operación == "X":
        salir = True
    else:
        print("[SELECIÓN INVÁLIDA] [VUELVA A INTENTAR]")
    