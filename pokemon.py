import gamelib
import classpokemon
from tda import Pila 
from tda import Cola
#from classpokemon import *
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

nro_pag_pok = 0
nro_pag_equ = 0 #error de poner esto como variables globales?

def crear_juego():
    menu_memorizado = 'menu principal'
    with open('equipos.csv', 'w'):
        pass
    return 'menu principal'

def juego_actualizar(juego):
    pass

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
    return 'menu principal'

def lector_nombres(nros, nombre_archivo): #cambiar el nombre por "lector"
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
                #print ('hola')
                lineas_solicitadas.desencolar()
                contador -= 1
    while not lineas_solicitadas.esta_vacia():
        lista_atributos = (lineas_solicitadas.desencolar()).split(';')
        rta[lista_atributos[0]] = lista_atributos
    return rta

def cuadritos_pokemones(nro_pag_pok): 
    nro_pok_nombre = lector_nombres([nro_pag_pok*4*7 +1, nro_pag_pok*4*7 +1+28], 'pokemons.csv')
    #print (nro_pok_nombre)
    for i in range (4): #arreglar numeros mágicos
        for j in range (7): #puede que estos cuadros sean remplazados por una imagen de photoshop
            gamelib.draw_rectangle(MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO)
            if i == VACIO and j == VACIO:
                continue
            else: #hay que administrar el keyerror cuando no existe un pokemon con esa llave
                elegido_en_ciclo = str(nro_pag_pok*(4*7) + i*7 + j)
                gamelib.draw_text(nro_pok_nombre[elegido_en_ciclo][2], MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=8, anchor='nw')
    gamelib.draw_text('<-', MRG_CUADRITOS_IZQ, MRG_CUADRITOS_SUP, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (7) + XY_CUADRITO * 7, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (4) + XY_CUADRITO * 4, fill='black', size=30, anchor='se')

def cuadritos_equipos(nro_pag_equ): 
    nro_equ_nombre = lector_nombres([nro_pag_equ*4*7 +1, nro_pag_equ*4*7 +1+28], 'pokemons.csv') 
    for i in range (4): #arreglar numeros mágicos
        for j in range (7):
            gamelib.draw_rectangle(MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO)
            if i == VACIO and j == VACIO:
                continue
            else: #hay que administrar el keyerror cuando no existe un pokemon con esa llave #arreglar bug superposición flecha proxima página y ultimo pokemon
                elegido_en_ciclo = str(nro_pag_equ*(4*7) + i*7 + j)
                gamelib.draw_text(nro_equ_nombre[elegido_en_ciclo][2], MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=8, anchor='nw')
    gamelib.draw_text('<-', MRG_CUADRITOS_IZQ, MRG_CUADRITOS_SUP, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (7) + XY_CUADRITO * 7, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (4) + XY_CUADRITO * 4, fill='black', size=30, anchor='se')

