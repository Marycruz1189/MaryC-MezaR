class Tablero:

        """Crea un tablero 2D que muestre la
    ubicación de los barcos"""


    def __init__(self, ancho=10, alto=10 ):
        self.ancho = ancho
        self.alto = alto 
        self.tablero = np.full((ancho,alto), "~")

    def imprime_tablero(self):

        self.tablero_jugador = self.tablero
        self.tablero_oponente = self.tablero




    