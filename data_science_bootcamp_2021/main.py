#!usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, time

from pygame.locals import *
from random import choice, randint
from configuracion import *
from constantes import *
from utilidades import *

#Se importan las funciones del modulo funciones.py
from funciones import *

# Se inicializan los modulos de pygame.
pygame.init()

# Se crea la ventana de juego.
ventana = pygame.display.set_mode(DIMENSIONES)
pygame.display.set_caption(TITULO_VENTANA)
pygame.mouse.set_visible(False)

# Se crean y se cargan los graficos del juego.
fondo_juego = pygame.image.load("img/"+FONDO_JUEGO).convert()
if fondo_juego.get_size() != DIMENSIONES: 
    fondo_juego = pygame.transform.scale(fondo_juego, DIMENSIONES)

#se cargan los graficos de los barcos

imagenes_barcos = dict()

for tipo, archivo in IMAGENES_BARCOS.items():
    imagen = pygame.image.load("img/"+archivo).convert_alpha()

    if imagen.get_size() != (100, 50):
        imagen = pygame.transform.scale(imagen, (100, 50))
        
    imagenes_barcos[tipo] = imagen

# Creacion del cursor.

imagen_cursor = pygame.Surface((RADIO_CURSOR * 2, RADIO_CURSOR * 2))
imagen_cursor.fill(NEGRO)
imagen_cursor.set_colorkey(NEGRO)
pygame.draw.circle(imagen_cursor, ROJO, (RADIO_CURSOR, RADIO_CURSOR), RADIO_CURSOR, 2)
pygame.draw.line(imagen_cursor, ROJO, (0, RADIO_CURSOR), (RADIO_CURSOR - 5, RADIO_CURSOR), 2)
pygame.draw.line(imagen_cursor, ROJO, (RADIO_CURSOR + 5, RADIO_CURSOR), (RADIO_CURSOR * 2, RADIO_CURSOR), 2)
pygame.draw.line(imagen_cursor, ROJO, (RADIO_CURSOR, 0), (RADIO_CURSOR, RADIO_CURSOR - 5), 2)
pygame.draw.line(imagen_cursor, ROJO, (RADIO_CURSOR, RADIO_CURSOR + 5), (RADIO_CURSOR, RADIO_CURSOR * 2), 2)


# Se cargan las fuentes de escritura y se renderizan algunos textos.
textos = []
cargar_textos(textos)

# Se crea el hud (zona que indica los datos de la partida).

fondo_hud = pygame.Surface((800, 100))
fondo_hud.fill(NEGRO)
hud = pygame.Surface((800, 100))
hud.fill(NEGRO)
hud.blit(textos[4],(10, 10))
hud.blit(textos[3], (10, 50))
hud.set_colorkey(NEGRO)


sonidos = []
#cargamos los sonidos
cargar_sonidos(sonidos)

# Inicializacion y parametros de juego.
tipos_barcos = sorted(list(IMAGENES_BARCOS))

# Se muestra la pantalla de titulo.
ventana.blit(fondo_juego, (0, 0))
pygame.display.flip()

# Se espera hasta que el usuario presione la tecla Enter para comenzar.
tiempo_de_juego = -(pygame.time.get_ticks() / 1000.0)
esperando_click = True

while esperando_click:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            esperando_click = False
            break

# Lo usamos para establecer cuan rapido se refresca la pantalla.
reloj = pygame.time.Clock()

# Establecemos el título de la pantalla.
pygame.display.set_caption("Combate Naval - Programación UTFSM")
 
#Iteramos hasta que el usuario pulse el botón de salir.
hecho = False
 
# Lo usamos para establecer cuán rápido de refresca la pantalla.
reloj = pygame.time.Clock()

#sonido del videojuego
sonidos[1].play(-1)

#barcos jugador
tablero_jugador = []  

#barcos oponente
tablero_cpu = []

#auxiliar para disparos del jugador
disparos_jugador = []

#auxiliar para disparos oponente
disparos_cpu = []



#Inicializamos las 4 listas vacias 

inicializar_tablero(tablero_jugador)
inicializar_tablero(tablero_cpu)
inicializar_tablero(disparos_cpu)
inicializar_tablero(disparos_jugador)

#################### CONFIGURACIONE INICIALES ####################
flag = True
barco_actual = 1

comenzar = False
salir = False

fila, columna = (-1,-1)
##################################################################


#Ciclo que permite posicionar tus barcos en el tablero

while not comenzar:
    
    #FPS
    reloj.tick(30)
    
    if (flag == True):
        sentido = NORTE

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
           
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                salir = True
                break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if (flag == True):
                    sentido = OESTE
                    flag = False
                else:
                    sentido = NORTE
                    flag = True

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
		        #Obtenemos los datos de la posicion clickeada en la pantalla
                cursor = (event.pos, RADIO_CURSOR)

		        # Funciones de la tarea.
                fila, columna = completar_tablero(cursor, tablero_jugador, barco_actual, sentido)          
                flag = actualizar_info_posicion(fila,columna,barco_actual)

                if (flag): 	
                    barco_actual+= 1
                    flag = True
	    
		        #Hemos posicionado todos los barcos
                if (barco_actual > 5):
                    comenzar = True 

    if salir == True:
        break

    # Se actualiza el hud.    
    fondo_hud.fill(NEGRO)
    fondo_hud.blit(hud, (0, 0))
      
    dibujar_barcos(fondo_hud, imagenes_barcos) 
   
    # Establecemos el fondo de pantalla.
    ventana.fill(NEGRO)    

    # Dibujamos el tablero
    dibujar_tablero (ventana, tablero_jugador, fila, columna, DES_X, DES_Y, MORADO)
     	 
    # Obtencion de posicion y dibujado del cursor.
    x, y = pygame.mouse.get_pos()
    x -= RADIO_CURSOR
    y -= RADIO_CURSOR
    ventana.blit(imagen_cursor, (x, y))
	 
    # Dibujado del hud.
    ventana.blit(fondo_hud, (0, 500))

    # Se refrezca la pantalla.
    pygame.display.update()



