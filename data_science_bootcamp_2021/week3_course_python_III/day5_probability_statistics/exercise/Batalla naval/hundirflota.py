from comandos import Comandos
#from battleshipscomputer import BattleshipsCOMP


def juega_Hundir_Flota():
    """Función para iniciar el 
    juego Hundir la Flota"""
    
    print("Que empiece el juego")
    
    print("\n 1) Player vs Player")
    

    flag = True

    while flag:
        try:
            mode = int(input("\n\nPick a number to select a game mode ----> "))
            if mode == 1:
                flag = False
                BattleshipsPVP()
            elif mode == 2:
                flag = False
                BattleshipsCOMP()
            else:
                continue
        except ValueError:
            print("You can only pick either option 1 or 2")


juega_Hundir_Flota()