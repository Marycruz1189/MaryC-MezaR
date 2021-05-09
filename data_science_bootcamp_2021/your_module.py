# This file represents your module.
# Write the code...
import pandas as pd
import numpy as np

def mean_visualization():
    """Draw the mean in a plot"""
    return None

def show_list_of_elements(lista):
    # TODO 
    pass


if __name__ == '__main__':
    x = mean_visualization()
    print(x)


from random import randint
import string
import secrets 


def generador(longitud, dificultad):
    """key generation program"""

    range_start = 10(longitud-1)
    range_end = (10**longitud)-1

    if dificultad == 1:

        return str(randint(range_start, range_end))
    elif dificultad == 2:
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(longitud))
    elif dificultad == 3:
        return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(longitud))
    elif dificultad == 4:
        return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(longitud2))
    else:
        return "numpy_y_pandas_son_lo_mejor"


def even_number(n):

    """It must satisfy the condition proving 
    further to be an odd number or to be an 
    even number"""
             
    if n % 2 ==0:
        return (True)
    else:
        return (False)

even_number(4)


def greet(*names):

   """ creat a names in a tuple with 
   arguments to say hello"""

   for name in names:

       print(“Hello”,name)

greet("Mary","Mati","Felix")

def create_board (player):
    #find out if you are printing the player 1 or player 2 board
    if player == "MaryCruz" or player == "Karina":

        print("The " + player + "'s board look like this: \n") 
    
  	#print the board
		    
    for i in range(10):
        print("~|" * 10)