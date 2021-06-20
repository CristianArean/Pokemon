#hay un estado inicial, se muestra la pantalla d
import gamelib
#from classpokemon import *
ANCHO_VENTANA = 900
ALTO_VENTANA = 600
VACIO = 0

TITLE_Y = 70 #######sacar de variables globales y mover a las funciones correspondientes? 
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
    return 'menu principal'

def cuadritos_pokemones(): 
    nro_pok_nombre = {0: VACIO, 1:'pikachu', 2:'bulbasur', 3:'charmander', 4:'hello', 5:'pikachu', 6:'bulbasur', 7:'charmander', 8:'hello', 9:'pikachu', 10:'bulbasur', 11:'charmander', 12:'hello', 13:'pikachu', 14:'bulbasur', 15:'charmander', 16:'hello', 17:'pikachu', 18:'bulbasur', 19:'charmander', 20:'hello', 21:'pikachu', 22:'bulbasur', 23:'charmander', 24:'hello', 25:'pikachu', 26:'bulbasur', 27:'charmander', 28:'hello', 29:'pikachu', 30:'bulbasur', 31:'pikachu', 32:'bulbasur', 33:'charmander', 34:'hello', 35:'pikachu', 36:'bulbasur', 37:'charmander', 38:'hello', 39:'pikachu', 40:'bulbasur', 41:'charmander', 42:'hello', }
    nro_pag_pok = 0
    for i in range (4): #arreglar numeros mágicos
        for j in range (7): #puede que estos cuadros sean remplazados por una imagen de photoshop
            gamelib.draw_rectangle(MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO)
            if i == VACIO and j == VACIO:
                continue
            else: #hay que administrar el keyerror cuando no existe un pokemon con esa llave
                gamelib.draw_text(nro_pok_nombre[nro_pag_pok*(4*7) + i*7 + j], MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=8, anchor='nw')
    gamelib.draw_text('<-', MRG_CUADRITOS_IZQ, MRG_CUADRITOS_SUP, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (7) + XY_CUADRITO * 7, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (4) + XY_CUADRITO * 4, fill='black', size=30, anchor='se')

def cuadritos_equipos(): ################## cuadritos equipos y cuadritos pokemones son practicamente identicos. Ahorrar lineas de codigo (por ejemplo con el metodo bibliotecas diseñado por Cris)
    nro_equ_nombre = {0: VACIO, 1:'Rocket', 2:'Empire', 3:'charmander', 4:'hello', 5:'Rocket', 6:'Empire', 7:'charmander', 8:'hello', 9:'Rocket', 10:'Empire', 11:'charmander', 12:'hello', 13:'Rocket', 14:'Empire', 15:'charmander', 16:'hello', 17:'Rocket', 18:'Empire', 19:'charmander', 20:'hello', 21:'Rocket', 22:'Empire', 23:'charmander', 24:'hello', 25:'Rocket', 26:'Empire', 27:'charmander', 28:'hello', 29:'Rocket', 30:'Empire', 31:'Rocket', 32:'Empire', 33:'charmander', 34:'hello', 35:'Rocket', 36:'Empire', 37:'charmander', 38:'hello', 39:'Rocket', 40:'Empire', 41:'charmander', 42:'hello', }
    nro_pag_equ = 0
    for i in range (4): #arreglar numeros mágicos
        for j in range (7):
            gamelib.draw_rectangle(MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j + XY_CUADRITO, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i + XY_CUADRITO)
            if i == VACIO and j == VACIO:
                continue
            else: #hay que administrar el keyerror cuando no existe un pokemon con esa llave #arreglar bug superposición flecha proxima página y ultimo pokemon
                gamelib.draw_text(nro_equ_nombre[nro_pag_equ*(4*7) + i*7 + j], MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (j+1) + XY_CUADRITO * j, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (i+1) + XY_CUADRITO * i, fill='black', size=8, anchor='nw')
    gamelib.draw_text('<-', MRG_CUADRITOS_IZQ, MRG_CUADRITOS_SUP, fill='black', size=30, anchor='nw')
    gamelib.draw_text('->', MRG_CUADRITOS_IZQ + ESP_ENTRE_CUADROS * (7) + XY_CUADRITO * 7, MRG_CUADRITOS_SUP + ESP_ENTRE_CUADROS * (4) + XY_CUADRITO * 4, fill='black', size=30, anchor='se')

