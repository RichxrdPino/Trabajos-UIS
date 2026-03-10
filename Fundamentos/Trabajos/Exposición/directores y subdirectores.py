import os


# Métodos en Python para crear directores y subdirectores:

# Tipos: os - pathlib

# Crea un directorio y sus subdirectorios
for i in range(3):
    os.makedirs(f"directorio1/subdirectorio{i}", exist_ok=True)
    for k in range(2):
        os.makedirs(f"directorio1/subdirectorio{i}/queso{k}", exist_ok=True)
        for l in range(1):
            os.makedirs(f"directorio1/subdirectorio{i}/queso{k}/quisito{l}", exist_ok=True)

# Puedes añadir tantos archivos como gustes.

def leer(directorio,nivel=0):

    #Control de tabulaciones
    A = [" "]
    if nivel == 0:
        print(directorio + " (Main Directory)")
    else:
        for i in range(nivel):
            A.append("  ")

    #Para cada elemento dentro del directorio...
    for i in os.listdir(directorio):
        if os.path.isdir(directorio + "/" + i): #Si es un direcotorio imprímelo, ábrelo y leelo añadiendo una tabulación.
            print("".join(A)+i)
            leer(directorio + "/" + i,nivel+1)
        else:                                   #Si es un archivo, imprímelo.
            print("".join(A)+i)



# Verificar si el directorio existe
if os.path.exists("directorio1"): #Boolean
    leer("directorio1")

else:
    print("El directorio no existe")