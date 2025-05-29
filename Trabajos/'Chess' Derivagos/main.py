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

def moverPieza(A):
    x, y = pos1
    z, w = pos2
    
    x = int(x)
    y = int(y)
    z = int(z)
    w = int(w)
    
    if A[x, y] == 1.0:
        if z == x+1 and y == w:
            A[z,w] = A[x, y]
            A[x, y] = 0
        elif z == x+2 and y == w and x == 1:
            A[z,w] = A[x, y]
            A[x, y] = 0
            
    if A[x, y] == 1.1:
        if z == x-1 and y == w:
            A[z,w] = A[x, y]
            A[x, y] = 0
        elif z == x-2 and y == w and x == 6:
            A[z,w] = A[x, y]
            A[x, y] = 0
            
    

# -------------------Función principal----------------- #

def main():
    global seleccion, selecPieza, pos1, pos2, cont
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            # Evento cerrar ventana
            if event.type == pygame.QUIT:
                running = False

            # Evento click
            if event.type == pygame.MOUSEBUTTONDOWN:
                seleccion = None # Reinicializar seleccion
                selecPieza = False # Reinicializar si hay o no una pieza selecionada
                x, y = event.pos # Guardar posición del click
                # Guardar fila y columna de la selección
                col = (x - DESFASE_LADO) // TAM_CASILLA
                fila = (y - DESFASE_LADO) // TAM_CASILLA
                cont = cont + 1
                        
                # comprobamos que esté dentro del tablero
                for area in posPiezas:
                    if area.collidepoint(event.pos):
                        seleccion = (fila, col)
                        selecPieza = True
                        
                if selecPieza:
                    pos1 = (fila, col)
                    pos2 = (0,0)
                    cont = 0
                    cont = cont + 1
                elif 0 < cont < 3:
                    pos2 = (fila,col)
                else:
                    pos1 = (0,0)
                    pos2 = (0,0)
                    cont = 0
                print(f"pos1: {pos1}, pos2: {pos2}")
                
        # Dibujado
        pantalla.fill((20, 20, 20))
        dibujarTablero(mTablero, seleccion)
        posPiezas.clear()
        dibujarPiezas(mPiezas)
        
        if pos1 != (0,0) and pos2 != (0,0):
            moverPieza(mPiezas)
            pos1 = (0,0)
            pos2 = (0,0)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    print("Fin")
