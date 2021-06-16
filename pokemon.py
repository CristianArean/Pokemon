#hay un estado inicial, se muestra la pantalla d
import gamelib
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



def crear_juego():
    return 'menu principal' #no creo que valga la pena una funcion entera crear juego para esto #########################

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
    
def pokemones_o_equipos(x, y, juego):
    selector = {}       
    selector['pokequipos'] = "pokemones"
    def menu_pokemones():
        print ('Menu ' + selector['pokequipos'])
        gamelib.draw_begin()
        gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
        gamelib.draw_text(selector['pokequipos'], ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
        gamelib.draw_end()
        return 'menu ' + selector['pokequipos']

    if juego == 'menu_principal' and x > MRG_HORZ_BOTONES and x < ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON \
       and y > BTN_Y1 and y < BTN_Y2:
        menu_pokemones()
        
    elif juego == 'menu_principal' and x > ANCHO_VENTANA // 2 + ESP_ENTRE_BOTON and x < ANCHO_VENTANA - MRG_HORZ_BOTONES \
       and y > BTN_Y1 and y < BTN_Y2:
        selector['pokemones'] = 'equipos'
        menu_pokemones()

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