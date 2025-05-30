from CONSTANTES import *
from piezas import *
import sys, pygame
import numpy as np

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ajedrez Derivagos')

# Reloj para controlar FPS
clock = pygame.time.Clock()

# ------------------Crear Matriz para Tablero------------------ #
mTablero = np.zeros((FILAS, COLS))
for i in range(FILAS):
    for j in range(COLS):
        # Pintar tablero estilo ajedrez
        mTablero[i, j] = 1 if (i + j) % 2 == 0 else 0

print('Matriz Tablero')
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
    
    x, y, z, w = map(int, (x, y, z, w))
    pieza = A[x, y]
    
    if A[z,w] == 0:
        # Movimiento peones negros (1.0)
        if pieza == 1.0:
            # Un paso adelante
            if z == x + 1 and y == w:
                A[z, w] = pieza
                A[x, y] = 0
                return True
            # Dos pasos desde posición inicial
            elif z == x + 2 and y == w and x == 1 and A[x+1,y] == 0:
                A[z, w] = pieza
                A[x, y] = 0
                return True
        # Movimiento peones blancos (1.1)
        elif pieza == 1.1:
            # Un paso adelante
            if z == x - 1 and y == w:
                A[z, w] = pieza
                A[x, y] = 0
                return True
            # Dos pasos desde posición inicial
            elif z == x - 2 and y == w and x == 6 and A[x-1,y] == 0:
                A[z, w] = pieza
                A[x, y] = 0
                return True
        # Movimiento caballo blanco y negro
        elif pieza == 2.0 or pieza == 2.1:
            if ((z == x + 2 or z == x - 2) and (w == y + 1 or w == y - 1)) or ((z == x + 1 or z == x - 1) and (w == y + 2 or w == y - 2)):
                A[z, w] = pieza
                A[x, y] = 0
                return True
        print(f"pos1: {(x,y)}, pos2: {(z,w)}")
    # Si no se movió la pieza, devolver false
    return False

# -------------------Función principal----------------- #

def main():
    global seleccion, selecPieza, pos1, pos2, cont, turno
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
                if mPiezas[int(fila),int(col)] - int(mPiezas[int(fila),int(col)]) == 0 and turno == "negro":
                    for area in posPiezas:
                        if area.collidepoint(event.pos):
                            seleccion = (fila, col)
                            selecPieza = True
                    
                elif mPiezas[int(fila),int(col)] - int(mPiezas[int(fila),int(col)]) != 0 and turno == "blanco":
                    for area in posPiezas:
                        if area.collidepoint(event.pos):
                            seleccion = (fila, col)
                            selecPieza = True
                
                print(f"selecpieza? {selecPieza}")
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
                    cont = 1
        # Dibujado
        pantalla.fill((20, 20, 20))
        dibujarTablero(mTablero, seleccion)
        posPiezas.clear()
        dibujarPiezas(mPiezas)
        
        if pos1 != (0,0) and pos2 != (0,0):
            if moverPieza(mPiezas):
                if turno == "blanco":
                    turno = "negro" 
                else:
                    turno = "blanco"
            pos1 = (0,0)
            pos2 = (0,0)
        
        pygame.display.flip()
        clock.tick(FPS)
        

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    print("Fin")
