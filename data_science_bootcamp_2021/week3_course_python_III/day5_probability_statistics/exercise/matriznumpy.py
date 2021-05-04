# http://progra.usm.cl/apunte/tareas/2015-1/tarea-2.html
# http://progra.usm.cl/apunte/tareas/2015-1/pygame.html
# https://gist.github.com/nicolasfig/3859954#file-clasematriz-py
# https://gist.github.com/nicolasfig/3859954#file-clasematriz-py

class matriz:


    #constructor y atributo de la matriz

    def __init__(self, filas, columnas):
        self.matriz=[]
        self.filas= filas
        self.columnas= columnas

    # método para completar la matriz

    def completar_matriz (self):

        import numpy as np
        self.matriz = np.array([["~"] * self.filas] * self.columnas, dtype=object)
    
    # método para mostrar la matriz
    def mostrar_matriz (self):
        for i in range(len(self.matriz[0])):
            self.matriz[i,i] = self.matriz[i,i]
        print(matriz)

    #Cada jugador deberá colocar en su tablero:
    # 4 barcos tamaño 2x1.
    # 3 barcos tamaño 3x1.
    # 2 barcos tamaño 4x1.
    # 1 barco tamaño 5x1.

