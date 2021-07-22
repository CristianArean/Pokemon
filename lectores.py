from tda import Cola

def lector_en_rango(nros, nombre_archivo): 
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
        for _ in range (maximo + 1):
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

def lector_por_numero(nro, nombre_archivo):
    """
    Lee el archivo ingresado por parametro, ignora la primera linea y retorna un diccionario con el numero de linea como llave.
    El diccionario contiene toda la información de la linea solicitada como lista.
    Retorna la información de solo un pokemon.
    """
    contador = -1
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            leido = linea#.readline()
            contador += 1
            if contador == nro:
                return leido[:-1].split(';')
            
def cuantas_lineas_archivo(archivo):
    """
    Lee cuantas lineas tiene un archivo, ignorando la primera de los encabezados.
    """
    total_de_lineas = -1  # IGNORA LA LINEA DE ENCABEZADOS
    
    with open (archivo) as archivo:
        for linea in archivo:
            total_de_lineas += 1
            
    return total_de_lineas
