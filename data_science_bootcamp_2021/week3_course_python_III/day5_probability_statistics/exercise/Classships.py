class Ships:
    """ Ship object container"""

    def __init__(self, position_row, position_colum, orientation, size  ):
        """ Necessary variables for the ship go here """
        self.position_row = position_row
        self.position_colu = position_colu
        self.orientation = orientation
        self.size = size

#Settings Variables
    row_size = 9 #number of rows
    col_size = 9 #number of columns
    num_ships = 10
    max_ship_size = 5
    min_ship_size = 2
    num_turns = 40

      
    def orientation(self):
        """get ship orientation 
        from user"""
        if orientation =='v' or orientation_input == 'h':
            self.orientation = orientation
                
        else:
            raise ValueError("Invalid sintax. Please enter v or h")

    def position_row(self):
        if orientation == 'h':
            if position_row in range(row_size):
                self.coordinates = []
                for i in range(size):
                    if position_colum + i in range(col_size):
                        self.coordinates.append({'row': position_row, 'col': position_row + i})
                    else:
                        raise IndexError("Column is out of range")
            else:
                raise IndexError("Row is out of range.")
    def position_colum(self):            
        if orientation == 'v':
            if position_colum in range(col_size):
                self.coordinates = []
                for i in range(size):
                    if position_colum + i in range(row_size):
                        self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
                    else:
                        raise IndexError("Row is out of range.")
            else:
                raise IndexError("Column is out of range.")


  












