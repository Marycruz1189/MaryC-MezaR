##Aquí vamos a colocar todas nuestras variables que vamos a ir utilizando durante el juego, mensajes biemvenida, instrucciones,dimensiones de los barcos,etc.
##4 barcos 2x1, 3b 3x1, 2b 4x1, 1b 5x1.

MENSAJES = {
    "introduccion": " **** Bienvenido al juego Battleship**** \
        \nLe presentamos su flota: \
        \n 1 Portador de 5x1 \
        \n 2 Acorazados de 4x1 \
        \n 3 Cruceros de 3x1 \
        \n 2 Submarinos de 2x1 \
        \n 2 Destructores de 2x2 ",

    "reglas" :" A continuación le indicamos las reglas del juego: \
        \n Coloque cada barco en cualquier posición horizontal o vertical pero no en diagonal \
        \n No coloque un barco de modo que cualquier parte de él se superponga a otro barco o al  borde de la cuadrícula \
        \n No se puede cambiar la posición del barco una vez empezado el juego. ",

    "blanco" : "Me ha dado en el blanco, buen tiro!",
    "fallo" :"Buen intento, pero ha fallado, sigue intentando!",
    "ganar" : "¡¡¡¡¡¡Has  GANADO!!!!! muy BIEN HECHO!! FELICITACIONES",
    "perder": "Has PERDIDO, sigue intentando",
    "adios": "***Hasta la próxima***"
}

LISTA_CARACTERES = ['A','B','C','D','E','F','G','H','I','J']

LISTA_NUMEROS = [1,2,3,4,5,6,7,8,9,10]

TIPOS_BARCO = [(4, 2), (3, 3), (2, 4), (1, 5)]

BARCO_CHAR= "#"

AGUA_CHAR = "~"

TOCADO_CHAR = "X"

FALLO_CHAR = "Ø"
