from CONSTANTES import *
from piezas import *
import sys, pygame
import numpy as np

# Inicialización de Pygame
pygame.init()
pygame.mixer.init()

# Configuración de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ajedrez Derivagos')

# Fuente de un texto
fuente = pygame.font.SysFont("Arial", 24)
# Textos para mostrar los puntos
textoPntsBlanco = fuente.render(f"+{pntB}", True, WHITE)
textoPntsNegro = fuente.render(f"+{pntN}", True, WHITE)
# Posición de los textos
pos_textoPntsBlanco = (0,ALTO - 54)
pos_textoPntsNegro = (0,20)

# Sonido mover pieza
sndMoverPieza = pygame.mixer.Sound("assets/sonidos/moverPieza.mp3")
sndMoverPieza.set_volume(0.1)

# Música de fondo
pygame.mixer.music.load("assets/sonidos/musicaFondo.mp3")
pygame.mixer.music.set_volume(0.02)
pygame.mixer.music.play(-1)

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
                
def moverPieza2(pieza2):
    global pntB, pntN, turno
    if turno == "blanco":
        pntB = pntB + int(pieza2)
    else:
        pntN = pntN + int(pieza2)
    print(f"Blancas: +{pntB}")
    print(f"Negras: +{pntN}")

# -------------------Función Mover Pieza ----------------- #

def moverPieza(A):
    global reyInicialB, torreInicial_1B, torreInicial_2B, reyInicialN, torreInicial_1N, torreInicial_2N, pntB, pntN
    x, y = pos1
    z, w = pos2
    
    x, y, z, w = map(int, (x, y, z, w))
    pieza = A[x, y]
    
    try:
        # Movimiento peones negros (1.0)
        if pieza == 1.0:
            # Si está vacío
            if A[z,w] == 0:
                # Un paso adelante
                if z == x + 1 and y == w:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True
                # Dos pasos desde posición inicial
                elif z == x + 2 and y == w and x == 1 and A[x+1,y] == 0:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True
            else:
                # Captura diagonal
                if (z == x + 1 and w == y + 1) or (z == x + 1 and w == y - 1):
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True

        # Movimiento peones blancos (1.1)
        elif pieza == 1.1:
            if A[z,w] == 0:
                # Un paso adelante
                if z == x - 1 and y == w:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True
                # Dos pasos desde posición inicial
                elif z == x - 2 and y == w and x == 6 and A[x-1,y] == 0:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True
            else:
                # Captura diagonal
                if (z == x - 1 and w == y + 1) or (z == x - 1 and w == y - 1):
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True
        # Movimiento caballo blanco y negro
        if pieza == 2.0 or pieza == 2.1:
            if ((z == x + 2 or z == x - 2) and (w == y + 1 or w == y - 1)) or ((z == x + 1 or z == x - 1) and (w == y + 2 or w == y - 2)):
                moverPieza2(A[z, w])
                A[z, w] = pieza
                A[x, y] = 0
                return True
        # Movimiento de alfil negro
        if A[x, y] == 3.0:
            if abs(z - x) == abs(w - y):  # Movimiento diagonal
                dx = 1 if z > x else -1
                dy = 1 if w > y else -1
                libre = True
                for i in range(1, abs(z - x)):
                    if A[x + i * dx, y + i * dy] != 0:
                        libre = False
                        break
                if libre:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True

        # Movimiento de alfil blanco
        if A[x, y] == 3.1:
            if abs(z - x) == abs(w - y):  # Movimiento diagonal
                dx = 1 if z > x else -1
                dy = 1 if w > y else -1
                libre = True
                for i in range(1, abs(z - x)):
                    if A[x + i * dx, y + i * dy] != 0:
                        libre = False
                        break
                if libre:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True
        
        # Movimiento de torre negra
        if A[x, y] == 4.0:
            if x == z or y == w:
                dx = 0 if x == z else (1 if z > x else -1)
                dy = 0 if y == w else (1 if w > y else -1)
                libre = True
                i = 1
                while (x + i*dx != z or y + i*dy != w):
                    if A[x + i*dx, y + i*dy] != 0:
                        libre = False
                        break
                    i += 1
                
                if libre:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    if (x == 0 and y == 0):
                        torreInicial_1N = False
                    elif (x == 0 and y == 7):
                        torreInicial_2N = False
                    return True

        # Movimiento de torre blanca
        if A[x, y] == 4.1:
            if x == z or y == w:
                dx = 0 if x == z else (1 if z > x else -1)
                dy = 0 if y == w else (1 if w > y else -1)
                libre = True
                i = 1
                while (x + i*dx != z or y + i*dy != w):
                    if A[x + i*dx, y + i*dy] != 0:
                        libre = False
                        break
                    i += 1
                if libre:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    if (x == 7 and y == 0):
                        torreInicial_1B = False
                    elif (x == 7 and y == 7):
                        torreInicial_2B = False
                    return True
        
        # Movimiento de rey negro
        if A[x, y] == 6.0:
            if abs(z - x) <= 1 and abs(w - y) <= 1:
                moverPieza2(A[z, w])
                A[z, w] = pieza
                A[x, y] = 0
                reyInicialN = False
                return True
            
            # Lógica del enrroque
            elif (z == x and w == y + 2) and A[x,y+1] == 0 and torreInicial_2N and reyInicialN:
                A[z, w] = pieza
                A[x, y] = 0
                A[x,y+1] = A[x,y+3]
                A[x,y+3] = 0
                torreInicial_2N = False
                reyInicialN = False
                return True
            elif ((z == x and w == y - 2) or (z == x and w == y - 3)) and A[x,y-1] == 0 and A[x,y-2] == 0 and torreInicial_1N and reyInicialN:
                A[x, y-2] = pieza
                A[x, y] = 0
                A[x,y-1] = A[x,y-4]
                A[x,y-4] = 0
                return True
        # Movimiento de rey blanco
        if A[x, y] == 6.1:
            if abs(z - x) <= 1 and abs(w - y) <= 1:
                moverPieza2(A[z, w])
                A[z, w] = pieza
                A[x, y] = 0
                reyInicialB = False
                return True
            
            # Lógica del enrroque
            elif (z == x and w == y + 2) and A[x,y+1] == 0 and torreInicial_2B and reyInicialB:
                A[z, w] = pieza
                A[x, y] = 0
                A[x,y+1] = A[x,y+3]
                A[x,y+3] = 0
                return True
            elif ((z == x and w == y - 2) or (z == x and w == y - 3)) and A[x,y-1] == 0 and A[x,y-2] == 0 and torreInicial_1B and reyInicialB:
                A[x, y-2] = pieza
                A[x, y] = 0
                A[x,y-1] = A[x,y-4]
                A[x,y-4] = 0
                return True
        # Movimiento de dama negra
        if A[x, y] == 5.0:
            if abs(z - x) == abs(w - y) or x == z or y == w:
                dx = 0 if x == z else (1 if z > x else -1)
                dy = 0 if y == w else (1 if w > y else -1)
                libre = True
                i = 1
                while (x + i*dx != z or y + i*dy != w):
                    if A[x + i*dx, y + i*dy] != 0:
                        libre = False
                        break
                    i += 1
                if libre:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True

        # Movimiento de dama blanca
        if A[x, y] == 5.1:
            if abs(z - x) == abs(w - y) or x == z or y == w:
                dx = 0 if x == z else (1 if z > x else -1)
                dy = 0 if y == w else (1 if w > y else -1)
                libre = True
                i = 1
                while (x + i*dx != z or y + i*dy != w):
                    if A[x + i*dx, y + i*dy] != 0:
                        libre = False
                        break
                    i += 1
                if libre:
                    moverPieza2(A[z, w])
                    A[z, w] = pieza
                    A[x, y] = 0
                    return True      
    except:
        print("Fuera del tablero")
    # Si no se movió la pieza, devolver false
    return False

