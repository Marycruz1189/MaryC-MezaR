class Seguimiento:

    """Mostrar el estado del oponente"""

    def __init__(self, ancho=10, alto=10 ):
        self.tablero = [["~|" * alto for i in range(ancho)]

    def __getitem__(self, punto):
        fila, colum = punto
        return self.seguimiento[fila][colum]

    def __setitem__(self, punto, valor):
        fila, colum = punto
        self.radar[fila][colum] = valor

    def imprimir_seguimiento(self):
        for fila in self.seguimiento:
            print(" ".join(fila))