from CONSTANTES import *
from main import pantalla
import numpy as np
import pygame

# ------------------Crear Matriz para Piezas------------------ #

mPiezas = np.zeros((FILAS,COLS))
# Piezas Negras
mPiezas[0] = [4.0, 2.0, 3.0, 5.0, 6.0, 3.0, 2.0, 4.0] # 4: Torre - 2: Caballo - 3: Alfil - 5: Dama - 6: Rey
mPiezas[1] = [1.0] * 8 # Peones
# Piezas Blancas
mPiezas[6] = [1.1] * 8 # Peones
mPiezas[7] = [4.1, 2.1, 3.1, 5.1, 6.1, 3.1, 2.1, 4.1] # 4: Torre - 2: Caballo - 3: Alfil - 5: Dama - 6: Rey
print("Matriz Piezas")
print(mPiezas)

# -------------------Definir y Rescalar imágenes de las piezas----------------- #

# Definir y Escalar Peones
pB = pygame.image.load("assets/piezas/PEON_BLANCO.png")
pB = pygame.transform.scale(pB, (TAM_CASILLA - 14, TAM_CASILLA - 14))
pN = pygame.image.load("assets/piezas/PEON_NEGRO.png")
pN = pygame.transform.scale(pN, (TAM_CASILLA - 14, TAM_CASILLA - 14))

# Definir y Escalar Torres
tB = pygame.image.load("assets/piezas/TORRE_BLANCA.png")
tB = pygame.transform.scale(tB, (TAM_CASILLA - 10, TAM_CASILLA - 10))
tN = pygame.image.load("assets/piezas/TORRE_NEGRA.png")
tN = pygame.transform.scale(tN, (TAM_CASILLA - 10, TAM_CASILLA - 10))

# Definir y Escalar Caballos
cB = pygame.image.load("assets/piezas/CABALLO_BLANCO.png")
cB = pygame.transform.scale(cB, (TAM_CASILLA - 10, TAM_CASILLA - 10))
cN = pygame.image.load("assets/piezas/CABALLO_NEGRO.png")
cN = pygame.transform.scale(cN, (TAM_CASILLA - 10, TAM_CASILLA - 10))

# Definir y Escalar Alfiles
aB = pygame.image.load("assets/piezas/ALFIL_BLANCO.png")
aB = pygame.transform.scale(aB, (TAM_CASILLA - 6, TAM_CASILLA - 6))
aN = pygame.image.load("assets/piezas/ALFIL_NEGRO.png")
aN = pygame.transform.scale(aN, (TAM_CASILLA - 6, TAM_CASILLA - 6))

# Definir y Escalar Damas
dB = pygame.image.load("assets/piezas/DAMA_BLANCA.png")
dB = pygame.transform.scale(dB, (TAM_CASILLA - 6, TAM_CASILLA - 6))
dN = pygame.image.load("assets/piezas/DAMA_NEGRA.png")
dN = pygame.transform.scale(dN, (TAM_CASILLA - 6, TAM_CASILLA - 6))

# Definir y Escalar Reyes
rB = pygame.image.load("assets/piezas/REY_BLANCO.png")
rB = pygame.transform.scale(rB, (TAM_CASILLA - 6, TAM_CASILLA - 6))
rN = pygame.image.load("assets/piezas/REY_NEGRO.png")
rN = pygame.transform.scale(rN, (TAM_CASILLA - 6, TAM_CASILLA - 6))

# -------------------Función Dibujar Piezas----------------- #

def dibujarPiezas(A):
    filas, cols = A.shape
    for i in range(filas):
        for j in range(cols):
            
            # Dibujar Peones
            if A[i,j] == 1.0:
                pantalla.blit(pN, (j*TAM_CASILLA + 7 + DESFASE_LADO, i*TAM_CASILLA + 7 + DESFASE_LADO))
            elif A[i,j] == 1.1:
                pantalla.blit(pB, (j*TAM_CASILLA + 7 + DESFASE_LADO, i*TAM_CASILLA + 7 + DESFASE_LADO))
            
            # Dibujar Torres
            elif A[i,j] == 4.0:
                pantalla.blit(tN, (j*TAM_CASILLA + 5 + DESFASE_LADO, i*TAM_CASILLA + 5 + DESFASE_LADO))
            elif A[i,j] == 4.1:
                pantalla.blit(tB, (j*TAM_CASILLA + 5 + DESFASE_LADO, i*TAM_CASILLA + 5 + DESFASE_LADO))
            
            # Dibujar Caballos
            elif A[i,j] == 2.0:
                pantalla.blit(cN, (j*TAM_CASILLA + 5 + DESFASE_LADO, i*TAM_CASILLA + 5 + DESFASE_LADO))
            elif A[i,j] == 2.1:
                pantalla.blit(cB, (j*TAM_CASILLA + 5 + DESFASE_LADO, i*TAM_CASILLA + 5 + DESFASE_LADO))
            
            # Dibujar Alfiles
            elif A[i,j] == 3.0:
                pantalla.blit(aN, (j*TAM_CASILLA + 3 + DESFASE_LADO, i*TAM_CASILLA + 3 + DESFASE_LADO))
            elif A[i,j] == 3.1:
                pantalla.blit(aB, (j*TAM_CASILLA + 3 + DESFASE_LADO, i*TAM_CASILLA + 3 + DESFASE_LADO))
            
            # Dibujar Damas
            elif A[i,j] == 5.0:
                pantalla.blit(dN, (j*TAM_CASILLA + 3 + DESFASE_LADO, i*TAM_CASILLA + 3 + DESFASE_LADO))
            elif A[i,j] == 5.1:
                pantalla.blit(dB, (j*TAM_CASILLA + 3 + DESFASE_LADO, i*TAM_CASILLA + 3 + DESFASE_LADO))
            
            # Dibujar Reyes
            elif A[i,j] == 6.0:
                pantalla.blit(rN, (j*TAM_CASILLA + 3 + DESFASE_LADO, i*TAM_CASILLA + 3 + DESFASE_LADO))
            elif A[i,j] == 6.1:
                pantalla.blit(rB, (j*TAM_CASILLA + 3 + DESFASE_LADO, i*TAM_CASILLA + 3 + DESFASE_LADO))

# ------------------------------------ #