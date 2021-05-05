class barcos:


    #constructor y atributo de los barcos

    def __init__(self, tamaño_fila, tamaño_columna, cantidad):
        
        self.tamaño_filas= filas
        self.tamaño_columnas= columnas
        self.cantidad=cantidad


    # método para ubicar los barcos

    def completar_matriz (self):

        import numpy as np
        self.matriz = np.array([["~"] * self.filas] * self.columnas, dtype=object)
    


    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False
