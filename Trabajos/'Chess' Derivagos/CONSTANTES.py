# Configuración de la ventana

FILAS, COLS = 8, 8
TAM_CASILLA = 80
DESFASE_CASILLAS = 55
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
pos1, pos2 = (-1,-1), (-1,-1)
cont = 0
turno = "blanco"

# Registro de si el rey blanco o negro o alguna torre blanca o negra se han movido
reyInicialB = True
torreInicial_1B = True
torreInicial_2B = True

reyInicialN = True
torreInicial_1N = True
torreInicial_2N = True

#Puntos Blanco y Negro
pntB = 0
pntN = 0
