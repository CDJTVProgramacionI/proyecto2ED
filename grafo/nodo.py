from grafo.listaSimpleDinamica import LinkedList
import flet as ft

class NodoVertice:  # Para guardar la información de cada vértice y con base a esta hacer la lista de adyacencia (el arreglo de listas simples)
    def __init__(self, nombre, contaminado : bool): 
        #Lógica para crear un nodo de vértice
        self.contaminado = contaminado
        self.nombre = nombre  # Nombre del vértice (Ej: "V1", "V2")
        self.adyacentes = LinkedList()  # Lista de adyacencia (lista de vértices adyacentes)
        self.estado = 0  
        
        #Gráfico
        self.color = "blue" if not contaminado else "#FFA500"
        self.boton = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=50,
            content=ft.FilledButton(
                text=nombre,
                width=50, height=50,
                bgcolor=self.color,
                data=nombre
            )
        )
        
    def set_on_pan(self, on_pan_update):
        self.boton.on_pan_update = on_pan_update
        
    def set_on_click(self, on_click):
        self.boton.content.on_click = on_click

        
    def setEstado(self, estado):
        self.estado = estado
    
    def estaEnEspera(self):
        return self.estado == 0