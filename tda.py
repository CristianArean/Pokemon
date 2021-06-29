class Cola:
    '''
    Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero
    en ser desencolado.
    '''
    
    def __init__(self):
        '''
        Crea una cola vacía.
        '''
        self.items = []

    def encolar(self, x):
        '''
        Encola el elemento x.
        '''
        self.items.append(x)

    def desencolar(self):
        '''
        Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError.
        '''
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        return self.items.pop(0)

    def ver_frente(self):
        '''
        Devuelve el elemento que está en el frente de la cola.
        Si la cola está vacía, levanta ValueError.
        '''
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        return self.items[0]

    def esta_vacia(self):
        '''
        Devuelve True si la cola esta vacía, False si no.
        '''
        return len(self.items) == 0

class Pila:
    '''
    Representa una pila con operaciones de apilar, desapilar y
    verificar si está vacía.
    '''

    def __init__(self):
        '''
        Crea una pila vacía.
        '''
        self.items = []

    def esta_vacia(self):
        '''
        Devuelve True si la lista está vacía, False si no.
        '''
        return len(self.items) == 0

    def ver_tope(self):
        '''
        Devuelve el elemento que se encuentra en el tope .
        Si la pila está vacía levanta una excepción.
        '''
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]

    def apilar(self, x):
        '''
        Apila un elemento en la pila.
        '''
        self.items.append(x)

    def desapilar(self):
        '''
        Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción.
        '''
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()