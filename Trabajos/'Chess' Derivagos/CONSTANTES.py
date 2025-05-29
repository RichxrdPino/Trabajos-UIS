# Configuración de la ventana

FILAS, COLS = 8, 8
TAM_CASILLA = 80
DESFASE_CASILLAS = 60
DESFASE_LADO = DESFASE_CASILLAS / 2
ANCHO, ALTO = TAM_CASILLA*COLS + DESFASE_CASILLAS, TAM_CASILLA*FILAS + DESFASE_CASILLAS
FPS = 60

# Colores

WHITE = (228, 228, 228)
BLACK = (27, 27, 27)
AMARILLO = (253, 253, 150)
AMARILLO_OSCURO = (153, 153, 50)

# Otros (No necesariamente constantes)

posPiezas = []
seleccion = None
selecPieza = False

pos1, pos2 = (0,0), (0,0)
cont = 0
