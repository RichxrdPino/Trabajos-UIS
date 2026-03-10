# Construir un programa que lea un entero positivo n y determine si dicho número es un cuadrado de otro
# entero, o sea, que tiene raíz cuadrada entera.

# Determinar el entero positivo
n = int(input("Ingresa un número entero positivo: "))

# Comprobar si la raíz de n tiene parte decimal
if n**(1/2) - int(n**(1/2)) == 0:
    print(f"la raíz cuadrada de {n} es {int(n**(1/2))}") # Si no, imprimir el valor de la raíz
else:
    print(f"{n} no tiene raíz cuadrada exacta o entera, ya que esta es {n**(1/2)}") # Si si, imprimir que no existe raíz entera