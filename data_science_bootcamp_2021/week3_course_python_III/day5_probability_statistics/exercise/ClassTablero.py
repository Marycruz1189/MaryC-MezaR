class Tablero():
    
    """Crea un tablero 2D que muestre la
    ubicación de los barcos"""
    
    
    def __init__(self, ancho=10, alto=10 ):
        self.tablero = [["~|" * alto for i in range(ancho)]
        

    def __getitem__(self, point):
        row, col = point
        return self.tablero[row][col]

    def __setitem__(self, point, value):
        row, col = point
        self.tablero[row][col] = value

    def print_tablero(self):
        for row in self.tablero:
            print(" ".join(row)
        
    




