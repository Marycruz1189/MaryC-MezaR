class Seguimiento:

    """Crea un tablero 2D que muestre el estado del oponente"""

    def __init__(self, ancho=10, alto=10 ):
        self.seguimiento = [["~|" * alto for i in range(ancho)]

    def __getitem__(self, point):
        row, col = point
        return self.seguimiento[row][col]

    def __setitem__(self, point, value):
        row, col = point
        self.seguimiento[row][col] = value

    def print_seguimiento(self):
        for row in self.seguimiento:
            print(" ".join(row))