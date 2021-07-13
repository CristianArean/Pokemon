import gamelib
import lectores

equipos = 'equipos.csv'
movimientos = 'movimientos.csv'
pokemons = 'pokemons.csv'

ANCHO_VENTANA = 900
ALTO_VENTANA = 600

MENSAJE_NOMBRE = "Elija un nombre para su equipo. Cancele la formación con [CANCELAR]"
MENSAJE_NOMBRE_ERROR = 'Por favor dale un nombre a tu equipo. Si quieres cancelar la formación pulsa [CANCELAR]'
MENSAJE_POKEMON = "Eliga un pokemon ingresando su número y presionando [OK]. Cancele la formación con [CANCELAR]"
MENSAJE_POKEMON_ERROR = "ERROR. Ingrese el número de un pokemon disponible."
MENSAJE_ELEGISTE_POKEMON = 'Elegiste a {} para el equipo {}. Puedes seguir eligiendo hasta llegar al límite de {} pokemones o terminar la elección con [CANCELAR]'
MENSAJE_MOVIMIENTOS = 'Ahora podrá elegir los movimientos para {}.'
MENSAJE_MOVIMIENTOS_OPCIONES = '¿Qué poder desea elegir para {}? Están disponibles {}.'
MENSAJE_MOVIMIENTOS_REPETIDO = 'Ese movimiento ya fue elegido. Eliga otro o termine la elección.'
MENSAJE_MOVIMIENTOS_ERROR = "No ingreso un movimiento disponible. Eliga uno de los siguientes {}. Termine la selección con [CANCELAR]"

VACIO = 0
NRO_COLUMNAS = 7
NRO_FILAS = 4
MAX_NRO_POKEMONES_EQUIPO = 6
MAX_NRO_MOVIMIENTOS_POKEMON = 4

TITLE_Y = 70
MARGEN_ENTRE_BOTONES = 70
ALTO_BOTONES = 50
ESPACIO_ENTRE_BOTONES = 30
BOTON_Y1 = ALTO_VENTANA // 2 - ALTO_BOTONES
BOTON_Y2 = ALTO_VENTANA // 2
XY_CUADRITO = 100
MARGEN_CUADRITOS_SUPERIOR = 90
MARGEN_CUADRITOS_IZQUIERDO = 70
ESPACIO_ENTRE_CUADROS = 10
BOTON_RETROCESO = 30
FRANJA_AZUL_Y = 88

BOTON_ROJO = BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO * 2, BOTON_RETROCESO * 2
BOTON_NARANJA = ANCHO_VENTANA - BOTON_RETROCESO * 2, BOTON_RETROCESO, ANCHO_VENTANA - BOTON_RETROCESO, BOTON_RETROCESO * 2


def crear_juego():
    """
    Crea el juego, retornando 'menu principal' y creando 'equipos.csv' si aún no existe. 
    Si 'equipos.csv' ya existe, será ultilizado para guardar los equipos ya guardados.
    """
    try:
        with open(equipos, 'x') as archivo:
            pass
    except:
        return 'menu principal', 0, 0

    with open(equipos, 'w') as archivo:
        for _ in range(1):
            archivo.writelines(
                'equipo_numero;equipo_nombre;integrante1;movimientos1;integrante2;movimientos2;integrante3;movimientos3;integrante4;movimientos4;integrante5;movimientos5;integrante6;movimientos6')
    return 'menu principal', 0, 0


def buscador_particular(pag_pok, pag_equ):
    """
    Le pide un número de pokemon al usuario y lo manda
    a la ventana correspondiente a ese pokemon.
    """
    numero = gamelib.input('Ingrese el número del pokemon que desea ver.')
    
    if numero == None or numero == '':
        return 'menu Pokemones', pag_pok, pag_equ 
    else:
        while not numero.isdigit(): 
            numero = gamelib.input('No ingreso un digite un caracter valido. Ingrese el número del pokemon que desea ver')
        return un_pokemon(int(numero), pag_pok, pag_equ)


