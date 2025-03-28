import flet as ft
import flet.canvas as cv
from grafo.nodo import NodoVertice

class Arista:
    def __init__(self, origen : NodoVertice, destino : NodoVertice, peso : int):
        """Clase que representa una arista entre dos nodos."""    
        #Lógica para crear una arista
        self.origen = origen  # Nodo de origen
        self.destino = destino  # Nodo de destino
        self.peso = peso  # Peso de la arista
        
        #Obtenemos las coordenadas de los nodos origen y destino
        x1 = origen.boton.left + 25
        y1 = origen.boton.top + 25
        
        x2 = destino.boton.left + 25
        y2 = destino.boton.top + 25
        
    
        #Graficos
        self.color = "black"  # Color por defecto de la arista
        self.paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE,color=self.color)  # Estilo de la línea
        #Dibuja la línea entre los dos nodos
        self.THE_LINE=cv.Line(x1, y1, x2, y2, self.paint)
        
        puntomed_x = (x1+x2)/2
        puntomed_y = (y1+y2)/2
        self.texto=cv.Text(puntomed_x,puntomed_y, peso, ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_500, size=14))
        
    def repaint(self, color : ft.Colors = "black"):
        """Redibuja la arista."""
        #Obtenemos las coordenadas de los nodos origen y destino
        x1 = self.origen.boton.left + 25
        y1 = self.origen.boton.top + 25
        
        x2 = self.destino.boton.left + 25
        y2 = self.destino.boton.top + 25
        
        #Repinta la línea
        self.paint.color = color
        
        self.THE_LINE.x1 = x1
        self.THE_LINE.y1 = y1
        self.THE_LINE.x2 = x2
        self.THE_LINE.y2 = y2
        self.THE_LINE.paint = self.paint
        
        self.THE_LINE.update()
        
        #Reubica el texto
        puntomed_x = (x1+x2)/2
        puntomed_y = (y1+y2)/2
        
        self.texto.x = puntomed_x
        self.texto.y = puntomed_y
        self.texto.update()
        
    def __lt__ (self, other):
        """Compara dos aristas por su peso."""
        return self.peso < other.peso
    
    def __eq__ (self, other):
        """Compara dos aristas por su peso."""
        return self.peso == other.peso
        
        