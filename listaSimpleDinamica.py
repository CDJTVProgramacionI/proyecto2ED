from dataclasses import dataclass

class Node:
    data : any
    next: 'Node'
    
    def __init__(self, dato: any, siguiente: 'Node'):
        self.data = dato
        self.next = siguiente

@dataclass      
class LinkedList:
    __head : Node
    __len : int
    
    @property
    def len(self):
        return self.__len
    
    def __init__(self):
        self.__head = None
        self.__len = 0
        
    def insertAtBegin(self, dato: any):
        self.__head = Node(dato, self.__head)
        self.__len += 1
        
    def insertAtEnd(self, dato: any):
        if self.__head is None:
            self.__head = Node(dato, None)
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
                
            current.next = Node(dato,  None)
            
        self.__len += 1
        
    def getAt(self, index : int):
        if index < 0 or index >= self.__len:
            raise IndexError("Índice fuera de rango")
        
        current = self.__head
        for i in range(index):
            current = current.next
            
        return current.data
    
    def insertAt(self, data : any, index : int):
        if index < 0 or index > self.__len:
            raise IndexError("Índice fuera de rango")
        
        if index == 0:
            self.insertAtBegin(data)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
                
            current.next = Node(data, current.next)
            self.__len += 1
            
    def deleteAtBegin(self) -> any:
        if self.__head is None:
            raise IndexError("Lista vacía")
        
        val = self.__head.data
        self.__head = self.__head.next
        self.__len -= 1
        return val
        
    def deleteAtEnd(self) -> any:
        if self.__head is None:
            raise IndexError("Lista vacía")
        
        val = None
        if self.__head.next is None:
            val = self.__head.data
        else:
            current = self.__head
            while current.next.next is not None:
                current = current.next
              
            val = current.next.data
            current.next = None
            
        self.__len -= 1
        return val
        
    def deleteAt(self, index : int) -> any:
        if index < 0 or index >= self.__len:
            raise IndexError("Índice fuera de rango")
        
        if index == 0:
            return self.deleteAtBegin()
        current = self.__head
        for i in range(1, index):
            current = current.next
                
        val = current.next.data
        current.next = current.next.next
        self.__len -= 1
        return val    
            
    def search(self, data : any) -> int:
        current = self.__head
        i = 0
        while current is not None:
            if current.data == data:
                return i
            current = current.next
            i += 1
            
        return -1
    
    def print(self):
        current = self.__head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
            
        print()
    
if __name__ == "__main__":
    lista = LinkedList()
    lista.insertAtEnd(5)
    lista.insertAtEnd(10)
    lista.insertAtEnd(15)
    print("Lista después de las inserciones:")
    lista.print()
    print("Valor 10 encontrado en el nodo: ", lista.search(10))
    print(lista.deleteAtEnd())
    print("Lista después de eliminar el último elemento:")
    lista.print()