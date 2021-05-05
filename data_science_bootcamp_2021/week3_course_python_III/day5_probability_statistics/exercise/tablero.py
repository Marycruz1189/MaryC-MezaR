
def matriz_barco (fila,columna,caracter):
    
    matriz = []
    for i in range(fila):
        a = [caracter]*columna
        matriz.append(a)
    return matriz
matriz_barco(10, 10, "~")


    #Cada jugador deberá colocar en su tablero:
    # 4 barcos tamaño 2x1.
    # 3 barcos tamaño 3x1.
    # 2 barcos tamaño 4x1.
    # 1 barco tamaño 5x1.

