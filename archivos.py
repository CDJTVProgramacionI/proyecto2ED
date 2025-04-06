from pickle import load, dump
from grafo.grafo import Grafo

class GrafoSerializado:
    """Clase para serializar y deserializar un grafo."""
    def __init__(self, vertices, aristas):
        self.vertices = vertices
        self.aristas = aristas
        
class VerticeSerializado:
    """Clase para serializar un vertice."""
    def __init__(self, nombre, contaminado, estado, posicion):
        self.contaminado = contaminado
        self.nombre = nombre  # Nombre del vértice (Ej: "V1", "V2")
        self.estado = estado
        self.posicion = posicion  # Posición inicial del vértice (se asignará en el grafo)
        
class AristaSerializada:
    """Clase para serializar una arista."""
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso  

def cargar_grafo(archivo, workarea):
    """Lee un archivo y devuelve su contenido."""
    try:
        with open(archivo, 'rb') as f:
            carga = load(f)
            grafo = Grafo()
            
            workarea.controls = [grafo.canvas]
            workarea.update()
            
            for vertice in carga.vertices:
                nodo = grafo.agregar_vertice(vertice.contaminado)
                nodo.nombre = vertice.nombre
                nodo.estado = vertice.estado
                nodo.boton.left = vertice.posicion[0]
                nodo.boton.top = vertice.posicion[1]
                
            for arista in carga.aristas:
                origen = obtener_vertice(grafo, arista.origen)
                destino = obtener_vertice(grafo, arista.destino)
                grafo.agregar_arista(origen, destino, arista.peso)
                
            return grafo
                
    except FileNotFoundError:
        return None
    
def obtener_vertice(grafo, nombre):
    """Busca un vértice en el grafo por su nombre."""
    for vertice in grafo.vertices:
        if vertice.nombre == nombre:
            return vertice
    return None
    
def guardar_grafo(archivo, grafo):
    """Escribe contenido en un archivo."""
    with open(archivo, 'wb') as f:
        vertices = []
        aristas = []
        for vertice in grafo.vertices:
            vertices.append(VerticeSerializado(vertice.nombre, vertice.contaminado, vertice.estado, (vertice.boton.left, vertice.boton.top)))
            
        for arista in grafo.aristas:
            origen = arista.origen.nombre
            destino = arista.destino.nombre
            aristas.append(AristaSerializada(origen, destino, arista.peso))
            
        contenido = GrafoSerializado(vertices, aristas)
        dump(contenido, f)