# -------------------Función principal----------------- #

def main():
    global seleccion, selecPieza, pos1, pos2, cont, turno, pntB, pntN
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
                try:
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
                except:
                    print("Fuera del tablero")
                
                if selecPieza:
                    pos1 = (fila, col)
                    pos2 = (-1,-1)
                    cont = 0
                    cont = cont + 1
                elif 0 < cont < 3:
                    pos2 = (fila,col)
                else:
                    pos1 = (-1,-1)
                    pos2 = (-1,-1)
                    cont = 1
        # Dibujado
        pantalla.fill((20, 20, 20))
        dibujarTablero(mTablero, seleccion)
        posPiezas.clear()
        dibujarPiezas(mPiezas)
        
        # Mostrar puntos de cada jugador
        textoPntsBlanco = fuente.render(f"+{pntB}", True, WHITE)
        textoPntsNegro = fuente.render(f"+{pntN}", True, WHITE)
        pantalla.blit(textoPntsBlanco, pos_textoPntsBlanco)
        pantalla.blit(textoPntsNegro, pos_textoPntsNegro)
        
        if pos1 != (-1,-1) and pos2 != (-1,-1):
            if moverPieza(mPiezas):
                sndMoverPieza.play()
                if turno == "blanco":
                    turno = "negro" 
                else:
                    turno = "blanco"
            pos1 = (-1,-1)
            pos2 = (-1,-1)
        
        pygame.display.flip()
        clock.tick(FPS)
        

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    print("Fin")
