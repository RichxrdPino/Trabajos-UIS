from CONSTANTES import *
from main import pantalla
import numpy as np
import pygame

# ------------------Crear Matriz para Piezas------------------ #
mPiezas = np.zeros((FILAS, COLS))
# Piezas Negras
mPiezas[0] = [4.0, 2.0, 3.0, 5.0, 6.0, 3.0, 2.0, 4.0]  # Torre, Caballo, Alfil, Dama, Rey
mPiezas[1] = [1.0] * 8  # Peones
# Piezas Blancas
mPiezas[6] = [1.1] * 8 # Peones
mPiezas[7] = [4.1, 2.1, 3.1, 5.1, 6.1, 3.1, 2.1, 4.1] # Torre, Caballo, Alfil, Dama, Rey
print("Matriz Piezas")
print(mPiezas)

# -------------------Carga y escalado de imágenes----------------- #

def cargar_textura(nombre, tamaño):
    img = pygame.image.load(f"assets/piezas/{nombre}.png")
    return pygame.transform.scale(img, tamaño)

# Tamaños
TAM_PEON = (TAM_CASILLA - 14, TAM_CASILLA - 14)
TAM_OTRAS = (TAM_CASILLA - 6,  TAM_CASILLA - 6)
# Desfases
OFF_PEON = (7 + DESFASE_LADO, 7 + DESFASE_LADO)
OFF_TDG  = (3 + DESFASE_LADO, 3 + DESFASE_LADO)
OFF_TC   = (5 + DESFASE_LADO, 5 + DESFASE_LADO)

# Diccionario: código → (imagen, tamaño, desfase)
PIEZAS = {
    1.0: (cargar_textura("PEON_NEGRO", TAM_PEON), TAM_PEON, OFF_PEON),
    1.1: (cargar_textura("PEON_BLANCO", TAM_PEON), TAM_PEON, OFF_PEON),
    4.0: (cargar_textura("TORRE_NEGRA", TAM_OTRAS), TAM_OTRAS, OFF_TC),
    4.1: (cargar_textura("TORRE_BLANCA", TAM_OTRAS), TAM_OTRAS, OFF_TC),
    2.0: (cargar_textura("CABALLO_NEGRO", TAM_OTRAS), TAM_OTRAS, OFF_TC),
    2.1: (cargar_textura("CABALLO_BLANCO", TAM_OTRAS), TAM_OTRAS, OFF_TC),
    3.0: (cargar_textura("ALFIL_NEGRO", TAM_OTRAS), TAM_OTRAS, OFF_TDG),
    3.1: (cargar_textura("ALFIL_BLANCO", TAM_OTRAS), TAM_OTRAS, OFF_TDG),
    5.0: (cargar_textura("DAMA_NEGRA", TAM_OTRAS), TAM_OTRAS, OFF_TDG),
    5.1: (cargar_textura("DAMA_BLANCA", TAM_OTRAS), TAM_OTRAS, OFF_TDG),
    6.0: (cargar_textura("REY_NEGRO", TAM_OTRAS), TAM_OTRAS, OFF_TDG),
    6.1: (cargar_textura("REY_BLANCO", TAM_OTRAS), TAM_OTRAS, OFF_TDG),
}

# -------------------Función Dibujar Piezas----------------- #

def dibujarPiezas(A):
    filas, cols = A.shape
    for i in range(filas):
        for j in range(cols):
            if A[i, j] != 0:
                img, (w, h), (dx, dy) = PIEZAS[A[i, j]] # Asignar valor correspondiente en el diccionario
                
                # Posición de la pieza
                x = j * TAM_CASILLA + dx
                y = i * TAM_CASILLA + dy

                # Área de la pieza y agregación a posPiezas
                area = pygame.Rect((x, y), (w, h))
                posPiezas.append(area)

                # Dibujar
                pantalla.blit(img, (x, y))