def un_pokemon(nro_pokemon):
    info = lector_nombres([nro_pokemon, nro_pokemon], 'pokemons.csv')
    print(info)
    contenido = info[str(nro_pokemon)]
    print (contenido)
    nombre = contenido[2]
    tipo = contenido[3]
    salud = contenido[4]
    ataque = contenido[5]
    defensa = contenido[6]
    specialA = contenido[7]
    specialD = contenido[8]
    velocidad = contenido[9]
    imagen = contenido[1]
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text(nombre   , ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    gamelib.draw_text(tipo     , 4* ANCHO_VENTANA // 5, 1 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(salud    , 4* ANCHO_VENTANA // 5, 2 * ALTO_VENTANA // 8, fill='black', size=30,) # ajustar alturas puse // 6 evitar superposiciosion
    gamelib.draw_text(ataque   , 4* ANCHO_VENTANA // 5, 3 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(defensa  , 4* ANCHO_VENTANA // 5, 4 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(specialA , 4* ANCHO_VENTANA // 5, 5 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(specialD , 4* ANCHO_VENTANA // 5, 6 * ALTO_VENTANA // 8, fill='black', size=30,)
    gamelib.draw_text(velocidad, 4* ANCHO_VENTANA // 5, 7 * ALTO_VENTANA // 8, fill='black', size=30,) # se podrían ahorrar lineas con un for
    gamelib.draw_image(imagen, VACIO, ALTO_VENTANA // 4)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    menu_memorizado = 'Individual Pokemon'
    return 'Individual Pokemon'

def un_equipo(nro_equipo):
    """
    nombre = 'Omega' #Acá implementación del nombre del pokemon
    integrantes = {1:[lista de ataques], 2:[lista de ataques], 3:[lista de ataques]}
    @ = nombre, lista de ataques
    gamelib.draw_text(@1, 4* ANCHO_VENTANA // 5, 2 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(@2   , 4* ANCHO_VENTANA // 5, 3 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(@3, 4* ANCHO_VENTANA // 5, 4 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(@4, 4* ANCHO_VENTANA // 5, 5 * ALTO_VENTANA // 7, fill='black', size=30,) #acá iría el nombre de cada pokemon integrante del equipo y sus ataques elegidos. Sacar info del csv que creamos nosotros
    gamelib.draw_text(@5, 4* ANCHO_VENTANA // 5, 6 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(@6, 4* ANCHO_VENTANA // 5, 7 * ALTO_VENTANA // 7, fill='black', size=30,)
    """
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    imagen = 'imgs/1.gif'
    menu_memorizado = 'Individual Equipo'
    return 'Individual Equipo'

def navegacion(x, y, juego): #implementado con diccionarios
    selector = {}       
    selector['pokequipos'] = "Pokemones"

    def menu_pokemones(): #lo que hice fué, como las funciones eran identicas pero cambiaba una palabra, que vaya cambiando solo el string, en vez de otra funcion solo por un string
        print ('menu ' + selector['pokequipos'])    
        gamelib.draw_begin()
        gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
        gamelib.draw_text(selector['pokequipos'], ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
        if selector['pokequipos'] == "Pokemones":
            cuadritos_pokemones(0)
        elif selector['pokequipos'] == "Equipos":
            cuadritos_equipos(0)
        gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
        gamelib.draw_end()
        menu_memorizado = 'menu ' + selector['pokequipos']
        return 'menu ' + selector['pokequipos']
 
    """
    if juego == 'menu principal' and x > MRG_HORZ_BOTONES and x < ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON \
       and y > BTN_Y1 and y < BTN_Y2:
        return menu_pokemones()
    """     
    if juego == 'menu principal':
        if x > ANCHO_VENTANA // 2 + ESP_ENTRE_BOTON and x < ANCHO_VENTANA - MRG_HORZ_BOTONES \
        and y > BTN_Y1 and y < BTN_Y2: #podriamos poner todos los juego == menu principal en un mismo if
            selector['pokequipos'] = 'Equipos'
            return menu_pokemones() 
        elif x > MRG_HORZ_BOTONES and x < ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON \
        and y > BTN_Y1 and y < BTN_Y2:
            selector['pokequipos'] = "Pokemones"
            return menu_pokemones()

    elif juego == 'menu Pokemones':
        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            return menu_principal()
        xcuadro = (x - MRG_CUADRITOS_IZQ) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        ycuadro = (y - MRG_CUADRITOS_SUP) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        print ('cuadro: ', xcuadro, ycuadro)
        nro_pokemon = ycuadro * 7 + xcuadro + nro_pag_pok ####Implementar, elige el pokemon que el usuario clickeó
        return un_pokemon(nro_pokemon)

    elif juego == 'menu Equipos':
        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            return menu_principal()
        xcuadro = (x - MRG_CUADRITOS_IZQ) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        ycuadro = (y - MRG_CUADRITOS_SUP) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        #print ('cuadro: ', xcuadro, ycuadro)
        nro_equipo = 1 #nro_pokemon = ycuadro * 7 + xcuadro + nro_pag_pok ####Implementar, elige el pokemon que el usuario clickeó
        return un_equipo(nro_equipo)

    elif juego == 'Individual Pokemon':
        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            return menu_pokemones()

    elif juego == 'Individual Equipo':
        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            selector['pokequipos'] = "Equipos"
            return menu_pokemones()

    return 'menu principal' #####Esto arregla en parte el bug donde los clicks dejan de hacer efecto. Sucede que
    # el estado de juego se vuelve none (en la linea 27 de main. Arreglar con menu_memorizado) MIENTRAS TANTO CADA VEZ QUE FALLA SIMPLEMENTE NOS LLEVA AL MENU PRINCIPAL, así no se rompe.
