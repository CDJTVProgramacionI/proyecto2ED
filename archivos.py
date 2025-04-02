from pickle import load, dump
from grafo.grafo import Grafo
import os
from datetime import datetime
import random
from pickle import load




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



def cargar_archivo_aleatorio(directorio, extension='.bin'):
    """Cargar un archivo aleatorio con la extensión especificada en el directorio dado."""
    # Asegurarse de que 'directorio' es una cadena que represente una ruta válida
    if not isinstance(directorio, str):
        print(f"Error: El directorio debe ser una cadena de texto. Tipo recibido: {type(directorio)}")
        return None
    
    # Verificar si el directorio existe
    if not os.path.isdir(directorio):
        print(f"Error: El directorio '{directorio}' no es válido.")
        return None
    
    # Obtener todos los archivos en el directorio que tienen la extensión .bin
    archivos = [archivo for archivo in os.listdir(directorio) if archivo.endswith(extension)]
    
    if not archivos:
        print(f"No se encontraron archivos con la extensión {extension} en {directorio}")
        return None
    
    # Depuración: Mostrar la lista de archivos encontrados
    print(f"Archivos encontrados: {archivos}")
    
    # Seleccionar un archivo aleatorio
    archivo_aleatorio = random.choice(archivos)
    
    # Depuración: Mostrar el archivo seleccionado aleatoriamente
    print(f"Archivo seleccionado aleatoriamente: {archivo_aleatorio}")
    
    # Ruta completa del archivo
    archivo_completo = os.path.join(directorio, archivo_aleatorio)
    
    return archivo_completo

def cargar_grafo(workarea, directorio=r"C:\Users\Viridiana\Downloads\proyecto2ED-proyecto_version_2"):
    """Carga un grafo de un archivo aleatorio."""
    # Asegurarse de que 'directorio' es una cadena válida
    if not isinstance(directorio, str):
        print(f"Error: El directorio debe ser una cadena de texto. Tipo recibido: {type(directorio)}")
        return None
    
    # Obtener un archivo aleatorio
    archivo_aleatorio = cargar_archivo_aleatorio(directorio)
    
    if not archivo_aleatorio:
        return None  # Si no se encuentra archivo, retornamos None
    
    try:
        with open(archivo_aleatorio, 'rb') as f:
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
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None



def obtener_vertice(grafo, nombre):
    """Busca un vértice en el grafo por su nombre."""
    for vertice in grafo.vertices:
        if vertice.nombre == nombre:
            return vertice
    return None
    

def generar_nombre_unico(archivo_base):
    """Genera un nombre único para el archivo usando un timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Obtén la fecha y hora actual
    archivo_unico = f"{archivo_base}_{timestamp}.bin"
    return archivo_unico

def guardar_grafo(archivo_base, grafo):
    """Guarda el grafo en un archivo con un nombre único para evitar sobrescribir."""
    archivo_unico = generar_nombre_unico(archivo_base)
    
    with open(archivo_unico, 'wb') as f:
        vertices = []
        aristas = []
        
        # Serializar los vértices
        for vertice in grafo.vertices:
            vertices.append(VerticeSerializado(vertice.nombre, vertice.contaminado, vertice.estado, (vertice.boton.left, vertice.boton.top)))
        
        # Serializar las aristas
        for arista in grafo.aristas:
            origen = arista.origen.nombre
            destino = arista.destino.nombre
            aristas.append(AristaSerializada(origen, destino, arista.peso))
        
        # Crear el objeto serializado del grafo
        contenido = GrafoSerializado(vertices, aristas)
        
        # Guardar en el archivo binario
        dump(contenido, f)