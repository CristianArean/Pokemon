from pokemon import * #es buena idea usar *? nos ahorra los prefijos pero tiene mucho costo de memoria o procesamiento? ####################

def main():
    juego = crear_juego()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        #gamelib.draw_begin()
        if juego == 1:
            menu_principal()
        #gamelib.draw_end() # CREO QUE EL DIBUJO VA EN CADA FUNCION. LO COMENTO PARA NO BORRARLO ##########################

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            print (f'x {x}, y {y}') #debug
            #juego = juego_actualizar(juego, x, y)
            juego = pokemones_o_equipos(x, y)

gamelib.init(main)

