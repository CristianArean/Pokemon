import gamelib
import lectores
import csv
from lectores import lector_por_numero
equipos = 'equipos.csv'
movimientos = 'movimientos.csv'
pokemons = 'pokemons.csv'

ANCHO_VENTANA = 900
ALTO_VENTANA = 600

MENSAJE_BUSCADOR = 'Ingrese el número del pokemon que desea ver.'
MENSAJE_BUSCADOR_ERROR = 'No ingresó un digito válido. Ingrese el número del pokemon que desea ver'
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
TOTAL_POKEMONES = lectores.cuantas_lineas_archivo(pokemons)

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
MITAD_ANCHO = ANCHO_VENTANA // 2

BOTON_ROJO = BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO * 2, BOTON_RETROCESO * 2
BOTON_NARANJA = ANCHO_VENTANA - BOTON_RETROCESO * 2, BOTON_RETROCESO, ANCHO_VENTANA - BOTON_RETROCESO, BOTON_RETROCESO * 2
BOTON_EDITAR_EQUIPO = 2 * ANCHO_VENTANA // 5, 7 * ALTO_VENTANA // 8, 3 * ANCHO_VENTANA // 5, 7 * ALTO_VENTANA // 8 + ALTO_BOTONES
FLECHA_IZQ = BOTON_RETROCESO + MARGEN_CUADRITOS_IZQUIERDO, BOTON_RETROCESO + MARGEN_CUADRITOS_SUPERIOR
FLECHA_DER = MARGEN_CUADRITOS_IZQUIERDO - BOTON_RETROCESO + ESPACIO_ENTRE_CUADROS * (NRO_COLUMNAS) + XY_CUADRITO * NRO_COLUMNAS, MARGEN_CUADRITOS_SUPERIOR + ESPACIO_ENTRE_CUADROS * (NRO_FILAS) + XY_CUADRITO * NRO_FILAS - BOTON_RETROCESO


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
    numero = gamelib.input(MENSAJE_BUSCADOR)
    
    if numero == None or numero == '':
        return 'menu Pokemones', pag_pok, pag_equ 
    else:
        while not (numero.isdigit() and int(numero) <= TOTAL_POKEMONES): 
            numero = gamelib.input(MENSAJE_BUSCADOR_ERROR)
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
    cuadritos(pag_pok, pag_equ, 'pokemon')
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
    cuadritos(pag_pok, pag_equ, 'equipo')
    gamelib.draw_end()

    return 'menu Equipos', pag_pok, pag_equ


def cuadritos(pag_pok, pag_equ, opcion):
    if opcion == 'pokemon':
        pag = pag_pok
        archivo = pokemons
    elif opcion == 'equipo':
        pag = pag_equ
        archivo = equipos
    principio_rango = pag * NRO_FILAS * NRO_COLUMNAS - 10
    ultimo_rango = pag * NRO_FILAS * NRO_COLUMNAS + 28
    biblioteca_rango = lectores.lector_en_rango([principio_rango, ultimo_rango], archivo)
    IZQ_X, IZQ_Y = FLECHA_IZQ
    DER_X, DER_Y = FLECHA_DER
    MAS_X, MAS_Y = ESPACIO_ENTRE_CUADROS * 3.5 + MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS, BOTON_RETROCESO + MARGEN_CUADRITOS_SUPERIOR * 1.1

    for i in range(NRO_FILAS):
        for j in range(NRO_COLUMNAS):
            X1 = MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, 
            Y1 = MARGEN_CUADRITOS_SUPERIOR  + ESPACIO_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i
            X2 = MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO
            Y2 = MARGEN_CUADRITOS_SUPERIOR  + ESPACIO_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO
            X_NOMBRE = MARGEN_CUADRITOS_IZQUIERDO + ESPACIO_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + ESPACIO_ENTRE_CUADROS
            gamelib.draw_rectangle(X1, Y1, X2, Y2, fill='#f1f8ff')
                
            if (i == VACIO and j == VACIO) or (i == 3 and j == 6):
                continue

            iteracion = str(pag * (NRO_FILAS * NRO_COLUMNAS) + i * NRO_COLUMNAS + j - 2 * pag)

            try:
                if opcion == 'pokemon':
                    nombre = biblioteca_rango[iteracion][2]
                elif opcion == 'equipo':
                    nombre = biblioteca_rango[iteracion][1]
            except KeyError:
                nombre = ''

            gamelib.draw_text(nombre, X_NOMBRE, Y1, fill='black', size=11, anchor='nw')
            
    if opcion == 'equipo' and pag == 0:
        gamelib.draw_text('+', MAS_X, MAS_Y, fill='black', size=28, anchor='nw')  # SIMBOLO SUMA PARA AGREGAR UN NUEVO EQUIPO
    else:
        gamelib.draw_text('<-', IZQ_X, IZQ_Y, fill='black', size=30, anchor='nw')  # FLECHA PARA PASAR A LA PÁGINA ANTERIOR
        
    gamelib.draw_text('->', DER_X, DER_Y, fill='black', size=30, anchor='se')  # FLECHA PARA PASAR A LA PÁGINA SIGUIENTE

    
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


