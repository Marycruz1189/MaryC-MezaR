import pygame, sys, time
from pygame.locals import *
from random import randint, choice
from constantes import *
from configuracion import *

#Cargamos la informacion de los sonidos

def cargar_sonidos (sonidos):

    sonido_fondo = pygame.mixer.Sound("audio/"+SONIDO_FONDO)
    sonidos.append(sonido_fondo)

    sonido_sonar = pygame.mixer.Sound("audio/"+SONIDO_SONAR)
    sonidos.append(sonido_sonar)
     
    sonido_miss = pygame.mixer.Sound("audio/"+SONIDO_MISS)
    sonidos.append(sonido_miss)

    sonido_acierto = pygame.mixer.Sound("audio/"+SONIDO_ACIERTO)
    sonidos.append(sonido_acierto)

    sonido_explosion = pygame.mixer.Sound("audio/"+SONIDO_EXPLOSION)
    sonidos.append(sonido_explosion)

    sonido_crash = pygame.mixer.Sound("audio/"+SONIDO_CRASH)
    sonidos.append(sonido_crash)


def cargar_textos(textos):

    fuente_de_texto = pygame.font.Font("fuentes/PressStart2P.ttf", 11)
    textos.append(fuente_de_texto)

    tus_barcos = fuente_de_texto.render(TEXTO_BARCOS, True, BLANCO)
    textos.append(tus_barcos)
    
    barcos_oponentes = fuente_de_texto.render(TEXTO_OPONENTE, True, BLANCO)
    textos.append(barcos_oponentes)
    
    texto_activos = fuente_de_texto.render(TEXTO_ACTIVOS, True, BLANCO)
    textos.append(texto_activos)

    texto_informaciones = fuente_de_texto.render(TEXTO_INFORMACIONES, True, BLANCO)
    textos.append(texto_informaciones)


def actualizar_textos (ventana, textos, b_jug, b_cpu):

    barcos_jugador = textos[0].render(str(b_jug), True, BLANCO)
    barcos_oponentes = textos[0].render(str(b_cpu), True, BLANCO)

    ventana.blit(textos[1],(250,10))
    ventana.blit(barcos_jugador,(400,10))

    ventana.blit(textos[2],(500,10))
    ventana.blit(barcos_oponentes,(750,10))


#Dibujamos los barcos en el hud
def dibujar_barcos(ventana, imagenes):

    borde = BORDE_INICIAL

    for i, j in INFO_BARCOS.items():
        posicionado = j[0][0] 
        if (posicionado == 1):
            ventana.blit(imagenes[i], (borde + 200 - imagenes[i].get_width() / 2, 30))
            borde+=140

#Cremos una grilla con elementos 0
def inicializar_tablero (tablero):
    
    for fila in range(10):
        tablero.append([])
        for columna in range(10):
            tablero[fila].append(0)


#actualizamos la informacion del diccionario principal para volver activos los barcos nuevamente
def reiniciar_info ():

    INFO_BARCOS["A"][0][0] = 1
    INFO_BARCOS["B"][0][0] = 1
    INFO_BARCOS["C"][0][0] = 1
    INFO_BARCOS["D"][0][0] = 1
    INFO_BARCOS["E"][0][0] = 1



#nos permite dibujar la informacion de los evento de la grilla en la pantalla

def dibujar_tablero (ventana, tablero, fila, columna, dx, dy, c):

    #Esta funcion permite dibujar todo tipo de acontecimientos ocurridos en la grilla. Por esta razon los distintos eventos se etiquetan de manera diferente tal como se puede apreciar en configuraciones.py. Cuando disparas a un barco, cuando un disparo cae al agua, cuando estas posicionando tus barcos o cuando has disparado sobre una grilla sin saber si habia o no barco, todos estos elementos tienen una etiqueta diferente.

    for fila in range(10):
        for columna in range(10):
            color = AZUL
            if tablero[fila][columna] != 0:
                if (tablero[fila][columna] == BARCO1 or tablero[fila][columna] == BARCO2 or tablero[fila][columna] == BARCO3 or tablero[fila][columna] == BARCO4 or tablero[fila][columna] == BARCO5):
	    	    #posicion de tus barcos iniciales
                    color = MORADO 				
                elif (tablero[fila][columna] == MISS):
		            #disparo fallido
                    color = COLORMISS
                elif (tablero[fila][columna] == HIT):
		            #disparo acertado
                    color = COLORHIT
                else:
		            #disparo en espera
                    color = c
            
            pygame.draw.rect(ventana, color, [(MARGEN+LARGO)*columna+MARGEN+dx,(MARGEN+ALTO)*fila+MARGEN+dy,LARGO,ALTO])

#funcion que permite cargar sonidos por cada disparo
def sonido_disparos (ventana, hud, imagen_cursor, tablero, disparos, sonidos, jugadas): 
 
    if (disparos[0] == DISPARO_AGUA):
        sonidos[2].play()
        time.sleep(2)	 
    else:
        sonidos[3].play()
        time.sleep(2)
	
    if (jugadas % 2 == 0):
        dibujar_tablero(ventana, tablero, disparos[1][0], disparos[1][1], DX, DY, AMARILLO)
    else:
        dibujar_tablero(hud, tablero, disparos[1][0], disparos[1][1], 0, 0, AMARILLO)
  	
    ventana.blit(hud, (30,30))
    
    x, y = pygame.mouse.get_pos()
    x -= RADIO_CURSOR
    y -= RADIO_CURSOR
   
    ventana.blit(imagen_cursor, (x, y))
  
    pygame.display.update()
  
