# Construir un programa que lea un número entero mayor que 2 y devuelva como resultado el
# número primo de valor más cercano, en este caso menor o igual, al número leído.

#Determinar las variables a revisar, n el número, x el número primo y div el número de divisores
n = int(input("número a revisar:"))
x = n
div = 3 #<-- div inicializa en 3 para que entre directamente al bucle while de más adelante

#Preguntar si el número es mayor a 2
if n > 2:

    #Comprovar si el número actual es primo o no
    while div > 2:
        div = 0 #Reinicializar el div una vez iniciado el bucle

        #Determinar si x es primo o no
        for i in range(1,x+1):
            if x%i == 0:
                div=div+1
        #restarle 1 a x en caso de que no sea primo
        if div > 2:
            x = x-1
    #imprimir la respuesta si x es primo
    print(f"El número primo más cercano a {n} es {x}")
else:
    print("Debes ingresar un valor mayor a 2")