import pokemon


def main():
    juego = pokemon.crear_juego()
    pokemon.gamelib.resize(pokemon.ANCHO_VENTANA, pokemon.ALTO_VENTANA)

    while pokemon.gamelib.is_alive():
        if juego[0] == 'menu principal':
            pokemon.menu_principal()

        ev = pokemon.gamelib.wait()

        if not ev:
            break

        if ev.type == pokemon.gamelib.EventType.KeyPress and ev.key == 'Escape':
            break

        if ev.type == pokemon.gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y 
            juego = pokemon.navegacion(x, y, juego)

pokemon.gamelib.init(main)
