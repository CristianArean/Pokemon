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

#puedo borrar mostrar_pokedex? ################################
def mostrar_pokedex():
    gamelib.draw_rectangle(50,50,900,650, fill='red')
    gamelib.draw_oval(80, 70, 130, 120, outline='black', fill='#15E8E8')
    gamelib.draw_oval(150, 70, 170, 90, outline='black', fill='red')
    gamelib.draw_oval(180, 70, 200, 90, outline='black', fill='green')
    gamelib.draw_oval(210, 70, 230, 90, outline='black', fill='yellow')
    gamelib.draw_rectangle(80,150,870,550, fill='grey')
    gamelib.draw_rectangle(90,160,860,540, fill='white')
    gamelib.draw_oval(80, 560, 120, 600, fill='blue')
    gamelib.draw_oval(150, 560, 180, 590, fill='green', outline='green')
    gamelib.draw_rectangle(165, 560, 235, 590, fill='green', outline='green')
    gamelib.draw_oval(220, 560, 250, 590, fill='green', outline='green')
    gamelib.draw_oval(290, 560, 320, 590, fill='yellow', outline='yellow')
    gamelib.draw_rectangle(305, 560, 375, 590, fill='yellow', outline='yellow')
    gamelib.draw_oval(360, 560, 390, 590, fill='yellow', outline='yellow')

def crear_juego():
    return 1 #no creo que valga la pena una funcion entera crear juego para esto #########################

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
    
def pokemones_o_equipos(x, y):
    if x > MRG_HORZ_BOTONES and x < ANCHO_VENTANA // 2 -  ESP_ENTRE_BOTON \
       and y > BTN_Y1 and y < BTN_Y2:
        menu_pokemones()
        
    elif x > ANCHO_VENTANA // 2 + ESP_ENTRE_BOTON and x < ANCHO_VENTANA - MRG_HORZ_BOTONES \
       and y > BTN_Y1 and y < BTN_Y2:
        menu_equipos()
        
def menu_pokemones():
    print ('Menu pokemones')
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text('POKEMONES', ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    gamelib.draw_end()
    return 2
    
def menu_equipos():
    print ('Menu equipos')
    gamelib.draw_begin()
    gamelib.draw_rectangle(VACIO, VACIO, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text('EQUIPOS', ANCHO_VENTANA // 2, TITLE_Y, fill='black', size=30, anchor='s')
    gamelib.draw_end()
    return 3
