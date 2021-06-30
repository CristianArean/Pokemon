from pokemon import * 

def main():
    juego = crear_juego()
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():
        if juego[0] == 'menu principal':
            menu_principal()

        ev = gamelib.wait()

        if not ev:
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break

        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y 
            juego = navegacion(x, y, juego)

gamelib.init(main)
