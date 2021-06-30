from pokemon import * 

def main():
    juego = crear_juego()

    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():

        if juego[0] == 'menu principal':
            #print ('funca')
            menu_principal()

        ev = gamelib.wait()

        if not ev:
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break

        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y 
            #print (f'x {x}, y {y}') #debug
            #juego = juego_actualizar(juego, x, y)
            #print (juego)
            juego = navegacion(x, y, juego) #le cambié el nombre a la funcion
            #print ('Juego', juego)

gamelib.init(main)
