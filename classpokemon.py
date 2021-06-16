class pokemon:
    def __init__(self, nombre = '', tipos = '', hp = 0, atk = 0, def = 0, spa = 0, spd = 0, spe = 0):
        self.nombre = nombre
        self.tipos = tipos
        self.hp = hp
        self.atk = atk
        self.defe = def
        self.spa = spa
        self.spd = spd
        self.spe = spe
    

    def mostrar_atributos(self):
        return (f"pokemon de {self.tipos}\n salud: {self.hp}\n Ataque: {self.atk}\n Defensa: {self.defe}\n Sparring: {self.spa}\n Velocidad: {self.spd}\n Spe: {self.spe}\n")

    def mostrar_nombre(self):
        return f"{self.nombre}\n"
    
    def comparacion(self, otro):

        #comparacion salud
        if self.hp > otro.hp:
            return f"{self.nombre} tiene mayor salud\n"

        elif self.hp < otro.hp:
            return f"{otro.nombre} tiene mayor salud\n"
        
        elif self.hp == otro.hp:
            return f"tienen la misma salud\n"
        
        #comparacion ataque
        if self.atk > otro.atk:
            return f"{self.nombre} tiene mayor ataque\n"

        elif self.atk < otro.atk:
            return f"{otro.nombre} tiene mayor ataque\n"
        
        elif self.atk == otro.atk:
            return f"tienen el misma ataque\n"

        #comparacion defensa
        if self.defe > otro.defe:
            return f"{self.nombre} tiene mayor defensa\n"

        elif self.defe < otro.defe:
            return f"{otro.nombre} tiene mayor defensa\n"
        
        elif self.defe == otro.defe:
            return f"tienen la misma defensa\n"  

        #comparacion de sparring
        if self.spa > otro.spa:
            return f"{self.nombre} tiene mayor sparring\n"

        elif self.spa < otro.spa:
            return f"{otro.nombre} tiene mayor sparring\n"
        
        elif self.spa == otro.spa:
            return f"tienen el mismo sparring\n"

        #comparacion velocidad
        if self.spd > otro.spd:
            return f"{self.nombre} tiene mayor velocidad\n"

        elif self.spd < otro.spd:
            return f"{otro.nombre} tiene mayor velocidad\n"
        
        elif self.spd == otro.spd:
            return f"tienen la misma velocidad\n"    

        #comparacion spe
        if self.spe > otro.spe:
            return f"{self.nombre} tiene mayor spe\n"

        elif self.spe < otro.spe:
            return f"{otro.nombre} tiene mayor spe\n"
        
        elif self.spe == otro.spe:
            return f"tienen la misma spe\n"