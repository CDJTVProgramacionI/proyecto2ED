from dataclasses import dataclass

@dataclass
class ColaLineal:
    """Clase que implementa una cola lineal dinámica
    frente(int): El indice que se agregó primero
    final(int): El indice que se agregó al final
    elementos(list)
    """
    
    #Atributos
    __frente : int
    __final : int
    __elementos : list   
        
    """
    final=-1, frente=0, elementos=[]
    encolar(0)
        elementos=[0]
        final = final + 1 = -1 + 1 = 0
            
    encolar(9)
        elementos=[0, 9]
        final = final + 1 = 0 + 1 = 1
    
    desencolar()
        elementos=[x, 9]
        frente = frente + 1 = 0 + 1 = 1
        
    encolar(5)
        elementos=[x, 9, 5]
        final = final + 1 = 1 + 1 = 2
        
    desencolar()
        elementos=[x, x, 5]
        frente = frente + 1 = 1 + 1 = 2
        
    desencolar()
        como frente == final -> v 
        elementos=[]
        frente=0
        final=-1
    """
    
    #Constructor
    def __init__(self):
        self.__frente = 0
        self.__final = -1
        self.__elementos = []
        
    #Método 1 (encolar)
    def encolar(self, elemento : any):
        self.__elementos.append(elemento) #Añade elemento al final de la cola
        self.__final += 1
        
    #Método 2 (desencolar)
    def desencolar(self) -> any:
        """
            [0, 5, 9, 8]
            int var = 0
            [5, 5, 9, 8]
            [5, 9, 9, 8]
            [5, 9, 8, 8]
            [5, 9, 8] malloc aquí
        """  
        valor_ret = None
        if self.esta_vacio():
            valor_ret = None
            print("Cola vacía")
        elif self.__frente == self.__final: #¿Solo queda un elemento?
            valor_ret = self.__elementos[self.__frente]
            self.__elementos=[]
            self.__final=-1
            self.__frente=0
        else:
            valor_ret = self.__elementos[self.__frente]
            self.__elementos[self.__frente] = 'x'
            self.__frente += 1
            
        return valor_ret
    
    def imprimir_cola(self):
        """
            [x, x, 8, 9]
            
            prioridad = 1
            
            for:
            elemento = 'x'
            'x' == 'x'? v
            sig it
            elemento = 'x'
            'x' == 'x'? v
            sig it
            elemento = 8
            8 == 'x'? f
            imprime 8 con prioridad 1
            se le suma a prioridad = 2
        """
        
        if self.esta_vacio():
            print("Cola vacía")
            return
        
        prioridad = 1
        for elemento in self.__elementos:
            if elemento != 'x':
                print(elemento, f", Prioridad: {prioridad}")
                prioridad += 1
        
        print() #Imprime salto de línea al final de todo
    
    #Método 3 (está vacio)
    def esta_vacio(self) -> bool:
        return self.__final < self.__frente     