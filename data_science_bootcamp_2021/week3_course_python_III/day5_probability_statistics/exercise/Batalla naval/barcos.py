class Barcos:

    def __init__(self, clases_barcos, tamaño):
        self.clases_barcos = clases_barcos
        self.tamaño = tamaño
        self.coord = []

    def rango_vertical(self, filas, colum):
        for i in range(self.tamaño):
            self.coord.append((filas, colum))
            filas = colum + 1

    def rango_horizontal(self, filas, colum):
        for i in range(self.tamaño):
            self.coord.append((row, col))
            col = col + 1

    def verificar_stado(self):
        if self.coord == []:
            return True
        else:
            return False