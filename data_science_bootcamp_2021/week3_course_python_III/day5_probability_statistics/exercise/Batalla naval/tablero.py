class Tablero:

    """Crea un tablero 2D que muestre la
    ubicación de los barcos"""

    def __init__(self, ancho=10, alto=10 ):
        self.tablero = [["~|" * alto for i in range(ancho)]]

    
    def __getitem__(self, puntos):
        fila, colum = puntos
        return self.tablero[fila][colum]

    def __setitem__(self, puntos, valores):
        fila, colum = puntos
        self.tablero[fila][colum] = valores

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(" ".join(fila))
                

    # Verifica si la ubicacion no esta ocupada

    def validar_colum(self, fila, colum, tamaño):
        
        validar_coor = []

        for i in range(tamaño):
            
            if self.tablero[fila][colum] == "~":

                valid_coords.append((fila, colum))
                colum = colum + 1
            else:
                colum = colum + 1
            #else:
                #return False

        if tamaño == len(validar_coor):
            return True
        else:
            return False

    def validar_fila(self, fila, colum, tamaño):

        validar_coor = []

        for i in range(tamaño):

            
            if self.tablero[fila][colum] == "~":
                validar_coor.append((fila, colum))
                fila = colum + 1
            #else:
                #fila = colum + 1
            else:
                return False

        if tamaño == len(validar_coor):
            return True
        else:
            return False

    # Función para ubicar el barco en un espacio en blanco

    def ubicar_barco(self, fila, colum):
        
            self.tablero[fila][colum] = "#"
            colum = colum + 1

    # def ubicar_barco_fila(self, fila, colum, tamaño):
    #     for i in range(tamaño):
    #         self.tablero[fila][colum] = "#"
    #         fila = fila + 1

barcos = Tablero(ancho=10, alto=10 )
imprimir_tablero()
