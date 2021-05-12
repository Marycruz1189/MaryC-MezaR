import os
import sys

from ClassTablero import Tablero
from ClassSeguimiento import Seguimiento
from ClassBarco import Barco

class Jugadores:

        """ Función para establecer la flota en el 
        tablero del jugador, de acuerdo a las posiciones dadas"""
 
#types of ships
	ships = {"ship 2x1":4,
		     "ship 3x1":3,
 		     "ship 4x1 ":2,
		     "ship 5x1":1}
  
    def __init__(self, player):
        self.tablero = Tablero()
        self.seguimiento = Seguimiento()
        self.player = player
        self.flota = []
        
     
    def tablero_inicial(self):
        input("Pick a coordinate between 0 and 9 for the columns and rows on your board")
        input("Boats are placed form right to left.")
        for ship, size in self.ships.items():

            flag = True
            while flag:
                self.print_tablero()
                try:
                    row = int(input("Ingrese un valor para fila del 0 al 9 "))
                    col = int(input("Ingrese un valor para columna del 0 al 9 "))
                    orientacion = str(input("Escoja 'v' para vertical y 'h' para horizontal "))

                    if orientacion in ["v"]:

                        barcos = Barco(ship, size)
                        barcos.localizacion_v(row, col)
                        self.flota.append(barcos)
                        flag = False
                    

                    elif orientation in ["h"]:
                       
                        barcos = Barco(ship, size)
                        barcos.localizacion_h(row, col)
                        self.flota.append(barcos)
                        flag = False
                        

                    else:
                        continue

                    self.print_tablero()
                    input()
                    os.system('clear')

                
    def print_tablero(self):

        """Esta función imprime el tablero del rival"""

        self.seguimiento.print_seguimiento()
        print("|                 |")
        self.tablero.print_tablero()


    def registro_disparos(self, row, col):
        """La función muestra los barcos atacados 
        de la flota rival"""
        for barcox in self.flota:
            if (row, col) in barcox.coords:
                barcox.coords.remove((row, col))
                self.flota.remove(barcox)
                    print("%s %s ha sido derribado!" % (self.player, barcox.ships))

    # Player interface for initiating in-game strikes,
    # updates the state of the boards of both players

    def ataque(self, objetivo):
        self.print_tablero()
        try:
            
            row = int(input("Inserte coordenadas a atacar fila x"))
            col = int(input("Inserte coordenadas a atacar columna x"))

            if objetivo.tablero.tablero[row][col] == "#":
                print("Barco derribado")
                objetivo.tablero.tablero[row][col] = "x"
                objetivo.registro_disparos(row, col)
                    self.seguimiento.seguimiento[row][col] = "x"

                else:
                    if self.seguimiento.seguimiento[row][col] == "~":
                        print("Disparo al agua")
                                        
                        self.seguimiento.seguimiento[row][col] = "o"
                
       
        os.system('clear')