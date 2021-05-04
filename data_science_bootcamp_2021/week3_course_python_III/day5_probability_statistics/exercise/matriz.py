#El tablero de este juego será una matriz de 10x10 dimensiones, 
# matriz sobre la que plamaremos el estado de cada turno. 
# Cada matriz de información continente del estado en cada momento, 
# se mostrará por pantalla.

#CREAR MATRIZ


# este es el juego buscaminas desarrollado en python.
# crear matriz, esta funcion no invoca ninguna otra funcion del programa
def matriz(filas,columnas,caracter=False):
    tablero = []
    for i in xrange(0,filas):
        v = [caracter]*columnas
        tablero.append(v)
    return tablero


# se crea el tablero de acuerdo a las especificaciones del jugador esta funcion invoca
# a la funcion matriz(es para crear una matriz dado el numero de filas y columnas)
# y a la funcion minas(es para colocar las pistas. las pistas son los numeros que aparecen en el juego)
def tablero1():
    filas = input("ingresa el numero de filas que deseas: ")
    columnas = input("ingresa el numero de columnas que desea: ")
        
    tablero = matriz(filas,columnas)
       
    return tablero,filas,columnas

tablero1(10)
# poner las pistas que son los numeros que aparecen en el tablero
# esta funcion solo hace uso de la funcion matriz
# def numeros(tablero,filas,columnas):
#     nueva = matriz(filas,columnas,".")
#     for i in xrange(0,filas):
#         for j in xrange(0,columnas):
#             # calcular el numero de vecinos de la celula que se esta vicitando
#             n = 0
#             if i > 0 and j > 0 and tablero[i - 1][j - 1]:
#                 n += 1
#             if j > 0 and tablero[i][j - 1]:
#                 n += 1
#             if i < filas - 1 and j > 0 and tablero[i + 1][j - 1]:
#                 n += 1
#             if i > 0 and tablero[i - 1][j]:
#                 n += 1
#             if i < filas - 1 and tablero[i + 1][j]:
#                 n += 1
#             if i > 0 and j < columnas - 1 and tablero[i - 1][j + 1]:
#                 n += 1
#             if j < columnas - 1 and tablero[i][j + 1]:
#                 n += 1
#             if i < filas - 1 and j < columnas - 1 and tablero[i + 1][j + 1]:
#                 n += 1
#             if not tablero[i][j]:
#                 nueva[i][j] = n
#             else :
#                 nueva[i][j] = True
#     tablero = nueva
#     return tablero

# # mostrar el tablero de juego, esta funcion no hace uso de ninguna otra funcion
# def mostrar(tablero,filas,columnas,caracter):
#     for i in xrange(0,filas):
#         for j in xrange(0,columnas):
#             if j != columnas - 1 :
#                 if type(tablero[i][j]) == (int or str):
#                     print tablero[i][j],
#                 elif (type(tablero[i][j]) == bool) and (tablero[i][j]):
#                     print "*",
#                 else :
   
#                     print caracter,
#             else :
#                 if type(tablero[i][j]) == (int or str):
#                     print tablero[i][j]
#                 elif (type(tablero[i][j]) == bool) and (tablero[i][j]):
#                     print "*"
#                 else:
           
#                     print caracter

import numpy as np
        matriz = np.array([["~"] * 10] * 10, dtype=object)

        for i in range(len(matriz[0])):
            matriz[i,i] = matriz[i,i]
        print(matriz)