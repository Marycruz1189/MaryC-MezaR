#!usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *

#Informacion de los barcos

IMAGENES_BARCOS = {
"A": "barco_A.png",
"B": "barco_B.png",
"C": "barco_C.png",
"D": "barco_D.png",
"E": "barco_E.png",
}

INFO_BARCOS = {
"A": [[1,1],[1,1]],
"B": [[1,2],[1,2]],
"C": [[1,3],[1,3]],
"D": [[1,4],[1,4]],
"E": [[1,5],[1,5]],
}


# Titulo de la ventana.
TITULO_VENTANA = "Combate Naval UTFSM"

#Dimensiones para la pantalla
DIMENSIONES = (800, 600)

# Fondo de pantalla: png o jpeg (800 x 600)
FONDO_JUEGO = "fondo.jpg"


# Imagen de inicio y fin del juego.
IMAGEN_TITULO = "titulo.jpg"
IMAGEN_RESULTADOS = "resultados.jpg"
IMAGEN_GANADOR = "win.jpg"
IMAGEN_PERDEDOR = "lost.jpg"


#Sentido de ubicacion de barcos

NORTE = "NORTE"
OESTE = "OESTE"

#Margen para posicionar los barcos en el hud
BORDE_INICIAL = -20


# Colores para MAPA

COLORMISS = VERDE
COLORHIT = ROJO

# Establecemos el largo y alto de cada celda de la reticula.
LARGO  = 30
ALTO = 30
 
# Establecemos el margen entre las celdas.
MARGEN = 3

#Desplazamientos para posicionar el tablero en la pantalla para proceder a posicionar los barcos
DES_X = 200
DES_Y = 50

#Desplazamiento para posicionar el tablero enemigo en la pantalla, en etapa de disparos
DX = 430
DY = 30

#Cantidad total de turnos
TOTAL_TURNOS = 3

#IMPORTANTE: ver dibujar_tablero
DISPARO_AGUA = 6
MISS = -9
HIT = 9

#Valores asociados a los barcos para ser dibujados
BARCO1 = -1
BARCO2 = -2
BARCO3 = -3
BARCO4 = -4
BARCO5 = -5

SONIDO_SONAR = "sonar.wav"
SONIDO_EXPLOSION = "explosion.ogg"
SONIDO_MISS = "miss.ogg"
SONIDO_ACIERTO = "acierto.ogg"
SONIDO_FONDO = "fondo.ogg"
SONIDO_CRASH = "crash.wav"

# Radio del cursor.
RADIO_CURSOR = 30

# Textos en pantalla.
TEXTO_BARCOS = "Mis barcos: "
TEXTO_OPONENTE = "Barcos oponentes: "

TEXTO_INFORMACIONES = "Barcos en juego "
TEXTO_ACTIVOS = "Activos"

N_BARCOS = 5
