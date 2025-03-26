from listaSimpleDinamica import LinkedList

class NodoVertice:  # Para guardar la información de cada vértice y con base a esta hacer la lista de adyacencia (el arreglo de listas simples)
    def __init__(self, nombre): 
        self.nombre = nombre  # Nombre del vértice (Ej: "V1", "V2")
        self.adyacentes = LinkedList()  # Lista enlazada de vecinos
        self.siguiente = None  # Apunta al siguiente vértice en el grafo
        self.estado = 0  
        
    def setEstado(self, estado):
        self.estado = estado
    
    def estaEnEspera(self):
        return self.estado == 0

class ListaAdyacencia:
    def __init__(self):
        self.cabeza = None  # Primer vértice en la lista

    def agregar_vertice(self, nombre):
        """Agrega un vértice al grafo."""
        nuevo_vertice = NodoVertice(nombre)
        if self.cabeza is None:
            self.cabeza = nuevo_vertice
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_vertice

    def buscar_vertice(self, nombre):
        """Busca un vértice en la lista de adyacencia."""
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None


    def agregar_arista(self, nombre_origen, nombre_destino, peso):
        """Agrega una arista dirigida desde origen hacia destino con un peso."""
        vertice_origen = self.buscar_vertice(nombre_origen)
        vertice_destino = self.buscar_vertice(nombre_destino)
        if vertice_origen and vertice_destino:
            vertice_origen.adyacentes.insertAtEnd((nombre_destino, peso))
            vertice_destino.adyacentes.insertAtEnd((nombre_origen, peso))


    def mostrar(self):
        """Muestra la lista de adyacencia del grafo."""
        actual = self.cabeza
        while actual:
            # Se imprime el nombre del vértice y sus adyacentes
            print(f"{actual.nombre} → {actual.adyacentes.print()}")
            actual = actual.siguiente
            
    def __len__(self):
        """Devuelve el número de vértices en el grafo."""
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def obtener_iesimo_vertice(self, i):
        """Devuelve el i-ésimo vértice en la lista."""
        actual = self.cabeza
        for _ in range(i):
            actual = actual.siguiente
        return actual

    def buscar_vertice_pos(self, nombre):
        """Busca un vértice en la lista de adyacencia."""
        actual = self.cabeza
        pos = 0
        while actual:
            if actual.nombre == nombre:
                return pos
            actual = actual.siguiente
            pos += 1
        return None
        