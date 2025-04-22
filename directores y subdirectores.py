import os
import pathlib


# Métodos en Python para crear directores y subdirectores:

# Tipos: os - pathlib


# Crea un directorio y sus subdirectorios
os.makedirs("directorio1/subdirectorio1", exist_ok=True)
#pathlib.Path("directorio2/subdirectorio2").mkdir(parents=True,exist_ok=True)

#Listar archivos y directorios en un directorio
for item in os.listdir("directorio1"):
    print(item)