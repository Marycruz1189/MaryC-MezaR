class Ship:
    def __init__(self, col, row, orientation, size):
        self.col = col
        self.row = row
        self.orientation = orientation
        self.size = size

    # Say the number of ships 
    
    ships = []

    def random_row(board):
        return randint(0, len(board[0]) - 1)


    def random_col(board):
        return randint(0, len(board[0]) - 1)

   
    import random
    ships = []
    NUMBER_OF_SHIPS = 9
    for i in range(NUMBER_OF_SHIPS):
        ships.append(ships(col(board), row(board)))






    # random_row, random_col, and board are just like you had them
    



    

ship_row = random_row(board)
ship_col = random_col(board)
import random
ships = [['row',random_row,'col',random_col]]
for i in range(9):
    ships.append(['row',random_row,'col',random_col])
random.choice(ships)() #i am lost