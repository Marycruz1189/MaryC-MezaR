board = []
for x in range(10):
    board.append(["~"] * 10)

def print_board(board):
    for row in board:
        print (" ".join(row))

def ubicar_barco(fila, colum):
    print_board[fila][colum] = "#"
    colum = colum + 1

def seguimiento(board):
    for row in board:
        print(" ".join(row)) 



#starting the game and printing the board
print("Let's play Battleship!") 
print_board(board)

#defining where the ship is

def get_coor(board):
    ships = {"ship 2x1":4,
		     "ship 3x1":3,
 		     "ship 4x1 ":2,
		     "ship 5x1":1}
    for barco, tamaño in ships.items():

            flag = True
            while flag:
                print_board(board)
                try:
                    print("Estado inicial de la flota, inserte el %s" % (ship))
    

                    user_input = input("Inserte las coordenadas del 1 al 10 en formato nhn:n(filas/horizontal/columnas) o nvn:n (columna/vertical/filas)")
                    if user_input in "v":
                        for elem in user_input:
                            if 'v' in elem:
                                                    
                                fila = []
                                colum = []
                                
                                colum.append(int(elem[0]))
                                fila.append(int(elem[2:4]))
                                seguimientov = ubicar_barco(fila, colum)
                                flag = False
                            else:
                                if 'h' in elem:
                                    fila = []
                                    colum = []
                                    fila.append(int(elem[0]))
                                    colum.append(int(elem[2:4]))
                                    seguimientoh = ubicar_barco(fila, colum)
                                    flag = False