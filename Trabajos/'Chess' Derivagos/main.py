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

# -------------------Función Dibujar Tablero y Selección de pieza----------------- #

def dibujarTablero(A, seleccion=None):
    filas, cols = A.shape
    for i in range(filas):
        for j in range(cols):
            rect = pygame.Rect(i*TAM_CASILLA + DESFASE_LADO, j*TAM_CASILLA + DESFASE_LADO, TAM_CASILLA, TAM_CASILLA)
            
            if seleccion == (j, i):
                pygame.draw.rect(pantalla, AMARILLO, rect)
                pygame.draw.rect(pantalla, AMARILLO_OSCURO, rect, 3)
            else:
                # coloreado normal (ejemplo: chessboard)
                pygame.draw.rect(pantalla, WHITE if (i + j) % 2 == 0 else BLACK, rect)

# -------------------Función Mover Pieza ----------------- #

def moverPieza(A, pos1, pos2):
    print(" :( ")
    
# -------------------Función principal----------------- #

def main():
    global seleccion, selecPieza
    running = True
    while running:
        # 1) Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                seleccion = None # Reinicializar seleccion
                selecPieza = False
                x, y = event.pos
                col = (x - DESFASE_LADO) // TAM_CASILLA
                fila = (y - DESFASE_LADO) // TAM_CASILLA
                # comprobamos que esté dentro del tablero
                for area in posPiezas:
                    print(area.collidepoint(event.pos))
                    if area.collidepoint(event.pos):
                        seleccion = (fila, col)
                        selecPieza = True
        # Dibujado
        pantalla.fill((20, 20, 20))
        dibujarTablero(mTablero, seleccion)
        posPiezas.clear()
        dibujarPiezas(mPiezas)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    print("Fin")