#Aca llamamos a la funcion que posiciona los barcos enemigos en su tablero
posicionar_barcos_enemigos(tablero_cpu)

#Aca actualizamos la informacion de los diccionarios para que podamos seguir considerandolos activos.
reiniciar_info()


fin_partida = False

#Creamos un hud para la informacion del tablero del jugador
tablero1_hud = pygame.Surface((340, 340))
tablero1_hud.fill(NEGRO)

tab1 = pygame.Surface((0, 0))
tab1.fill(NEGRO)
tab1.set_colorkey(NEGRO)

turnos = TOTAL_TURNOS
jugadas = 0

#lista para almacenar los disparos del jugador
disparos = []

#lista para almacenar los disparos del oponente
disparos_random = []

ventana.fill(NEGRO)
pygame.display.update()

#Cantidad de barcos en juego
restantes_jugador = N_BARCOS
restantes_maquina = N_BARCOS


#IMPORTANTE, copiamos la informacion del tablero para poder visualizar tus propios barcos al comienzo de la partida

disparos_jugador = tablero_jugador

terminado = False
gandor = -1

#cantidad total de disparos del jugador 1
restantes = 200
while not terminado:
    
    #FPS
    reloj.tick(20) 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminado = True
                break

        if (jugadas % 2 == 0):
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor = (event.pos, RADIO_CURSOR)

		            #procesamos el disparo del jugador
                    disparo = procesar_disparo(cursor, tablero_cpu, disparos_cpu, DX, DY)          
		    
		            #si el disparo es valido
                    if (disparo[0] != -1):
                        disparos.append(disparo)
                        turnos-= 1
                        fila, columna = disparo[1]
        else:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    while (1):
		                #procesamos el disparo de tu oponente
                        random_disparo = disparo_enemigo(tablero_jugador, disparos_jugador)
	    	      
		                #si el disparo es valido  
                        if (random_disparo[0] != -1):
                            break

                    disparos_random.append(random_disparo)
                    turnos-= 1
                    fila, columna = disparo[1]

    #cargamos los elementos visuales
    
    if (terminado):
        break

    ventana.fill(NEGRO)
    
    fondo_hud.fill(NEGRO)
    fondo_hud.blit(hud, (0, 0))
    
    dibujar_barcos(fondo_hud, imagenes_barcos)
    actualizar_textos(fondo_hud, textos, restantes_jugador, restantes_maquina)

    #Dibujamos lo ocurrido con el disparo
    dibujar_tablero(ventana,disparos_cpu,fila,columna,DX,DY,AMARILLO)	
    dibujar_tablero(tablero1_hud,disparos_jugador,fila,columna,0,0,AMARILLO)
    
    #cargamos el cursor
    x, y = pygame.mouse.get_pos()
    x -= RADIO_CURSOR
    y -= RADIO_CURSOR
    ventana.blit(imagen_cursor, (x, y))
  
    # Dibujado del hud.
    ventana.blit(tablero1_hud, (30,30))
    ventana.blit(fondo_hud, (0, 500))

    # Se refrezca la pantalla.
    pygame.display.update()
    
    #si es que hemos realizado los 3 disparos
    if (turnos == 0):
        if (jugadas % 2 == 0):
            for i in disparos:		
                restantes-= 1
                bajas = actualizar_tablero(disparos_cpu, i, jugadas)
                sonido_disparos(ventana, tablero1_hud, imagen_cursor, disparos_cpu, i, sonidos, 0)

                if (bajas == 1):
                    sonidos[4].play()
                    sonidos[5].play()
	                #time.sleep(2)
                    restantes_maquina-= 1

                if (restantes_maquina == 0):
                    ganador = 0
                    terminado = True
                    break

	        #limpiamos la informacion de los disparos
            disparos  = []	
        else:
	   
            for i in disparos_random:		
                restantes-= 1
                bajas = actualizar_tablero(disparos_jugador, i, jugadas)
                sonido_disparos(ventana,tablero1_hud, imagen_cursor, disparos_jugador, i, sonidos, 1)

                if (bajas == 1):
                    sonidos[4].play()
                    sonidos[5].play()
                   #time.sleep(2)
                    restantes_jugador-= 1
	
                if (restantes_jugador == 0):
                    ganador = 1
                    terminado = True
                    break

	    #limpiamos la informacion de los disparos		   
            disparos_random = []   

	#cargamos la informacion de los disparos
        if (restantes == 2):
            turnos = 1
        else:
            turnos = 3
        jugadas+=1
	

ventana.fill(NEGRO)

if (ganador == 0):
    img_ganador = pygame.image.load("img/"+IMAGEN_GANADOR).convert()
    if img_ganador.get_size() != DIMENSIONES: 
        img_ganador = pygame.transform.scale(img_ganador, DIMENSIONES)
    ventana.blit(img_ganador, (0, 0))

else:
    img_perdedor = pygame.image.load("img/"+IMAGEN_PERDEDOR).convert()
    if img_perdedor.get_size() != DIMENSIONES: 
        img_perdedor = pygame.transform.scale(img_perdedor, DIMENSIONES)
    ventana.blit(img_perdedor, (0, 0))


pygame.display.flip()

esperando_click = True

while esperando_click:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            esperando_click = False
            break

# Se finalizan los modulos de pygame.
pygame.quit()
sys.exit()

