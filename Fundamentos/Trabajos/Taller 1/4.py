# Solicita al usuario que ingrese el primer número entero y lo convierte a tipo entero
n1 = int(input("Digite un número entero: "))
# Solicita al usuario que ingrese el segundo número entero y lo convierte a tipo entero
n2 = int(input("Digite otro número entero: "))

# Verifica si ambos números son pares o ambos son impares
if (n1 % 2 == 0 and n2 % 2 == 0) or (n1 % 2 != 0 and n2 % 2 != 0):
    # Si alguno de los números es cero, se establece el mcd (máximo común divisor) en 0
    if n1 == 0 or n2 == 0:
        mcd = 0
    # Si el primer número es mayor que el segundo, se usará un ciclo while
    elif n1 > n2:
        i = 1
        # Se itera desde 1 hasta n2 para encontrar todos los divisores comunes
        while i <= n2:
            # Si i es divisor de ambos números
            if n1 % i == 0 and n2 % i == 0:
                mcd = i  # Se actualiza mcd con el divisor actual (el mayor encontrado hasta el momento)
            i = i + 1
    # Si el primer número es menor que el segundo, se utiliza un ciclo for
    elif n1 < n2:
        # Se itera desde 1 hasta n1 (inclusive) para hallar divisores comunes
        for i in range(1, n1 + 1, 1):
           if n1 % i == 0 and n2 % i == 0:
                mcd = i  # Se actualiza mcd con el divisor actual encontrado
    # Si ambos números son iguales, el mcd es el mismo número
    else:
        mcd = n1
    # Si mcd es 0, significa que al menos uno de los números era 0 y no se puede definir un mcd convencional
    if mcd == 0:
        print(f"{n1} y {n2} no poseen máximo común divisor")
    else:
        print(f"El máximo común divisor entre {n1} y {n2} es {mcd}")
# Caso en el que uno de los números es par y el otro impar
else:
    # Si alguno de los números es 0, se establece el mcm (mínimo común múltiplo) en 0
    if n1 == 0 or n2 == 0:
        mcm = 0
    # Si los números son diferentes
    elif n1 != n2:
        # Se determina cuál de los dos números es mayor y se asigna a la variable 'max'
        if n1 > n2:
            max = n1
        else:
            max = n2
        # Se recorre desde el producto de n1 y n2 hasta el mayor de ellos, en orden descendente
        for i in range(n1 * n2, max - 1, -1):
            # Si i es múltiplo de ambos números
            if i % n1 == 0 and i % n2 == 0:
                mcm = i  # Se actualiza mcm con el múltiplo común actual encontrado
    # Si ambos números son iguales, el mcm es el mismo número
    else:
        mcm = n1
    # Se imprime el resultado del mínimo común múltiplo
    print(f"El mínimo común múltiplo entre {n1} y {n2} es {mcm}")