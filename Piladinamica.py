from dataclasses import dataclass

#Definimos clase para la estructura
@dataclass
class pila: 

#ATRIBUTOS 
    __tope: int
    __elementos: list
#Constructor
    def __init__(self): 
        self.__tope=-1
        self.__elementos=[]

#PUSH
    def push(self,elemento:any): 
        self.__elementos.append(elemento)
        self.__tope+=1

#POP    saca el ultimo valor el apuntador se disminuye en uno
    def pop(self) -> any: 
        valor_ret= None 
        if self.estavacio(): 
            valor_ret=None
            print("Error: Pila vacia ")
        else:
            var=self.__elementos.pop()
            self.__tope -=1
            return var        
        
#Imprimir la pila 
    def imprimir_pila(self):
        print("Pila: [", end="")
        for elemento in self.__elementos:
            print(elemento, end=", ")
        print("]")

#Definir ESTAVACIO
    def estavacio(self) -> bool : 
        return self.__tope == -1 