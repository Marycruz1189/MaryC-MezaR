from tablero import Tablero
from seguimiento import Seguimiento
from barcos import Barcos
import os

class Jugador:

    ships = {"ship 2x1":4,
		     "ship 3x1":3,
 		     "ship 4x1 ":2,
		     "ship 5x1":1}

    def __init__(self, turnos):
        """ Función que ubica los barcos del jugador en el tablero"""

        self.tablero = Tablero()
        self.seguimiento = Seguimiento(())
        self.turnos = turnos
        self.flota = []

   

    def ubicar_barcos(self):
       
        for barco, canti in self.ships.items():

            flag = True
            while flag:
                self.imprimir_tablero()
                try:
                    print("Estado inicial de la flota, inserte el %s" % (ship))
                    ubicacion_inicial = (input("Inserte las coordenadas del 1 al 10 en formato nhn:n(filas/horizontal/columnas) o nvn:n (columna/vertical/filas)"))
                    if ubicacion_inicial in "v":
                        for elem in ubicacion_inicial:
                            if 'v' in elem:
                                fila = []
                                colum = []
                                
                                colum.append(int(elem[0]))
                                fila.append(int(elem[2:4]))
                                self.tablero.ubicar_barco(fila, colum)
                            else:
                                if 'h' in elem:
                                    fila = []
                                    colum = []
                                    fila.append(int(elem[0]))
                                    colum.append(int(elem[2:4]))


                    #filas = int(input("Pick a row -----> "))
                    #colum = int(input("Pick a column -----> "))
                    #orientation = str(input("Vertical or Horizontal? (choose v or h) -----> "))

                    #if orientation in ["v", "V"]:
                        #if self.ocean.can_use_row(row, col, size):
                            #self.ocean.set_ship_row(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_vertical(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Overlapping ships, try again")

                    elif orientation in ["h", "H"]:
                        if self.ocean.can_use_col(row, col, size):
                            self.ocean.set_ship_col(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_horizontal(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Overlapping ships, try agin")

                    else:
                        continue

                    self.view_console()
                    input()
                    os.system('clear')

                except ValueError:
                    print("Don't you remember your training?\nType a number..\n")

    # Function displays player ocean/radar in readable format

    def view_console(self):
        self.radar.view_radar()
        print("|                 |")
        self.ocean.view_ocean()

    # Function checks status of ship objects within player fleet

    def register_hit(self, row, col):
        for boat in self.fleet:
            if (row, col) in boat.coords:
                boat.coords.remove((row, col))
                if boat.check_status():
                    self.fleet.remove(boat)
                    print("%s's %s has been sunk!" % (self.name, boat.ship_type))

    # Player interface for initiating in-game strikes,
    # updates the state of the boards of both players

    def strike(self, target):
        self.view_console()
        try:
            print("\n%s Pick your target..." % (self.name))
            row = int(input("Pick a row -----> "))
            col = int(input("Pick a column -----> "))

            if self.ocean.valid_row(row) and self.ocean.valid_col(col):
                if target.ocean.ocean[row][col] == "S":
                    print("DIRECT HIT!!!")
                    target.ocean.ocean[row][col] = "X"
                    target.register_hit(row, col)
                    self.radar.radar[row][col] = "X"

                else:
                    if self.radar.radar[row][col] == "O":
                        print("Area already hit....Check your radar!")
                        self.strike(target)
                    else:
                        print("Negative...")
                        self.radar.radar[row][col] = "O"

            else:
                print("Coordinates out of range...")
                self.strike(target)

        except ValueError:
            print("You need to provide a number....\n")
            self.strike(target)
        input()
        os.system('clear')