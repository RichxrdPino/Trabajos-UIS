#Programa que enuncie las instrucciones para resolver las torres de hanoi con n piezas

n = int(input("Número de piezas: "))

# Definir cada torre com una lista
torre1 = []
torre2 = []
torre3 = []

#* Gráfica del problema y rellenar las torres

for i in range(1,n+1):
    torre1.append(i)
    torre2.append(0)
    torre3.append(0)
    print(" |         |       |")
    print(f" {i}         |       |")
print(" |         |       |")
print("~~~       ~~~     ~~~")

print(f"{torre1}   {torre2}  {torre3}")
