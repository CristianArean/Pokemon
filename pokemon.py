import gamelib
from tda import Pila 
from tda import Cola
from tkinter import simpledialog
ANCHO_VENTANA = 900
ALTO_VENTANA = 600

VACIO = 0
NRO_COLUMNAS = 7
NRO_FILAS = 4

TITLE_Y = 70 
MRG_HORZ_BOTONES = 70
ALTO_BOTONES = 50
ESP_ENTRE_BOTON = 30
BTN_Y1 = ALTO_VENTANA // 2 - ALTO_BOTONES
BTN_Y2 = ALTO_VENTANA // 2
XY_CUADRITO = 100
MRG_CUADRITOS_SUP = 90
MRG_CUADRITOS_IZQ = 70
ESP_ENTRE_CUADROS = 10
BOTON_RETROCESO = 30
FRANJA_AZUL_Y = 88

def crear_juego():
    """
    Crea el juego, retornando 'menu principal' y creando 'equipos.csv' si aún no existe. 
    Si 'equipos.csv' ya existe, será ultilizado para guardar los equipos ya guardados.
    """
    menu_memorizado = 'menu principal'

    try:
        with open('equipos.csv', 'x') as archivo:
            pass
    except:
        return 'menu principal', 0, 0

    with open('equipos.csv', 'w') as archivo:
        for _ in range (1):
            archivo.writelines('equipo_nombre;integrante1;movimientos1;integrante2;movimientos2;integrante3;movimientos3;integrante4;movimientos4;integrante5;movimientos5;integrante6;movimientos6')
    return 'menu principal', 0, 0

def lector(nros, nombre_archivo): 
    """
    Lee el archivo ingresado por parametro, ignora la primera linea y retorna un diccionario con el numero de linea como llave
    El diccionario contiene toda la info del rango de lineas solicitado (en forma de lista). Si es necesaria la información de solo una linea, 
    debe ingresarse una lista con esa unica linea repetida.
    """
    lineas_solicitadas = Cola()
    minimo = min(nros)
    maximo = max(nros)
    contador = -1
    rta = {}

    with open(nombre_archivo) as archivo:
        for _ in range (maximo+1):
            linea = archivo.readline().rstrip('\n')
            lineas_solicitadas.encolar(linea)
            contador += 1
            if contador == (maximo - minimo +1):
                lineas_solicitadas.desencolar()
                contador -= 1

    while not lineas_solicitadas.esta_vacia():
        lista_atributos = (lineas_solicitadas.desencolar()).split(';')
        rta[lista_atributos[0]] = lista_atributos
    return rta

def lector_movimientos(nro, nombre_archivo):
    """
    Lee el archivo ingresado por parametro, ignora la primera linea y retorna un diccionario con el numero de linea como llave.
    El diccionario contiene todos los movimientos del pokemon solicitado.
    Retorna la información de solo un pokemon.
    """
    contador = 1

    with open(nombre_archivo) as archivo:
        for linea in archivo:
            leido = linea.readline()
            contador += 1
            if contador == nro:
                return leido.split(';')

