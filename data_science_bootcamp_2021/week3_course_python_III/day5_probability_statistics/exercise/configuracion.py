import random as rnd

n  = int(input('¿Cuántas municiones?: '))
bx = int(input('Barco ¿Coordenada bx?: '))
by = int(input('Barco ¿Coordenada by?: '))

hundido = 0
disparo = 0

# Juego
while (disparo<n and hundido==0):

    print('\nIntento '+str(disparo+1))
    print('Barco enemigo en ('+str(bx)+','+str(by)+')')
    cx = int(input('Disparo ¿Coordenada cx?: '))
    cy = int(input('Disparo ¿Coordenada cy?: '))

    d = int(rnd.random()*4)+1
    p = int(rnd.random()*3)+1

    if d==1:
        by = by + p
    if d==2:
        by = by - p
    if d==3:
        bx = bx + p
    if d==4:
        bx = bx - p
    if (bx==cx and by==cy):
       hundido = 1

    disparo = disparo+1

    print('Movimiento direccion:',d,
          ' con:',p,'casillas')
    print('Disparados: ',disparo)
    print('   Hundido: ',hundido)

# SALIDA
print('Barco Hundido:', hundido)
print('Disparos realizados:',disparo