def un_pokemon(nro_pokemon):
    nombre = 'Pikachu' #Acá implementación del nombre del pokemon
    tipo = 'Agua' #Acá implementación del tipo del pokemon
    ataque = '40' #Acá implementación del ataque del pokemon
    defensa = '20' #Acá implementación del defensa del pokemon
    sparring = '69' #Acá implementación del saparring del pokemon 
    velocidad = '50' #Acá implementación del velocidad del pokemon
    spee = '13' #Acá implementación del spee del pokemon    (¿qué es spee?)
    imagen = 'imgs/1.gif'
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text(nombre   , ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    gamelib.draw_text(tipo     , 4* ANCHO_VENTANA // 5, 2 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(ataque   , 4* ANCHO_VENTANA // 5, 3 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(defensa  , 4* ANCHO_VENTANA // 5, 4 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(sparring , 4* ANCHO_VENTANA // 5, 5 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(velocidad, 4* ANCHO_VENTANA // 5, 6 * ALTO_VENTANA // 7, fill='black', size=30,)
    gamelib.draw_text(spee     , 4* ANCHO_VENTANA // 5, 7 * ALTO_VENTANA // 7, fill='black', size=30,) # se podrían ahorrar lineas con un for
    gamelib.draw_image(imagen, VACIO, ALTO_VENTANA // 4)
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
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
    gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
    gamelib.draw_end()
    imagen = 'imgs/1.gif'
    return 'Individual Equipo'

def navegacion(x, y, juego): #implementado con diccionarios
    selector = {}       
    selector['pokequipos'] = "Pokemones"
    selector['equipos'] = "Equipos"

    def menu_pokemones():
        print ('menu ' + selector['pokequipos'])
        gamelib.draw_begin()
        gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
        gamelib.draw_text(selector['pokequipos'], ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
        cuadritos_pokemones()
        gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
        gamelib.draw_end()
        return 'menu ' + selector['pokequipos']

    def menu_equipos(): #para mi pongamos las funciones menu equipos y menu pokemones fuera de la funcion navegación. Que te parece? Así queda más limpia
        print ('menu ' + selector['equipos'])
        gamelib.draw_begin()
        gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
        gamelib.draw_text(selector['equipos'], ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
        cuadritos_equipos()
        gamelib.draw_rectangle(BOTON_RETROCESO, BOTON_RETROCESO, BOTON_RETROCESO*2, BOTON_RETROCESO*2, fill = 'red')
        gamelib.draw_end()
        return 'menu ' + selector['equipos']
    """
    if juego == 'menu principal' and x > MRG_HORZ_BOTONES and x < ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON \
       and y > BTN_Y1 and y < BTN_Y2:
        return menu_pokemones()
    """     
    if juego == 'menu principal':
        if x > ANCHO_VENTANA // 2 + ESP_ENTRE_BOTON and x < ANCHO_VENTANA - MRG_HORZ_BOTONES \
        and y > BTN_Y1 and y < BTN_Y2: #podriamos poner todos los juego == menu principal en un mismo if
            selector['pokemones'] = 'equipos'
            return menu_equipos()
        elif x > MRG_HORZ_BOTONES and x < ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON \
        and y > BTN_Y1 and y < BTN_Y2:
            return menu_pokemones()

    elif juego == 'menu Pokemones':
        if x > BOTON_RETROCESO and x < BOTON_RETROCESO*2 \
        and y > BOTON_RETROCESO and y < BOTON_RETROCESO*2:
            return menu_principal()
        xcuadro = (x - MRG_CUADRITOS_IZQ) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        ycuadro = (y - MRG_CUADRITOS_SUP) // (XY_CUADRITO + ESP_ENTRE_CUADROS)
        #print ('cuadro: ', xcuadro, ycuadro)
        nro_pokemon = 1 #nro_pokemon = ycuadro * 7 + xcuadro + nro_pag_pok ####Implementar, elige el pokemon que el usuario clickeó
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
            return menu_equipos()

    return juego












'''
selector = {}       
selector['pokequipos'] = "pokemones"
 
       
def menu_pokemones():
    print ('Menu pokemones')
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text('POKEMONES', ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    gamelib.draw_end()
    return 'menu pokemones'
    
def menu_equipos():
    print ('Menu equipos')
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text('EQUIPOS', ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    gamelib.draw_end()
    return 'menu pokemones'
'''