def menu_principal():
    """
    Dibuja el menú principal.
    """
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill = '#0d1364')
    gamelib.draw_rectangle(VACIO, ALTO_VENTANA - FRANJA_AZUL_Y, ANCHO_VENTANA, ALTO_VENTANA, fill = '#0d1364')
    gamelib.draw_text('POKEDEX', ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    gamelib.draw_text('De Ditto, Arean y Langer', ANCHO_VENTANA // 2, ALTO_VENTANA - 2*TITLE_Y//3, fill='white', size=10, anchor='n')
    gamelib.draw_rectangle(MRG_HORZ_BOTONES, BTN_Y1, ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON, BTN_Y2) #Rectangulo de botón izq.
    gamelib.draw_rectangle(ANCHO_VENTANA // 2 + ESP_ENTRE_BOTON, BTN_Y1, ANCHO_VENTANA - MRG_HORZ_BOTONES, BTN_Y2) #Rectangulo de botón der.
    gamelib.draw_text('POKEMONES', MRG_HORZ_BOTONES*2, ALTO_VENTANA // 2 - 5*ALTO_BOTONES//6, fill='black', size=25, anchor='nw') #Texto de botón izq.
    gamelib.draw_text('EQUIPOS', ANCHO_VENTANA // 2 +  2*ESP_ENTRE_BOTON + MRG_HORZ_BOTONES, ALTO_VENTANA // 2 - 5*ALTO_BOTONES//6, fill='black', size=25, anchor='nw') #Texto de botón der.
    gamelib.draw_end()
    menu_memorizado = 'menu principal'
    return 'menu principal', 0, 0

def menu_pokemones(pag_pok, pag_equ): 
    """
    Dibuja el menú de pokemones.
    """  
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill = '#0d1364')
    gamelib.draw_text('POKEMONES', ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    cuadritos_pokemones(pag_pok, pag_equ)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    menu_memorizado = 'menu Pokemones', pag_pok, pag_equ
    return 'menu Pokemones', pag_pok, pag_equ

def menu_equipos(pag_pok, pag_equ): 
    """
    Dibuja el menú de equipos.
    """ 
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill = '#0d1364')
    gamelib.draw_text('EQUIPOS', ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    cuadritos_equipos(pag_pok, pag_equ)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    menu_memorizado = 'menu Equipos', 0, 0
    return 'menu Equipos', 0, 0

def cuadritos_pokemones(pag_pok, pag_equ): 
    """
    Dibuja la visualización general de pokemones tomando información de 'pokemons.csv'.
    """
    nro_pok_nombre = lector([pag_pok*NRO_FILAS*NRO_COLUMNAS -10, pag_pok*NRO_FILAS*NRO_COLUMNAS +28], 'pokemons.csv') 
    print (nro_pok_nombre)

    for i in range (NRO_FILAS): 
        for j in range (NRO_COLUMNAS): 
            gamelib.draw_rectangle(MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO, fill='#f1f8ff')
            
            if i == VACIO and j == VACIO:
                continue
            elif i == 3 and j == 6:
                continue
            else: 
                elegido_en_ciclo = str(pag_pok*(NRO_FILAS*NRO_COLUMNAS) + i*NRO_COLUMNAS + j - 2*pag_pok)
                
                try:
                    nombre = nro_pok_nombre[elegido_en_ciclo][2]
                except KeyError:
                    nombre = ''

                gamelib.draw_text(nombre, ESP_ENTRE_CUADROS + MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=11, anchor='nw')
    gamelib.draw_text('<-', BOTON_RETROCESO + MRG_CUADRITOS_IZQ, BOTON_RETROCESO + MRG_CUADRITOS_SUP, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MRG_CUADRITOS_IZQ - BOTON_RETROCESO + ESP_ENTRE_CUADROS * (NRO_COLUMNAS) + XY_CUADRITO * NRO_COLUMNAS, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (NRO_FILAS) + XY_CUADRITO * NRO_FILAS - BOTON_RETROCESO, fill='black', size=30, anchor='se')

def cuadritos_equipos(pag_pok, pag_equ): 
    """
    Dibuja la visualización general de equipos tomando información de 'equipos.csv'.
    """
    nro_pok_nombre = lector([pag_equ*NRO_FILAS*NRO_COLUMNAS -10, pag_equ*NRO_FILAS*NRO_COLUMNAS +28], 'equipos.csv') 
    print (nro_pok_nombre)

    for i in range (NRO_FILAS): 
        for j in range (NRO_COLUMNAS): 
            gamelib.draw_rectangle(MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO, fill='#f1f8ff')
            
            if i == VACIO and j == VACIO:
                continue
            if i == VACIO and j == 1:
                gamelib.draw_text('+', ESP_ENTRE_CUADROS*3.5 + MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, BOTON_RETROCESO + MRG_CUADRITOS_SUP*1.1, fill='black', size=28, anchor='nw')
            elif i == 3 and j == 6:
                continue
            else: 
                elegido_en_ciclo = str(pag_equ*(NRO_FILAS*NRO_COLUMNAS) + i*NRO_COLUMNAS + j - 2*pag_equ)

                try:
                    nombre = nro_pok_nombre[elegido_en_ciclo][1]
                except KeyError:
                    nombre = ''

                gamelib.draw_text(nombre, ESP_ENTRE_CUADROS + MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=11, anchor='nw')
    gamelib.draw_text('<-', BOTON_RETROCESO + MRG_CUADRITOS_IZQ, BOTON_RETROCESO + MRG_CUADRITOS_SUP, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MRG_CUADRITOS_IZQ - BOTON_RETROCESO + ESP_ENTRE_CUADROS * (NRO_COLUMNAS) + XY_CUADRITO * NRO_COLUMNAS, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (NRO_FILAS) + XY_CUADRITO * NRO_FILAS - BOTON_RETROCESO, fill='black', size=30, anchor='se')

def un_pokemon(nro_pokemon, pag_pok, pag_equ):
    """
    Dibuja toda la información del pokemon que recibe por parámetro.
    """
    info = lector([nro_pokemon, nro_pokemon], 'pokemons.csv')
    contenido = info[str(nro_pokemon)]
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill = '#0d1364')
    gamelib.draw_text((contenido[2]+', '+contenido[0]), ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    gamelib.draw_text('Tipos: '+contenido[3], 5* ANCHO_VENTANA // 10, 3 * ALTO_VENTANA // 10, fill='black', size=30, anchor='w')
    gamelib.draw_text('HP: '+contenido[4], 5* ANCHO_VENTANA // 10, 4 * ALTO_VENTANA // 10, fill='black', size=30, anchor='w') 
    gamelib.draw_text('ATK: '+contenido[5], 5* ANCHO_VENTANA // 10, 5 * ALTO_VENTANA // 10, fill='black', size=30, anchor='w')
    gamelib.draw_text('DEF: '+contenido[6], 5* ANCHO_VENTANA // 10, 6 * ALTO_VENTANA // 10, fill='black', size=30, anchor='w')
    gamelib.draw_text('Spe-At: '+contenido[7], 5* ANCHO_VENTANA // 10, 7 * ALTO_VENTANA // 10, fill='black', size=30, anchor='w')
    gamelib.draw_text('Spe-De: '+contenido[8], 5* ANCHO_VENTANA // 10, 8 * ALTO_VENTANA // 10, fill='black', size=30, anchor='w')
    gamelib.draw_text('SPD: '+contenido[9], 5* ANCHO_VENTANA // 10, 9 * ALTO_VENTANA // 10, fill='black', size=30, anchor='w') 
    gamelib.draw_image(contenido[1], VACIO, ALTO_VENTANA // 4)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    menu_memorizado = 'Individual Pokemon', pag_pok, pag_equ
    return 'Individual Pokemon', pag_pok, pag_equ

def un_equipo(nro_equipo, pag_pok, pag_equ):
    """
    Dibuja toda la información del equipo que recibe por parámetro.
    """
    info = lector([nro_equipo, nro_equipo], 'equipos.csv')
    contenido = info[str(nro_equipo)]
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, FRANJA_AZUL_Y, fill = '#0d1364')
    gamelib.draw_text((contenido[1]+', '+contenido[0]), ANCHO_VENTANA // 2, TITLE_Y, fill='white', size=30, anchor='s')
    gamelib.draw_text(contenido[2], 1* ANCHO_VENTANA // 9, 2 * ALTO_VENTANA // 8, fill='black', size=30, anchor='w')
    gamelib.draw_text(contenido[3], 8* ANCHO_VENTANA // 9, 2 * ALTO_VENTANA // 8, fill='black', size=20, anchor='e')
    gamelib.draw_text(contenido[4], 1* ANCHO_VENTANA // 9, 3 * ALTO_VENTANA // 8, fill='black', size=30, anchor='w') # ajustar alturas puse // 6 evitar superposiciosion
    gamelib.draw_text(contenido[5], 8* ANCHO_VENTANA // 9, 3 * ALTO_VENTANA // 8, fill='black', size=20, anchor='e')
    gamelib.draw_text(contenido[6], 1* ANCHO_VENTANA // 9, 4 * ALTO_VENTANA // 8, fill='black', size=30, anchor='w')
    gamelib.draw_text(contenido[7], 8* ANCHO_VENTANA // 9, 4 * ALTO_VENTANA // 8, fill='black', size=20, anchor='e')
    gamelib.draw_text(contenido[8], 1* ANCHO_VENTANA // 9, 5 * ALTO_VENTANA // 8, fill='black', size=30, anchor='w')
    gamelib.draw_text(contenido[9], 8* ANCHO_VENTANA // 9, 5 * ALTO_VENTANA // 8, fill='black', size=20, anchor='e') # se podrían ahorrar lineas con un for
    gamelib.draw_text(contenido[10], 1* ANCHO_VENTANA // 9, 6 * ALTO_VENTANA // 8, fill='black', size=30, anchor='w')
    gamelib.draw_text(contenido[11], 8* ANCHO_VENTANA // 9, 6 * ALTO_VENTANA // 8, fill='black', size=20, anchor='e')
    gamelib.draw_text(contenido[12], 1* ANCHO_VENTANA // 9, 7 * ALTO_VENTANA // 8, fill='black', size=30, anchor='w')
    gamelib.draw_text(contenido[13], 8* ANCHO_VENTANA // 9, 7 * ALTO_VENTANA // 8, fill='black', size=20, anchor='e')
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    menu_memorizado = 'Individual Equipo', pag_pok, pag_equ
    return 'Individual Equipo', pag_pok, pag_equ

def creador_equipo():
    """
    Consulta al usuario por el nombre del equipo que quiere crear, 
    qué pokemones integrarán ese equipo y qué movmientos utilizarán.
    Retorna esta información como tres valores distintos
    """
    pokemones_elegidos = []
    poderes_elegidos = [] 
    nombre_equipo = simpledialog.askstring("nombre de equipo", "Elija un nombre para su equipo").upper()
    desea_seguir_pokemones = "SI"
    desea_seguir_poderes = "SI"
    while len(pokemones_elegidos) <= 5 and desea_seguir_pokemones == "SI":
        elegido = simpledialog.askstring("pokemones", "que pokemon desea elegir?")
        while elegido is not elegido.isdigit():
            elegido = simpledialog.askstring("pokemones", "Ingreso un carater no numerico. Que pokemon desea elegir?")
        pokemones_elegidos.append(int(elegido)) #se agrega el pokemon
        if len(pokemones_elegidos) != 0: #si la lista tiene algun elemento te pregunta si queres borrar
            desea_eliminar_pokemones = simpledialog.askstring("pokemones", "Desea borrar algun pokemon?[SI/NO]").upper()
            while desea_eliminar_pokemones not in["SI", "NO"]:
                desea_eliminar_pokemones = simpledialog.askstring("pokemones", "Ingreso una respuesta incorrecta. Desea borrar algun pokemon?[SI/NO]")
            if desea_eliminar_pokemones == "SI": #pregunta que pokemon queremos eliminar
                pokemon_a_eliminar = simpledialog.askstring("pokemones", "Ingrese el numero de pokemon que desea borrar")
                while not pokemon_a_eliminar is pokemon_a_eliminar.isdigit() and pokemon_a_eliminar not in pokemones_elegidos:
                    pokemon_a_eliminar = simpledialog.askstring("pokemones", "El caracter es invalido o no posee ese pokemon. Ingrese el numero de pokemon que desea borrar")
                pokemones_elegidos.remove(int(pokemon_a_eliminar))
            elif desea_eliminar_pokemones == "NO":
                continue #acá habia dudas
        #te pregunta si queres agregar pokemones
        desea_seguir_pokemones = simpledialog.askstring("pokemones", "desea seguir agregando pokemones?[SI/NO]").upper()
        while desea_seguir_pokemones not in["SI", "NO"]:
            desea_seguir_pokemones = simpledialog.askstring("pokemones", "No eligio una respusta valida. Desea seguir agregando pokemones[SI/NO]").upper()
    for monstruo in pokemones_elegidos:
        info = lector_movimientos(monstruo, 'movimientos.csv')
        lista_movimientos = info[1].split(',')
        #poderes_elegidos.append([])    
    #agregar cómo se escribe al equipos
        while len(pokemones_elegidos) >= 1 or len(poderes_elegidos) <5  and desea_seguir_poderes == "SI":
            elegido_poderes = simpledialog.askstring("poderes", "que pokemon desea elegir?")
            while elegido_poderes is not elegido_poderes.isdigit():
                elegido_poderes = simpledialog.askstring("poderes", "Ingreso un carater no numerico. Que pokemon desea elegir?")
            poderes_elegidos.append(int(elegido_poderes)) #se agrega el poder
            if len(poderes_elegidos) != 0: #si la lista tiene algun elemento te pregunta si queres borrar
                desea_eliminar_poderes = simpledialog.askstring("poderes", "Desea borrar algun poder?[SI/NO]").upper()
                while desea_eliminar_poderes not in["SI", "NO"]:
                    desea_eliminar_poderes = simpledialog.askstring("poderes", "Ingreso una respuesta incorrecta. Desea borrar algun pokemon?[SI/NO]")
                if desea_eliminar_poderes == "SI": #pregunta que poderes queremos eliminar
                    poder_a_eliminar = simpledialog.askstring("poderes", "Ingrese el numero de pokemon que desea borrar")
                    while not poder_a_eliminar is poder_a_eliminar.isdigit() and poder_a_eliminar not in poderes_elegidos:
                        poder_a_eliminar = simpledialog.askstring("poderes", "El caracter es invalido o no posee ese poder. Ingrese el numero de pokemon que desea borrar")
                    pokemones_elegidos.remove(int(poder_a_eliminar))
                elif desea_eliminar_poderes == "NO":
                    continue #acá habia dudas
        #te pregunta si queres agregar poderes
            desea_seguir_poderes = simpledialog.askstring("poderes", "desea seguir agregando poderes?[SI/NO]").upper()
            while desea_seguir_poderes not in["SI", "NO"]:
                desea_seguir_poderes = simpledialog.askstring("poderes", "No eligio una respusta valida. Desea seguir agregando poderes[SI/NO]").upper()

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
    nombre_equipo, pokemones, poderes = creador_equipo()
    #nombre_equipo, pokemones, poderes = 'hola', ['pikachu', 'charmander'], ['relampago', 'trueno']
    nombre_equipo += ';'

    for i in range (len(pokemones)):
        nombre_equipo += pokemones[i] + ';' + poderes[i] + ';'

    with open('equipos.csv', 'a') as archivo:
        archivo.write('\n'+nombre_equipo)

    return menu_equipos(pag_pok, pag_equ)

def navegacion(x, y, juego):
    """
    La función navegación llama a la función correcta dependiendo de 
    donde está parado el usuario en el pokedex y donde hizo click.
    """
    if juego[0] == 'menu principal':
        p_pok = juego [1]
        p_equ = juego [2]

        if x > ANCHO_VENTANA // 2 + ESP_ENTRE_BOTON and x < ANCHO_VENTANA - MRG_HORZ_BOTONES \
        and y > BTN_Y1 and y < BTN_Y2: 
            return menu_equipos(p_pok, p_equ) 
        elif x > MRG_HORZ_BOTONES and x < ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON \
        and y > BTN_Y1 and y < BTN_Y2:
            return menu_pokemones(p_pok, p_equ)

    elif juego[0] == 'menu Pokemones':
        pag_pok = juego[1]
        pag_equ = juego[2]
        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            return menu_principal() #BOTON ROJO

        xcuadro = (x - MRG_CUADRITOS_IZQ) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        ycuadro = (y - MRG_CUADRITOS_SUP) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        nro_pokemon = ycuadro * NRO_COLUMNAS + xcuadro + pag_pok*26

        if (nro_pokemon - pag_pok*26) == 0:
            if pag_pok > 0: return menu_pokemones(pag_pok-1, pag_equ)
            return menu_pokemones(pag_pok, pag_equ)
        if (nro_pokemon - pag_pok*26) == 27:
            return menu_pokemones(pag_pok+1, pag_equ)
        if nro_pokemon > 0:
            return un_pokemon(nro_pokemon, pag_pok, pag_equ)

    elif juego[0] == 'menu Equipos':
        pag_pok = juego[1]
        pag_equ = juego[2]
        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            return menu_principal() #BOTON ROJO
            
        xcuadro = (x - MRG_CUADRITOS_IZQ) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        ycuadro = (y - MRG_CUADRITOS_SUP) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        nro_equipo = ycuadro * NRO_COLUMNAS + xcuadro + pag_equ*26

        if (nro_equipo - pag_equ*26) == 0:
            if pag_pok > 0: return menu_pokemones(pag_pok, pag_equ-1)
            return menu_equipos(pag_pok, pag_equ)
        if (nro_equipo - pag_equ*26) == 27:
            return menu_equipos(pag_pok, pag_equ+1)
        if nro_equipo == 1:
            return menu_creador(pag_pok, pag_equ)
        if nro_equipo > 1:
            return un_equipo(nro_equipo, pag_pok, pag_equ) #equipos

    elif juego[0] == 'Individual Pokemon':
        pag_pok = juego[1]
        pag_equ = juego[2]
        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            return menu_pokemones(pag_pok, pag_equ) #BOTON ROJO

    elif juego[0] == 'Individual Equipo':
        pag_pok = juego[1]
        pag_equ = juego[2]

        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            return menu_equipos(pag_pok, pag_equ) #BOTON ROJO

    return 'menu principal', 0, 0
