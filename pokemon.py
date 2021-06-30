import gamelib
from tda import Pila 
from tda import Cola
from tkinter import simpledialog
ANCHO_VENTANA = 900
ALTO_VENTANA = 600
VACIO = 0

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

def crear_juego():
    menu_memorizado = 'menu principal'
    with open('equipos.csv', 'w') as archivo:
        for _ in range (1):
            archivo.writelines('equipo_nombre;integrante1;movimientos1;integrante2;movimientos2;integrante3;movimientos3;integrante4;movimientos4;integrante5;movimientos5;integrante6;movimientos6')
    return 'menu principal', 0, 0

def lector(nros, nombre_archivo): 
    """
    Entrega toda la info de las lineas que solicites (tomando la primera linea como cero, para ignorarla). Retorna un diccionario
    Puede usarse para el archivo de pokemones y de equipos, ya sea para menús o para mostrar la info de un pokemon o equipo en particular.
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
            #print (contador, linea)
            if contador == (maximo - minimo +1):
                lineas_solicitadas.desencolar()
                contador -= 1
    while not lineas_solicitadas.esta_vacia():
        lista_atributos = (lineas_solicitadas.desencolar()).split(';')
        rta[lista_atributos[0]] = lista_atributos
    return rta

def lector_movimientos(nro, nombre_archivo):
    contador = 1
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            leido = linea.readline()
            contador += 1
            if contador == nro:
                return leido.split(';')

def menu_principal(): 
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text('POKEDEX', ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    gamelib.draw_rectangle(MRG_HORZ_BOTONES, BTN_Y1, ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON, BTN_Y2) #Rectangulo de botón izq.
    gamelib.draw_rectangle(ANCHO_VENTANA // 2 + ESP_ENTRE_BOTON, BTN_Y1, ANCHO_VENTANA - MRG_HORZ_BOTONES, BTN_Y2) #Rectangulo de botón der.
    gamelib.draw_text('POKEMONES', MRG_HORZ_BOTONES, ALTO_VENTANA // 2 - ALTO_BOTONES, fill='black', size=25, anchor='nw') #Texto de botón izq.
    gamelib.draw_text('EQUIPOS', ANCHO_VENTANA // 2 +  ESP_ENTRE_BOTON, ALTO_VENTANA // 2 - ALTO_BOTONES, fill='black', size=25, anchor='nw') #Texto de botón der.
    gamelib.draw_end()
    menu_memorizado = 'menu principal'
    return 'menu principal', 0, 0

def menu_pokemones(pag_pok, pag_equ): 
    #print ('menu Pokemones')    
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text('Pokemones', ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    cuadritos_pokemones(pag_pok, pag_equ)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    menu_memorizado = 'menu Pokemones', pag_pok, pag_equ
    return 'menu Pokemones', pag_pok, pag_equ

def menu_equipos(pag_pok, pag_equ): 
    #print ('menu Equipos')    
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text('Equipos', ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    cuadritos_equipos(pag_pok, pag_equ)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    menu_memorizado = 'menu Equipos', 0, 0
    return 'menu Equipos', 0, 0

def cuadritos_pokemones(pag_pok, pag_equ): 
    nro_pok_nombre = lector([pag_pok*4*7 -10, pag_pok*4*7 +28], 'pokemons.csv') #ajustar numeros mágicos
    for i in range (4): #arreglar numeros mágicos
        for j in range (7): 
            gamelib.draw_rectangle(MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO)
            if i == VACIO and j == VACIO:
                continue
            elif i == 3 and j == 6:
                continue
            else: #hay que administrar el keyerror cuando no existe un pokemon con esa llave
                elegido_en_ciclo = str(pag_pok*(4*7) + i*7 + j - 2*pag_pok)
                #print(i, j, elegido_en_ciclo)
                gamelib.draw_text(nro_pok_nombre[elegido_en_ciclo][2], MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=8, anchor='nw')
    gamelib.draw_text('<-', MRG_CUADRITOS_IZQ, MRG_CUADRITOS_SUP, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (7) + XY_CUADRITO * 7, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (4) + XY_CUADRITO * 4, fill='black', size=30, anchor='se')

def cuadritos_equipos(pag_pok, pag_equ): 
    nro_equ_nombre = lector([pag_equ*4*7 +1, pag_equ*4*7 +1+28], 'pokemons.csv') 
    for i in range (4): #arreglar numeros mágicos
        for j in range (7):
            gamelib.draw_rectangle(MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO)
            if i == VACIO and j == VACIO:
                continue
            else: #hay que administrar el keyerror cuando no existe un pokemon con esa llave 
                elegido_en_ciclo = str(pag_equ*(4*7) + i*7 + j + 2*pag_equ)
                gamelib.draw_text(nro_equ_nombre[elegido_en_ciclo][2], MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=8, anchor='nw')
    gamelib.draw_text('<-', MRG_CUADRITOS_IZQ, MRG_CUADRITOS_SUP, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (7) + XY_CUADRITO * 7, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (4) + XY_CUADRITO * 4, fill='black', size=30, anchor='se')

def un_pokemon(nro_pokemon, pag_pok, pag_equ):
    info = lector([nro_pokemon, nro_pokemon], 'pokemons.csv')
    contenido = info[str(nro_pokemon)]
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text((contenido[2]+', '+contenido[0]), ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    gamelib.draw_text(contenido[3], 4* ANCHO_VENTANA // 5, 1 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(contenido[4], 4* ANCHO_VENTANA // 5, 2 * ALTO_VENTANA // 8, fill='black', size=30,) # ajustar alturas puse // 6 evitar superposiciosion
    gamelib.draw_text(contenido[5], 4* ANCHO_VENTANA // 5, 3 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(contenido[6], 4* ANCHO_VENTANA // 5, 4 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(contenido[7], 4* ANCHO_VENTANA // 5, 5 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(contenido[8], 4* ANCHO_VENTANA // 5, 6 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(contenido[9], 4* ANCHO_VENTANA // 5, 7 * ALTO_VENTANA // 8, fill='black', size=30,) # se podrían ahorrar lineas con un for
    gamelib.draw_image(contenido[1], VACIO, ALTO_VENTANA // 4)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    menu_memorizado = 'Individual Pokemon', pag_pok, pag_equ
    return 'Individual Pokemon', pag_pok, pag_equ

def un_equipo(nro_equipo, pag_pok, pag_equ):
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    imagen = 'imgs/1.gif'
    menu_memorizado = 'Individual Equipo', pag_pok, pag_equ
    return 'Individual Equipo', pag_pok, pag_equ

def creador_equipo():
    pokemones_elegidos = []
    nombre_equipo = simpledialog.askstring("nombre de equipo", "Elija un nombre para su equipo").upper()
    desea_seguir_pokemones = "SI"
    while len(pokemones_elegidos) >= 5 and desea_seguir_pokemones == "SI":
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
    #agregar cómo se escribe al equipos

def menu_creador(pag_pok, pag_equ):
    #dibujar
    #llamar a creador_equipo()
    pass

def navegacion(x, y, juego):

    #print (juego)
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
        #print ('cuadro: ', xcuadro, ycuadro)
        nro_pokemon = ycuadro * 7 + xcuadro + pag_pok*26
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
        #print ('cuadro: ', xcuadro, ycuadro)
        nro_equipo = ycuadro * 7 + xcuadro + pag_equ*26
        if (nro_equipo - pag_equ*26) == 0:
            if pag_pok > 0: return menu_pokemones(pag_pok, pag_equ-1)
            return menu_pokemones(pag_pok, pag_equ)
        if (nro_equipo - pag_equ*26) == 27:
            return menu_pokemones(pag_pok, pag_equ+1)
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
            return menu_pokemones(pag_pok, pag_equ) #BOTON ROJO

    return 'menu principal', 0, 0 #####Esto arregla en parte el bug donde los clicks dejan de hacer efecto. Sucede que
    # el estado de juego se vuelve none (en la linea 27 de main. Arreglar con menu_memorizado) MIENTRAS TANTO CADA VEZ QUE FALLA SIMPLEMENTE NOS LLEVA AL MENU
