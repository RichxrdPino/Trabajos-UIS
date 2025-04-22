from genericpath import exists
import os
import pathlib


# Métodos en Python para crear directores y subdirectores:

# Tipos: os - pathlib


# Crea un directorio y sus subdirectorios
#for i in range(10):
#    os.makedirs(f"directorio1/subdirectorio{i}", exist_ok=True)

#for j in range(10):
#   pathlib.Path(f"directorio2/subdirectorio{j}").mkdir(parents=True,exist_ok=True)

# Verificar si el directorio existe
if os.path.exists("directorio1"): #Boolean
    print("El directorio existe")
    
    #Listar archivos y directorios en un directorio
    for item in os.listdir("directorio1"): #Arreglo
        print(item)

    # Obtener la ruta absoluta del directorio
    ruta = os.path.abspath("directorio1")
    print(f"La ruta absoluta del directorio1 es: {ruta}")

else:
    print("El directorio no existe")