def menu_principal():
    """
    Dibuja el menú principal.
    """
    CREDITOS_X, CREDITOS_Y = ANCHO_VENTANA // 2, ALTO_VENTANA - 2 * TITLE_Y // 3  # POSICIÓN CREDITOS
    BOTON_IZQ_X1, BOTON_IZQ_Y1, BOTON_IZQ_X2, BOTON_IZQ_Y2 = MARGEN_ENTRE_BOTONES, BOTON_Y1, ANCHO_VENTANA // 2 - ESPACIO_ENTRE_BOTONES, BOTON_Y2
    BOTON_DER_X1, BOTON_DER_Y1, BOTON_DER_X2, BOTON_DER_Y2 = ANCHO_VENTANA // 2 + ESPACIO_ENTRE_BOTONES, BOTON_Y1, ANCHO_VENTANA - MARGEN_ENTRE_BOTONES, BOTON_Y2
    TEXTO_IZQ_X, TEXTO_IZQ_Y = MARGEN_ENTRE_BOTONES * 2, ALTO_VENTANA // 2 - 5 * ALTO_BOTONES // 6
    TEXTO_DER_X, TEXTO_DER_Y = ANCHO_VENTANA // 2 + 2 * ESPACIO_ENTRE_BOTONES + MARGEN_ENTRE_BOTONES, ALTO_VENTANA // 2 - 5 * ALTO_BOTONES // 6

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill='#0d1364')  # FRANJA SUPERIOR AZUL
    gamelib.draw_rectangle(VACIO, ALTO_VENTANA - FRANJA_AZUL_Y, ANCHO_VENTANA, ALTO_VENTANA, fill='#0d1364')  # FRANJA INFERIOR AZUL
    gamelib.draw_rectangle(BOTON_IZQ_X1, BOTON_IZQ_Y1, BOTON_IZQ_X2, BOTON_IZQ_Y2)  # BOTÓN TITULO "POKEMONES"
    gamelib.draw_rectangle(BOTON_DER_X1, BOTON_DER_Y1, BOTON_DER_X2, BOTON_DER_Y2)  # BOTÓN TITULO "EQUIPOS"
    gamelib.draw_text('POKEDEX', ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')  # TITULO
    gamelib.draw_text('De Ditto, Arean y Langer', CREDITOS_X, CREDITOS_Y, fill='white', size=10, anchor='n')  # CREDITOS
    gamelib.draw_text('POKEMONES', TEXTO_IZQ_X, TEXTO_IZQ_Y, fill='black', size=25, anchor='nw')  # TEXTO "POKEMONES"
    gamelib.draw_text('EQUIPOS', TEXTO_DER_X, TEXTO_DER_Y, fill='black', size=25, anchor='nw')  # TEXTO "EQUIPOS"
    gamelib.draw_end()

    return 'menu principal', 0, 0


def menu_pokemones(pag_pok, pag_equ):
    """
    Dibuja el menú de pokemones.
    """
    RX1, RY1, RX2, RY2 = BOTON_ROJO  # RETROCEDE AL MENÚ ANTERIOR
    NX1, NY1, NX2, NY2 = BOTON_NARANJA  # ABRE UN MENSAJE PARA BUSCAR UN POKEMON PARTICULAR

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)  # FONDO BLANCO
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill='#0d1364')  # FRANJA SUPERIOR AZUL
    gamelib.draw_rectangle(RX1, RY1, RX2, RY2, fill='red')  # BOTON ROJO
    gamelib.draw_rectangle(NX1, NY1, NX2, NY2, fill='orange')  # BOTON NARANJA
    gamelib.draw_text('POKEMONES', ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')  # TEXTO "POKEMONES"
    cuadritos_pokemones(pag_pok, pag_equ)
    gamelib.draw_end()

    return 'menu Pokemones', pag_pok, pag_equ


def menu_equipos(pag_pok, pag_equ):
    """
    Dibuja el menú de equipos.
    """
    RX1, RY1, RX2, RY2 = BOTON_ROJO  # RETROCEDE AL MENÚ ANTERIOR

    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill='#0d1364')
    gamelib.draw_rectangle(RX1, RY1, RX2, RY2, fill='red')  # BOTON ROJO
    gamelib.draw_text('EQUIPOS', ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    cuadritos_equipos(pag_pok, pag_equ)
    gamelib.draw_end()

    return 'menu Equipos', pag_pok, pag_equ


def cuadritos_pokemones(pag_pok, pag_equ):
    """
    Dibuja la visualización general de pokemones tomando información de 'pokemons.csv'.
    """
    nro_pok_nombre = lectores.lector_en_rango([pag_pok*NRO_FILAS*NRO_COLUMNAS - 10, pag_pok*NRO_FILAS*NRO_COLUMNAS + 28], pokemons)

    for i in range(NRO_FILAS):
        for j in range(NRO_COLUMNAS):
            gamelib.draw_rectangle(MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO, fill='#f1f8ff')

            if i == VACIO and j == VACIO:
                continue
            elif i == 3 and j == 6:
                continue
            else:
                elegido_en_ciclo = str(
                    pag_pok * (NRO_FILAS*NRO_COLUMNAS) + i * NRO_COLUMNAS + j - 2 * pag_pok)

                try:
                    nombre = nro_pok_nombre[elegido_en_ciclo][2]
                except KeyError:
                    nombre = ''

                gamelib.draw_text(nombre, ESPACIO_ENTRE_CUADROS + MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=11, anchor='nw')
    gamelib.draw_text('<-', BOTON_RETROCESO + MARGEN_CUADRITOS_IZQUIERDO, BOTON_RETROCESO + MARGEN_CUADRITOS_SUPERIOR, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MARGEN_CUADRITOS_IZQUIERDO - BOTON_RETROCESO + ESPACIO_ENTRE_CUADROS * (NRO_COLUMNAS) + XY_CUADRITO * NRO_COLUMNAS, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (NRO_FILAS) + XY_CUADRITO * NRO_FILAS - BOTON_RETROCESO, fill='black', size=30, anchor='se')


def cuadritos_equipos(pag_pok, pag_equ):
    """
    Dibuja la visualización general de equipos tomando información de 'equipos.csv'.
    """
    nro_pok_nombre = lectores.lector_en_rango([pag_equ*NRO_FILAS*NRO_COLUMNAS - 10, pag_equ*NRO_FILAS*NRO_COLUMNAS + 28], equipos)

    for i in range(NRO_FILAS):
        for j in range(NRO_COLUMNAS):
            gamelib.draw_rectangle(MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i,
                                   MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO, fill='#f1f8ff')

            if i == VACIO and j == VACIO:
                continue
            if i == VACIO and j == 1 and pag_equ == 0:
                gamelib.draw_text('+', ESPACIO_ENTRE_CUADROS*3.5 + MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, BOTON_RETROCESO + MARGEN_CUADRITOS_SUPERIOR*1.1, fill='black', size=28, anchor='nw')
                continue
            elif i == 3 and j == 6:
                continue
            else:
                elegido_en_ciclo = str(
                    pag_equ*(NRO_FILAS*NRO_COLUMNAS) + i * NRO_COLUMNAS + j - 2 * pag_equ)

                try:
                    nombre = nro_pok_nombre[elegido_en_ciclo][1]
                except KeyError:
                    nombre = ''

                gamelib.draw_text(nombre, ESPACIO_ENTRE_CUADROS + MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=11, anchor='nw')
    gamelib.draw_text('<-', BOTON_RETROCESO + MARGEN_CUADRITOS_IZQUIERDO, BOTON_RETROCESO + MARGEN_CUADRITOS_SUPERIOR, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MARGEN_CUADRITOS_IZQUIERDO - BOTON_RETROCESO + ESPACIO_ENTRE_CUADROS * (NRO_COLUMNAS) + XY_CUADRITO * NRO_COLUMNAS, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (NRO_FILAS) + XY_CUADRITO * NRO_FILAS - BOTON_RETROCESO, fill='black', size=30, anchor='se')


def un_pokemon(nro_pokemon, pag_pok, pag_equ):
    """
    Dibuja toda la información del pokemon que recibe por parámetro.
    """
    RX1, RY1, RX2, RY2 = BOTON_ROJO  # RETROCEDE AL MENÚ ANTERIOR
    tipo_de_stat = ('Numero', 'Imagen', 'Nombre', 'Tipos: ', 'HP: ', 'ATK: ', 'DEF: ', 'Spe-At: ', 'Spe-De: ', 'SPD: ')

    info = lectores.lector_en_rango([nro_pokemon, nro_pokemon], pokemons)
    contenido = info[str(nro_pokemon)]
    
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill='#0d1364')
    gamelib.draw_text((contenido[2]+', '+contenido[0]), ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    for i in range (3, 10):
        gamelib.draw_text(tipo_de_stat[i] + contenido[i], 5 * ANCHO_VENTANA // 10, i * ALTO_VENTANA // 10, fill='black', size=30, anchor='w') 
    gamelib.draw_image(contenido[1], VACIO, ALTO_VENTANA // 4)
    gamelib.draw_rectangle(RX1, RY1, RX2, RY2, fill='red')
    gamelib.draw_end()

    return 'Individual Pokemon', pag_pok, pag_equ


def un_equipo(nro_equipo, pag_pok, pag_equ):
    """
    Dibuja toda la información del equipo que recibe por parámetro.
    """
    posicion_alto = 2
    contador_pokemones = 0
    
    RX1, RY1, RX2, RY2 = BOTON_ROJO  # RETROCEDE AL MENÚ ANTERIOR

    info = lectores.lector_en_rango([nro_equipo, nro_equipo], equipos)
    contenido = info[str(nro_equipo)]
    numero_pokemones_en_equipo = (len(contenido) - 3) // 2
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill='#0d1364')
    gamelib.draw_text((contenido[1]+', '+ contenido[0]), ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    
    for i in range (2, 13, 2):
        if contador_pokemones == numero_pokemones_en_equipo:
            break
        gamelib.draw_text(contenido[i],   1 * ANCHO_VENTANA // 9, (posicion_alto) * ALTO_VENTANA // 8, fill='black', size=30, anchor='w')
        gamelib.draw_text(contenido[i+1], 8 * ANCHO_VENTANA // 9, (posicion_alto) * ALTO_VENTANA // 8, fill='black', size=20, anchor='e')
        contador_pokemones += 1
        posicion_alto += 1
        
    gamelib.draw_rectangle(RX1, RY1, RX2, RY2, fill='red')
    gamelib.draw_end()

    return 'Individual Equipo', pag_pok, pag_equ


def creador_equipos():
    pokemones_elegidos = []
    poderes_elegidos = []
    elegido = ''
    nombre_equipo = ''
    total_de_pokemones = lectores.cuantas_lineas_archivo(pokemons)
    
    while nombre_equipo == '':
        nombre_equipo = gamelib.input(MENSAJE_NOMBRE)
        if nombre_equipo == '':
            gamelib.say(MENSAJE_NOMBRE_ERROR)
        if nombre_equipo == None:
            return None
    nombre_equipo.upper()
    
    while len(pokemones_elegidos) <= MAX_NRO_POKEMONES_EQUIPO: 
        elegido = gamelib.input(MENSAJE_POKEMON)

        if elegido == None:
            return None
        
        elif elegido == '':
            break
        
        while not elegido.isdigit() and (1 <= elegido <= total_de_pokemones or elegido in pokemones_elegidos):
            gamelib.say(MENSAJE_POKEMON_ERROR)
            elegido = gamelib.input(MENSAJE_POKEMON)
            
        aux_nombre = lectores.lector_por_numero(int(elegido), movimientos)
        gamelib.say((MENSAJE_ELEGISTE_POKEMON.format(aux_nombre[0], nombre_equipo, MAX_NRO_POKEMONES_EQUIPO)))
        
        pokemones_elegidos.append(int(elegido))
        
        if len(pokemones_elegidos) == 0:
                continue
            
    for monstruo in pokemones_elegidos:
        info = lectores.lector_por_numero(monstruo, movimientos)
        lista_movimientos = info[1].split(',')
        aux = []
        gamelib.say(MENSAJE_MOVIMIENTOS.format(info[0]))
        
        while len(aux) < MAX_NRO_MOVIMIENTOS_POKEMON or len(aux) == len(lista_movimientos):
            eleccion_pequena = gamelib.input((MENSAJE_MOVIMIENTOS_OPCIONES.format(info[0], lista_movimientos)))
            
            if eleccion_pequena == None:
                return None
            
            if eleccion_pequena in aux:
                gamelib.say(MENSAJE_MOVIMIENTOS_REPETIDO)
                continue
            
            elif eleccion_pequena == '':
                if len(aux) == 0:
                    continue
                break
            
            while not eleccion_pequena in lista_movimientos:
                eleccion_pequena = gamelib.input((MENSAJE_MOVIMIENTOS_ERROR.format(info[1])))
                if eleccion_pequena == '' or eleccion_pequena == None:
                    break
            
            aux.append(eleccion_pequena)

        poderes_elegidos.append(aux)

    return nombre_equipo, pokemones_elegidos, poderes_elegidos


def menu_creador(pag_pok, pag_equ):
    """
    Dibuja el menú creador y llama a creador_equipo().
    Escribe los resultados de creador_equipo() en 'equipos.csv'
    """
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill = '#0d1364')
    gamelib.draw_text('CREACIÓN DE UN EQUIPO NUEVO', ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()

    seleccion_usuario = creador_equipos()
    
    if not seleccion_usuario == None:
        nombre_equipo, pokemones, poderes = seleccion_usuario
        nuevo_equipo_a_archivo(nombre_equipo, pokemones, poderes)
    
    return menu_equipos(pag_pok, pag_equ)


def nuevo_equipo_a_archivo(nombre_equipo, pokemones, poderes):
    """
    Escribe los resultados de creador_equipo() en 'equipos.csv' 
    """
    largo_equipos = 0
    
    with open(equipos) as archivo:
        for linea in archivo:
            if linea != '\n':
                largo_equipos += 1
                
    largo_equipos = str(largo_equipos)+';'
    nombre_equipo += ';'

    for i in range (len(pokemones)):
        poder = ','.join(poderes[i])
        nombre_equipo += str(pokemones[i]) + ';' + str(poder) + ';'

    with open(equipos, 'a') as archivo:
        archivo.write('\n' + largo_equipos + nombre_equipo)
        
        
def que_pokemon(x, y, pag_pok, pag_equ):
    xcuadro = (x - MARGEN_CUADRITOS_IZQUIERDO) // (XY_CUADRITO + ESPACIO_ENTRE_CUADROS)
    ycuadro = (y - MARGEN_CUADRITOS_SUPERIOR)  // (XY_CUADRITO + ESPACIO_ENTRE_CUADROS)
    nro_pokemon = ycuadro * NRO_COLUMNAS + xcuadro + pag_pok * 26

    if (nro_pokemon - pag_pok * 26) == 0:
        if pag_pok > 0:
            return menu_pokemones(pag_pok-1, pag_equ)
        return menu_pokemones(pag_pok, pag_equ)

    if (nro_pokemon - pag_pok * 26) == 27:
        return menu_pokemones(pag_pok+1, pag_equ)

    if nro_pokemon > 0:
        return un_pokemon(nro_pokemon, pag_pok, pag_equ)


def que_equipo(x, y, pag_pok, pag_equ):
    xcuadro = (x - MARGEN_CUADRITOS_IZQUIERDO) // (XY_CUADRITO + ESPACIO_ENTRE_CUADROS)
    ycuadro = (y - MARGEN_CUADRITOS_SUPERIOR)  // (XY_CUADRITO + ESPACIO_ENTRE_CUADROS)
    nro_equipo = ycuadro * NRO_COLUMNAS + xcuadro + pag_equ * 26

    if (nro_equipo - pag_equ * 26) == 0:
        if pag_equ > 0:
            return menu_equipos(pag_pok, pag_equ - 1)
        return menu_equipos(pag_pok, pag_equ)

    if (nro_equipo - pag_equ * 26) == 27:
        return menu_equipos(pag_pok, pag_equ + 1)

    if nro_equipo == 1:
        return menu_creador(pag_pok, pag_equ)

    if nro_equipo > 1:
        return un_equipo(nro_equipo, pag_pok, pag_equ)


def navegacion(x, y, juego):
    """
    La función navegación llama a la función correcta dependiendo de 
    donde está parado el usuario en el pokedex y donde hizo click.
    """
    RX1, RY1, RX2, RY2 = BOTON_ROJO
    NX1, NY1, NX2, NY2 = BOTON_NARANJA
    BOTON_IZQ_X1, BOTON_IZQ_Y1, BOTON_IZQ_X2, BOTON_IZQ_Y2 = MARGEN_ENTRE_BOTONES, BOTON_Y1, ANCHO_VENTANA // 2 - ESPACIO_ENTRE_BOTONES, BOTON_Y2
    BOTON_DER_X1, BOTON_DER_Y1, BOTON_DER_X2, BOTON_DER_Y2 = ANCHO_VENTANA // 2 + ESPACIO_ENTRE_BOTONES, BOTON_Y1, ANCHO_VENTANA - MARGEN_ENTRE_BOTONES, BOTON_Y2

    pag_pok = juego[1]
    pag_equ = juego[2]

    if juego[0] == 'menu principal':
        if BOTON_IZQ_X1 < x < BOTON_IZQ_X2 and BOTON_IZQ_Y1 < y < BOTON_IZQ_Y2:
            return menu_pokemones(pag_pok, pag_equ)  # BOTON POKEMONES
        if BOTON_DER_X1 < x < BOTON_DER_X2 and BOTON_DER_Y1 < y < BOTON_DER_Y2:
            return menu_equipos(pag_pok, pag_equ)  # BOTON EQUIPOS

    if juego[0] == 'menu Pokemones':
        if RX1 < x < RX2 and RY1 < y < RY2:
            return menu_principal()  # BOTON ROJO
        if NX1 < x < NX2 and NY1 < y < NY2:
            return buscador_particular(pag_pok, pag_equ)  # BOTON NARANJA
        return que_pokemon(x, y, pag_pok, pag_equ)

    if juego[0] == 'menu Equipos':
        if RX1 < x < RX2 and RY1 < y < RY2:
            return menu_principal()  # BOTON ROJO
        return que_equipo(x, y, pag_pok, pag_equ)

    if juego[0] == 'Individual Pokemon':
        if RX1 < x < RX2 and RY1 < y < RY2:
            return menu_pokemones(pag_pok, pag_equ)  # BOTON ROJO

    if juego[0] == 'Individual Equipo':
        if RX1 < x < RX2 and RY1 < y < RY2:
            return menu_equipos(pag_pok, pag_equ)  # BOTON ROJO

    return 'menu principal', 0, 0