def numero_a_nombre(nro):
    """
    Recibe el número de un pokemon y retorna su nombre en string.
    """
    info = lectores.lector_por_numero(nro, pokemons)
    return info[2]


def un_equipo(nro_equipo, pag_pok, pag_equ):
    """
    Dibuja toda la información del equipo que recibe por parámetro.
    """
    posicion_alto = 2
    contador_pokemones = 0
    
    RX1, RY1, RX2, RY2 = BOTON_ROJO  # RETROCEDE AL MENÚ ANTERIOR
    EX1, EY1, EX2, EY2 = BOTON_EDITAR_EQUIPO  #ABRE EL MENÚ DE EDICIÓN

    info = lectores.lector_en_rango([nro_equipo, nro_equipo], equipos)
    contenido = info[str(nro_equipo)]
    numero_pokemones_en_equipo = (len(contenido) - 3) // 2
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill='#0d1364')  #FRANJA AZUL
    gamelib.draw_rectangle(RX1, RY1, RX2, RY2, fill='red')  #BOTON ROJO
    gamelib.draw_rectangle(EX1, EY1, EX2, EY2, fill='#f1f8ff')  #BOTON EDITAR
    gamelib.draw_text('EDITAR', MITAD_ANCHO, EY1, fill = 'black', size = 25, anchor = 'n')  #TEXTO BOTON EDITAR
    gamelib.draw_text((contenido[1]+', '+ contenido[0]), ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')  #NOMBRE DE EQUIPO Y NÚMERO
    
    for i in range (2, 13, 2):
        if contador_pokemones == numero_pokemones_en_equipo:
            break
        gamelib.draw_text(numero_a_nombre(int(contenido[i])),   1 * ANCHO_VENTANA // 9, (posicion_alto) * ALTO_VENTANA // 8, fill='black', size=30, anchor='w')  #NOMBRE DE POKEMON
        gamelib.draw_text(contenido[i+1],                       8 * ANCHO_VENTANA // 9, (posicion_alto) * ALTO_VENTANA // 8, fill='black', size=20, anchor='e')  #MOVMIENTOS DE POKEMON
        contador_pokemones += 1
        posicion_alto += 1
        
    gamelib.draw_end()

    return 'Individual Equipo', pag_pok, pag_equ, nro_equipo


def recibir_nombre_equipo():
    """
    Solicita al usuario el nombre del nuevo equipo
    """
    nombre_equipo = ''
    
    while nombre_equipo == '':
        nombre_equipo = gamelib.input(MENSAJE_NOMBRE)
        if nombre_equipo == '':
            gamelib.say(MENSAJE_NOMBRE_ERROR)
        if nombre_equipo == None:
            return None
        
    nombre_equipo.upper()
    
    return nombre_equipo
    
    
def recibir_pokemones_equipo(nombre_equipo):
    """
    Solicita al usuario los pokemones del nuevo equipo.
    Recibe el nombre del nuevo equipo.
    """
    pokemones_elegidos = []
    total_de_pokemones = lectores.cuantas_lineas_archivo(pokemons)
    
    while len(pokemones_elegidos) <= MAX_NRO_POKEMONES_EQUIPO:
        elegido = ''
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
            
    return pokemones_elegidos


def recibir_movimientos_equipo(pokemones_elegidos):
    """
    Solicita al usuario los poderes de los pokemones del nuevo equipo.
    Recibe los pokemones elegidos.
    """
    poderes_elegidos = []
    for monstruo in pokemones_elegidos:
        info = lectores.lector_por_numero(monstruo, movimientos)
        info[1].rstrip('\n')
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
        
    return poderes_elegidos


def creador_equipos():
    """
    Llama a las tres funciones que le piden la información necesaria al usuario para
    crear un equipo nuevo
    """
    nombre_equipo = recibir_nombre_equipo()
    if nombre_equipo == None:
        return None
    
    pokemones_elegidos = recibir_pokemones_equipo(nombre_equipo)
    if pokemones_elegidos == None:
        return None
    
    poderes_elegidos = recibir_movimientos_equipo(pokemones_elegidos)
    if poderes_elegidos == None:
        return None

    return nombre_equipo, pokemones_elegidos, poderes_elegidos


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

def editar_equipos(nro_equipo):
    #comenzamos leyendo el archivo y guardamos todo en una lista
    with open (equipos, "r") as inpf:
        lector = csv.reader(inpf)
        data = list(reader)
    #pedimos al usuario que quiere borrar
    
    primer_int = gamelib.input("que pokemon desea borrar[ingrese su numero]?")
    while not primer_int.isnumeric():
      primer_int = gamelib.input("No eligio un pokemon, que pokemon desea borrar[ingrese su numero]?")
    
    #pedimos a la funcion la lista con el equipo que quiere borrar
    #excluimos los primeros dos items ya que se podria dar el caso de querer borrar un pokemon y que el numero de equipo sea el mismo
    #para evitar eso no tomamos en la lista esos dos items

    lista = lector_por_numero(nro_equipo, equipos)[2::]
    
    #tomo sus enteros y guardo la posicion en un diccionario
    
    orden = {n: lista.index(n) for n in lista if n.isnumeric()}
    
    #convierto las keys en una lista
    
    keys = list(orden.keys())
    
    #tomo la posicion del primer numero en la lista
    
    primer_numero_idx = keys.index(primer_int)
    
    #si es el ultimo, elimino el ultimo fragmento de lista

    if primer_numero_idx + 1 == len(keys):
        lista_nueva = lista[:orden[primer_int]]

    #de lo contrario me quedo con lo anterior al primer numero
    # y lo posterior al segundo eliminando lo del medio
    
    else:
        segundo_numero = keys[primer_numero_idx + 1]
        lista_nueva = lector_por_numero(nro_equipo, equipos)[:2] + lista[:orden[primer_int]] + lista[orden[segundo_numero]:]

    #modificamos el item de esa lista correspondiente al equipo (que tambien es una lista)
    
    data.pop(nro_equipo)
    data.insert(nro_equipo, lista_nueva)
  
    #abrimos el archivo nuevamente pero en modo lectura para poder cargarle los equipos no modificados y el ya modificado
    
    with open (equipos, "w") as outf:
        escritor = csv.writer(outf, delimiter=';', lineterminator='\n')
        escritor.writerows(data) 

        
        
def que_pokemon(x, y, pag_pok, pag_equ):
    """
    Recibe la posición de un click y retorna qué pokemon debe mostrar dependiendo del número de página.
    """
    xcuadro = (x - MARGEN_CUADRITOS_IZQUIERDO) // (XY_CUADRITO + ESPACIO_ENTRE_CUADROS)
    ycuadro = (y - MARGEN_CUADRITOS_SUPERIOR)  // (XY_CUADRITO + ESPACIO_ENTRE_CUADROS)
    nro_pokemon = ycuadro * NRO_COLUMNAS + xcuadro + pag_pok * 26

    if (nro_pokemon - pag_pok * 26) == 0:
        if pag_pok > 0:
            return menu_pokemones(pag_pok-1, pag_equ)
        return menu_pokemones(pag_pok, pag_equ)

    if (nro_pokemon - pag_pok * 26) == 27:
        return menu_pokemones(pag_pok+1, pag_equ)

    if nro_pokemon > 0 and nro_pokemon <= TOTAL_POKEMONES:
        return un_pokemon(nro_pokemon, pag_pok, pag_equ)
    
    return menu_pokemones(pag_pok, pag_equ)


def que_equipo(x, y, pag_pok, pag_equ):
    """
    Recibe la posición de un click y retorna qué equipo debe mostrar dependiendo del número de página.
    """
    xcuadro = (x - MARGEN_CUADRITOS_IZQUIERDO) // (XY_CUADRITO + ESPACIO_ENTRE_CUADROS)
    ycuadro = (y - MARGEN_CUADRITOS_SUPERIOR)  // (XY_CUADRITO + ESPACIO_ENTRE_CUADROS)
    nro_equipo = ycuadro * NRO_COLUMNAS + xcuadro + pag_equ * 26
    total_equipos = lectores.cuantas_lineas_archivo(equipos)

    if (nro_equipo - pag_equ * 26) == 0 and pag_equ != 0:
        if pag_equ > 0:
            return menu_equipos(pag_pok, pag_equ - 1)
        return menu_equipos(pag_pok, pag_equ)

    if (nro_equipo - pag_equ * 26) == 27:
        return menu_equipos(pag_pok, pag_equ + 1)

    if nro_equipo == 0 and pag_equ == 0:
        return menu_creador(pag_pok, pag_equ)

    if nro_equipo > 0 and nro_equipo <= total_equipos:
        return un_equipo(nro_equipo, pag_pok, pag_equ)
    
    return menu_equipos(pag_pok, pag_equ)


def navegacion(x, y, juego):
    """
    La función navegación llama a la función correcta dependiendo de 
    donde está parado el usuario en el pokedex y donde hizo click.
    """
    RX1, RY1, RX2, RY2 = BOTON_ROJO
    NX1, NY1, NX2, NY2 = BOTON_NARANJA
    EX1, EY1, EX2, EY2 = BOTON_EDITAR_EQUIPO  
    IZQ_X1, IZQ_Y1, IZQ_X2, IZQ_Y2 = MARGEN_ENTRE_BOTONES, BOTON_Y1, ANCHO_VENTANA // 2 - ESPACIO_ENTRE_BOTONES, BOTON_Y2
    DER_X1, DER_Y1, DER_X2, DER_Y2 = ANCHO_VENTANA // 2 + ESPACIO_ENTRE_BOTONES, BOTON_Y1, ANCHO_VENTANA - MARGEN_ENTRE_BOTONES, BOTON_Y2

    pag_pok = juego[1]
    pag_equ = juego[2]

    if juego[0] == 'menu principal':
        if IZQ_X1 < x < IZQ_X2 and IZQ_Y1 < y < IZQ_Y2:
            return menu_pokemones(pag_pok, pag_equ)  # BOTON POKEMONES
        if DER_X1 < x < DER_X2 and DER_Y1 < y < DER_Y2:
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
        if EX1 < x < EX2 and EY1 < y < EY2:
            return editar_equipos(juego[3])  # BOTON EDITAR EQUIPOS

    return 'menu principal', 0, 0
