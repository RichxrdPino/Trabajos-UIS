from CONSTANTES import *
from piezas import *
import sys, pygame
import numpy as np

# Inicialización de Pygame\pygame.init()
pygame.init()

# Configuración de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('"Ajedrez" Derivagos')

# Reloj para controlar FPS
clock = pygame.time.Clock()

# ------------------Crear Matriz para Tablero------------------ #

mTablero = np.zeros((FILAS,COLS))
for i in range(FILAS):
    for j in range(COLS):
        if (i + j) % 2 == 0:
            mTablero[i,j] = 1
print("Matriz Tablero")
print(mTablero)

# -------------------Función Dibujar Tablero----------------- #

def dibujarTablero(A):
    filas, cols = A.shape
    for i in range(filas):
        for j in range(cols):
            pygame.draw.rect(pantalla, WHITE if (i + j) % 2 == 0 else BLACK, pygame.Rect(i*TAM_CASILLA + DESFASE_LADO, j*TAM_CASILLA + DESFASE_LADO, TAM_CASILLA, TAM_CASILLA))

# -------------------Función principal----------------- #

def main():
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lógica del juego
        # TODO: actualizar objetos, detectar colisiones, etc.

        # Dibujado
        pantalla.fill((20,20,20))
        # TODO: dibujar objetos, UI, etc.
        dibujarTablero(mTablero)
        dibujarPiezas(mPiezas)
        
        # Actualizar pantalla
        pygame.display.flip()
        # Controlar FPS
        clock.tick(FPS)

    # Salida limpia
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    print("Fin")