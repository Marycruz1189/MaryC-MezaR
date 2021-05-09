class Board():
    """ The ship battle board """
    def __init__(self, col, row):
        """Initialize clean GameBoard depending on size, etc """
        self.occupied = "#" # representation for ships
        self.destroyed = 'x' # representation for destroyed area
        self.clear = '~' # representation for clear water
        self.col = columns
        self.row = row

    def create_board (self):
        board = []
        for i in range(10):
            board.append["~|" * 10]
            


    def printBoard(self):
        """ Print the current gameboard state """
        for row in board:
        print ("Let's play Battleship!\n\n")
        print (" ".join(row))
        
    
        

    def updateBoard(self, ship):
        """ Updates the gameboard according to updated ship """

    



