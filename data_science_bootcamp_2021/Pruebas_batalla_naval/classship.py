
import numpy as np


row_size = 10
col_size = 10
num_ships = 4
max_ship_size = 5
min_ship_size = 2
num_turns = 40

class Ship:
    def __init__(self, x, y, orientation, size):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.size = size

    def get_coordinates_ship(self, x, y, orientation, size):

        user_input = input(f"Please enter size of ship --->  ")
        user_input1 = input(f"Please enter coordinates and orientation 1 to 10 in format 1:10'v'/'h'1:10(row|'v' or 'h'|col")
      
        if 'h' in user_input1:
            self.size = int(user_input)
            self.orientation = 'h'
            self.x = int(user_input1[0])
            self.y = (range(int(user_input1[2]), int(user_input1[4])))
        elif 'v' in user_input:
            self.size = int(user_input)
            self.orientation = 'h'
            self.y = int(user_input1[0])
            self.x = (range(int(user_input1[2]), int(user_input1[4])))
        return {
            'ship_x': x,
            'ship_y': y,
            'ship_size':size,
            'ship_orientation':orientation,
            }

    def print_ship(self):
        print('row: %d, colum: %d, orientation: %d, size: %d' %(self.x,self.y,self.orientation,self.size))