import pokemon
from pokemon import gamelib

ANCHO_VENTANA = 900
ALTO_VENTANA = 600

def main():
    juego = pokemon.crear_juego()
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():
        if juego[0] == 'menu principal':
            pokemon.menu_principal()

        ev = gamelib.wait()

        if not ev:
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break

        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y 
            juego = pokemon.navegacion(x, y, juego)

gamelib.init(main)
