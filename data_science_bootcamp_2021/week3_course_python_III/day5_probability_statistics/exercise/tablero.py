class tablero():


    def __init__ (self, fila,columna,caracter):
        self.fila = fila
        self.columna = columna
        self.caracter = caracter

    def crear_tablero (self, fila, columna, caracter):

        import numpy as np
        matrix = np.full((fila,columna), str(caracter))
        return matrix
    
   


