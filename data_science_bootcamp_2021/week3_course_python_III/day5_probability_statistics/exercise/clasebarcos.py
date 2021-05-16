from clasetablero import Tablero
import sys
import copy, random
class Barcos:


    def __init__(self,) :
        self.tablero_jugador
        self.tablero_oponente





    posicionar_barcos(tablero_jugador, tablero_oponente) #call function to choose ships

def posicionar_barcos(tablero_jugador, tablero_oponente):
    """Funcion para posicionar los barcos en el tablero de cada jugador"""
    barcos = {'5x1': 5, '4x1': 4, '3x1': 3, '2x1': 2} #tamano de los barcos
    barcos_jugador = [['5x1', 1], ['4x1', 2],['3x1', 3], ['2x1', 4]] #numero de barcos a ubicar
    barcos_oponente = [['5x1', 1], ['4x1', 2],['3x1', 3], ['2x1', 4]]

    for x in barcos_jugador: #barcos a ubicar
        contador = 0

        while x[1] > 0:
            contador += 1
            clase_barco = x[0]
            tamano_barco = barcos[x[0]]
            posicion = input("Por favor ingrese las coordenadas y orientacion del 1 al 10 en formato 1:10'v'/'h'1:10(fila|'v' o 'h'|col de {0}: ".format(x[0]))
            validacion = ubicar_barcos(tablero_jugador, tamano_barco, posicion, clase_barco)
            if validacion is True:
                x[1] -= 1
            else:
                print("No es posible ubicar el barco en esta posicion")

    for z in barcos_oponente:
        contador = 0

        while z[1] > 0:
            contador += 1
            clase_barco = z[0]
            tamano_barco = barcos[z[0]]
            posicion = input("Por favor ingrese las coordenadas y orientacion del 1 al 10 en formato 1:10'v'/'h'1:10(fila|'v' o 'h'|col de {0}:".format(z[0]))
            validacion = ubicar_barcos(tablero_oponente, tamano_barco, posicion, clase_barco)
            if validacion is True:
                z[1] -= 1
            else:
                print("No es posible ubicar el barco en esta posicion")
    iniciar_juego(tablero_jugador, tablero_oponente)

def validar_posicion(tablero_jugador, tamano_barco, columna, fila, pos2,direccion):
    validar_barcos = ["5x1", "4x1", "3x1", "2x1"]
    if direccion == 'v':
        espacio = pos2 + int(tamano_barco)
        if espacio <= 11:
            for i in range(0, tamano_barco):
                rawr = tablero_jugador[int(pos2 + i)][int(columna) - 1]
                if rawr not in validar_barcos:
                    pass
                else:
                    return False
            return True
        else:
            return False
    elif direccion == 'h':
        if pos2 + int(tamano_barco) <= 11:
            for i in range(0, tamano_barco):
                if tablero_jugador[int(fila)][int(pos2) + i - 1] not in validar_barcos:
                    pass
                else:
                    return False
            return True
        else:
            return False


def ubicar_barcos(tablero_jugador, tamano_barco, posicion, tipo_barco):

    if 'h' in posicion:
        orientacion = 'h'
        fila = int(posicion[0])
        columna = (range(int(posicion[2]), int(posicion[4])))
        pos2 = int(posicion[2])
    elif 'v' in posicion:
        orientacion ='v'
        columna = int(posicion[0])
        fila = (range(int(posicion[2]), int(posicion[4])))
        pos2 = int(posicion[2])


    if orientacion == 'v':
            resultado = validar_posicion(tablero_jugador, tamano_barco, columna, fila, pos2,'v')
            if resultado is True:
                for i in range(0, tamano_barco):
                    tablero_jugador[int(pos2 + i)][int(columna) - 1] = str(tipo_barco)

            print(tablero_jugador)


    elif orientacion == 'h':

            resultado = validar_posicion(tablero_jugador, tamano_barco, columna, fila,pos2, 'h')
            if resultado is True:
                for i in range(0, tamano_barco):
                    tablero_jugador[int(fila)][int(pos2) + i - 1] = str(tipo_barco)
            print(tablero_jugador)


    return resultado

def definir_turno(nombre1, nombre2):
    """Funcion para definir que jugador empieza el juego"""
    turno1 = random.randint(1, 6)
    print(f'El numero de {nombre1} es {turno1}')
    turno2 = random.randint(1, 6)
    print(f'El numero de {nombre2} es {turno2}')
    if turno1 > turno2:
        jugador = nombre1
        oponente = nombre2
        print(f'{nombre1} start the game and is the jugador')
        return jugador, oponente
    else:
        jugador = nombre2
        oponente = nombre1
        print(f'{nombre2} start the game and is the jugador')
        return jugador, oponente


def iniciar_juego(tablero_jugador, tablero_oponente, definir_turno):
    print("Empieza el Jugador")
    definir_turno("Karina", "Marycruz")
    turno_jugador = True
    turno_oponente = False
    validar_barcos = ["5x1", "4x1", "3x1", "2x1"]
    victoria = False

    while True:
        if turno_jugador:
            while not victoria:
                posicion = input("Jugador ataque: ")
                fila = posicion[0]
                if len(posicion) > 2:
                    columna = (posicion[1]+posicion[2])
                else:
                    columna = posicion[1]
                fila = int(fila)
                columna = int(columna) - 1
                objetivo = tablero_oponente[fila][columna]
                barco_tocado = objetivo
                objetivo = str(barco_tocado)
                if objetivo in validar_barcos:
                    print("Tocado")
                else:
                    print("Agua")
                tablero_oponente[fila][columna] = "X"

                hundido = True
                for y in tablero_oponente:
                    if hundido:
                        for x in y:
                            if x == barco_tocado:
                                hundido = False
                                break
                    else:
                        break

                if hundido:
                    if objetivo in validar_barcos:
                        print("{0} HUNDIDO.".format(objetivo))

                victoria = True
                for y in tablero_oponente:
                    if victoria:
                        for j in y:
                            if j not in validar_barcos:
                                victoria = True
                            else:
                                victoria = False
                                break
                if victoria:
                    print("JUGADOR GANA")
                    sys.exit()
                turno_jugador = False
                turno_oponente = True
                break

        elif turno_oponente:
            while not victoria:
                posicion = input("Oponente, ataque: ")
                fila = posicion[0]
                if len(posicion) > 2:
                    columna = (posicion[1]+posicion[2])
                else:
                    columna = posicion[1]
                fila = int(fila)
                columna = int(columna) - 1
                objetivo = tablero_jugador[fila][columna]
                barco_tocado = objetivo
                objetivo = str(barco_tocado)
                if objetivo in validar_barcos:
                    print("Tocado")
                else:
                    print("Agua")
                tablero_jugador[fila][columna] = "X"

                hundido = True
                for y in tablero_jugador:
                    if hundido:
                        for x in y:
                            if x == barco_tocado:
                                hundido = False
                                break
                    else:
                        break

                if hundido:
                    if objetivo in validar_barcos:
                        print("{0} HUNDIDO.".format(objetivo))

                victoria = True
                for y in tablero_jugador:
                    if victoria:
                        for j in y:
                            if j not in validar_barcos:
                                victoria = True
                            else:
                                victoria = False
                                break
                if victoria:
                    print("Oponente Gana")
                    sys.exit()
                turno_jugador = True
                turno_oponente = False
                break

imprime_tablero()