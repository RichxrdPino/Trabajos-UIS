#LISTA DE 0 HASTA n DIVISIBLES EN 2, 3, O 5

n = int(input("número hasta el que debe llegar la lista: "))

for i in range (n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        print(i)
