# Construir un programa que lea un entero positivo n y determine si dicho número es un cuadrado de otro
# entero, o sea, que tiene raíz cuadrada entera.

# Determinar el entero positivo
n = int(input("Ingresa un número entero positivo: "))
# Inicializar comprobante de que se halló o no una raíz
noExiste = True
# Definir root como la parte entera de la raíz cuadrada de n
root = int(n**(1/2))

# Recorrer todos los números de 0 hasta root (sea exacta o no)
for i in range(root+1):
    # Iterar i y preguntar si es la raíz o no
    if i*i == n:
        print(f"la raíz cuadrada de {n} es {i}") # Imprimir el valor de la raíz
        noExiste = False # Cambiar el valor del comprobante
    
# Verificar si se encontró o no una raíz e Imprimir la respuesta.
if noExiste:
    print(f"{n} no tiene raíz cuadrada exacta o entera, ya que esta es {n**(1/2)}")