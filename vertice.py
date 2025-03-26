class Vertice:
    dato : any
    __estado : int #0: en espera, 1: listo, 2: procesado
    __vecinos : list
    
    def __init__(self, dato):
        self.dato = dato
        self.__estado = 0
        self.__vecinos = []
        
    def setVecinos(self, vecinos):
        self.__vecinos = vecinos
        
    def getVecinos(self):
        return self.__vecinos
    
    def setEstado(self, estado):
        self.__estado = estado
        
    def estaEnEspera(self):
        return self.__estado == 0
    
    def __str__(self):
        return f"Vertice {self.dato}"