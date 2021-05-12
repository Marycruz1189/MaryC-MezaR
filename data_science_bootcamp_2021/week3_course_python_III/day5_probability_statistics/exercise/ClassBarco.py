class Barco:
    """ Funciones para posicionar 
    las naves en el tablero"""


    def __init__(self, tipo_barco, tamaño):
        self.tipo_barco = tipo_barco
        self.tamaño = tamaño
        self.coor = []

    def localizacion_v(self, row, col):
        for i in range(self.tamaño):
            self.coor.append((row, col))
            row = row + 1

    def localizacion_h(self, row, col):
        for i in range(self.tamaño):
            self.coor.append((row, col))
            col = col + 1

    def verificacion(self):
        if self.coor == []:
            return True
        else:
            return False   

