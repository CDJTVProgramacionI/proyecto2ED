from grafo.nodo import NodoVertice
from grafo.arista import Arista
import flet.canvas as cv
import flet as ft

class Grafo:  # Clase que representa el grafo
    canvas : cv.Canvas  # Lienzo para dibujar el grafo
    
    def __init__(self):
        # Inicializa el grafo vacío
        self.vertices = []  # Vertices del grafo
        self.aristas = [] # Lista de aristas
        
        #Graficos
        self.canvas = cv.Canvas(width=650, height=525)  # Lienzo para dibujar el grafo

    def agregar_vertice(self,contaminado : bool) -> NodoVertice:
        """Agrega un vértice al grafo."""
        
        nombre = f"V{len(self.vertices) + 1}"  # Genera un nombre único para el vértice
        nodo = NodoVertice(nombre, contaminado)  # Crea un nuevo nodo de vértice
        nodo.set_on_pan(self.mover_circulo)  # Asigna la función de movimiento al nodo
        self.vertices.append(nodo)  # Agrega el vértice a la lista de vértices
        return nodo  # Retorna el nodo creado

    def buscar_vertice(self, nombre) -> NodoVertice:
        """Busca un vértice en la lista de vértices y retorna su posición."""
        for vertice in self.vertices:
            if vertice.nombre == nombre:
                return vertice
        return None


    def agregar_arista(self, origen : NodoVertice, destino : NodoVertice, peso: int):
        """Agrega una arista dirigida desde origen hacia destino con un peso."""
        vertice_origen = origen
        vertice_destino = destino
        
        #Agregar la arista a la lista de adyacencia del vértice origen y destino
        vertice_origen.adyacentes.insertAtEnd((destino, peso))
        vertice_destino.adyacentes.insertAtEnd((origen, peso))
        
        #Dibuja la arista entre los dos vértices
        arista = Arista(origen, destino, peso)
        self.canvas.shapes.append(arista.THE_LINE)  # Agrega la línea al lienzo
        self.canvas.shapes.append(arista.texto)  # Agrega el texto al lienzo
        self.canvas.update()  # Actualiza el lienzo con los cambios
        
        self.aristas.append(arista)  # Agrega la arista a la lista de aristas
        
    def matriz_costos(self):
        a = [[None] * len(self.vertices) for _ in range(len(self.vertices))] #Crea un arreglo de tamaño n*n
        for i in range (len(self.vertices)):
            a[i][i]= 0
            nodo = self.vertices[i]  # Obtiene el nodo correspondiente al índice i
            
            for j in range (nodo.adyacentes.len): 
                v,p=nodo.adyacentes.getAt(j)
                k = self.vertices.index(v) # Obtiene el índice del nodo adyacente
                a[i][k]=p
                
        return a
    
    def buscar_arista(self, origen, destino):
        """Busca una arista entre dos vértices."""
        for arista in self.aristas:
            if (arista.origen == origen and arista.destino == destino) or (arista.origen == destino and arista.destino == origen):
                return arista
        return None
    
    def mover_circulo(self, e: ft.DragUpdateEvent):
            # Obtener el círculo que se está moviendo
            circulo : ft.GestureDetector = e.control  # El círculo que se está moviendo  
            
            # Actualizar la posición del vértice
            circulo.top = max(0, circulo.top + e.delta_y)
            circulo.left = max(0, circulo.left + e.delta_x)
            circulo.update()
                  
            # Recorrer todas las aristas y redibujar
            for arista in self.aristas:
                arista.repaint()
            
    def borrar(self):
        """Borra el grafo."""
        self.canvas.shapes.clear()
        self.vertices.clear()
        self.aristas.clear()
        self.canvas.update()
        