import flet as ft
import flet.canvas as cv
import random
import time
from grafo.nodo import NodoVertice
from grafo.grafo import Grafo
from Piladinamica import pila
from Piladinamica import pila
from colalineal import ColaLineal
from archivos import guardar_grafo, cargar_grafo
import heapq

circulo_activo = False  
seleccion = [] 
vertices_contaminados = []
vertices_no_contaminados = []
grafo = Grafo()  # Se crea el grafo con los vértices

def reiniciar():
    texto_distancia.value = ""
    for arista in grafo.aristas:
        arista.repaint("black")

def borrar(e : ft.ControlEvent):
    grafo.borrar()
    seleccion.clear()
    workarea.controls = [grafo.canvas]
    workarea.update()

def recorrido_anchura(event):
    
    if len(seleccion) == 0:
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("Debe seleccionar un nodo inicial"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
        event.page.open(alert)
        return
    
    # Reiniciar estados de los vértices
    for vertice in grafo.vertices:
        vertice.setEstado(0)  # Estado 0: En espera

    # Crear la cola para el recorrido en anchura
    cola = ColaLineal()
    
    # Obtener el índice del vértice inicial de la selección
    nodo_inicial = seleccion[0]  # Seleccionar el primer nodo de la lista de selección

    # Iniciar el BFS
    if nodo_inicial.estaEnEspera():
        nodo_inicial.setEstado(0)  # Estado 0: En espera
        cola.encolar(nodo_inicial)
    else:
        print("El vértice inicial ya está contaminado.")
        return
    
    while not cola.esta_vacio():
        nodo_actual = cola.desencolar()
        
        # Si el nodo ya no está en espera (por ejemplo, si es contaminado) lo saltamos
        if not nodo_actual.estaEnEspera():
            continue

        nodo_actual.setEstado(2)  # Marcamos como visitado
        
        # Procesamos cada vecino del nodo_actual
        vecinos = nodo_actual.adyacentes #Lista Simple de adyacentes
        for vecino in range(vecinos.len):
            nodo, _ = nodo_actual.adyacentes.getAt(vecino)  # Obtenemos nodo vecino
            # Solo se encola si el vecino no ha sido visitado (estado 0)
            if nodo.estaEnEspera():
                nodo.setEstado(0)  # Marcar como en espera
                cola.encolar(nodo)

                # Dibujar la arista entre nodo_actual y nodo en verde
                arista=grafo.buscar_arista(nodo_actual, nodo)  # Obtener el índice del nodo actual
                arista.repaint("green")  # Resaltar en verde
                time.sleep(0.5)  # Pausa para visualizar paso a paso

    print("Recorrido en anchura finalizado.")
    
def hexa_random (): 
    while True:
        #Se genera un numero random
        num=random.randint(0,16777215)
        hexa=hex(num)
        hexa=hexa.replace('0x', '#')
        
        # Evitar colores específicos
        if hexa not in ["#e3f2fd", "#000000"]:  # Ahora los colores tienen '#'
            return hexa  # Devuelve el color si no está en la lista prohibida 
           
def recorrido_profundidad(event):
    
    if len(seleccion) == 0:
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("Debe seleccionar un nodo inicial"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
        event.page.open(alert)
        return
    
    # Reiniciar estados de los vértices
    for vertice in grafo.vertices:
        vertice.setEstado(0)  # Estado 0: En espera
    
    #pila para recorrido en profundidad (DFS)
    stack = pila()
    
    # Obtener el nodo inicial de la selección
    nodo_inicial = seleccion[0]  # Seleccionar el primer nodo de la lista de selección
    
    # Iniciar DFS desde el nodo inicial
    nodo_inicial.setEstado(1)  # Estado 1: En proceso
    stack.push(nodo_inicial)

    while not stack.estavacio():
        nodo_actual = stack.pop()
        
        # Si el nodo ya fue visitado (estado 2), lo ignoramos
        # Paint edges of an already visited vertex
        for vecino in range(nodo_actual.adyacentes.len):
            nodo_vecino, _ = nodo_actual.adyacentes.getAt(vecino)
            if nodo_vecino.estado == 2:  # If the neighbor is already visited
                arista = grafo.buscar_arista(nodo_actual, nodo_vecino)  # Find the edge
                arista.repaint("green")  # Paint the edge blue
                time.sleep(0.5)  
        if nodo_actual.estado == 2:
            continue

        nodo_actual.setEstado(2)  # Marcamos como visitado

        # Visualizar en la interfaz
        vecinos = nodo_actual.adyacentes
        
        for vecino in range (vecinos.len):
            nodo_vecino, _ = nodo_actual.adyacentes.getAt(vecino)  # Obtenemos índice de la arista

            if nodo_vecino.estado == 0:  # Solo encolamos si está en espera
                nodo_vecino.setEstado(1)  # Estado 1: En proceso
                stack.push(nodo_vecino)
                
                #Buscamos la arista
                arista = grafo.buscar_arista(nodo_actual, nodo_vecino)  # Obtener la arista entre nodo_actual y nodo_vecino
                arista.repaint(hexa_random())  # Resaltar en verde
                time.sleep(0.5)  # Pausa para visualizar cada paso

    print("Recorrido en profundidad finalizado.")
    
def determinar_bosque():
        #Determinar si el bosque es denso o disperso
        num_vertices = len(grafo.vertices)  # Número de vértices en el grafo
        num_aristas = len(grafo.aristas)  # Número de aristas en el grafo
        #numero maximo de conexiones en un grafo completo
        max_conexiones = num_vertices * (num_vertices - 1) // 2  # Máximo de aristas en un grafo completo
        #numero minimo de conexiones en un grafo completo
        min_conexiones = num_vertices - 1  # Mínimo de aristas para un árbol

        #Calcular si el numero de caminos esta mas cerca del maximo o del minimo
        if abs (num_aristas - max_conexiones) < abs(num_aristas - min_conexiones):
            return "Denso" 
        else:
            return "Disperso"
        
def ejecutar_prim_o_kruskal(event):
    # Determinar el tipo de bosque (denso o disperso)
    tipo_bosque = determinar_bosque()
    
    if tipo_bosque == "Denso":
        texto_distancia.value = "El bosque es denso, se ejecutará Prim."
        texto_distancia.update()
        act_prim(event)  # Ejecutar Prim si el bosque es denso
    else: 
        texto_distancia.value = "El bosque es disperso, se ejecutará kruskal."
        texto_distancia.update()
        act_kruskal(event)  # Ejecutar Kruskal si el bosque es disperso

def act_prim(event):
    if len(seleccion) == 0:
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("Debe seleccionar un nodo inicial"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
        event.page.open(alert)
        return
    
    peso_total= 0
    mst = []  # Lista para almacenar el árbol de expansión mínima (MST)
    aristas = grafo.aristas.copy()  # Copia de la lista de aristas
    aristas.sort(key=lambda x: x.peso)  # Ordena las aristas por peso
    visitados = [False] * len(grafo.vertices)  # Lista para marcar los vértices visitados
    min_heap = []  # Cola de prioridad para seleccionar la arista de menor peso
    vertice_inicial = grafo.vertices.index(seleccion[0] ) # Vértice inicial para comenzar el algoritmo

    def agregar_aristas(v):
        visitados[v] = True  # Marca el vértice como visitado
        nodo = grafo.vertices[v]  # Obtiene el nodo correspondiente al vértice
        for j in range(nodo.adyacentes.len):  # Itera sobre los adyacentes del nodo
            vecino, peso = nodo.adyacentes.getAt(j)  # Obtiene el vecino y el peso de la arista
            if not visitados[grafo.vertices.index(vecino)]:  # Si el vecino no ha sido visitado
                heapq.heappush(min_heap, (peso, v, grafo.vertices.index(vecino)))  # Añade la arista a la cola de prioridad

    agregar_aristas(vertice_inicial)  # Añade las aristas del vértice inicial a la cola de prioridad

    while min_heap:  # Mientras haya aristas en la cola de prioridad
        peso, v_inicio, v_fin = heapq.heappop(min_heap)  # Extrae la arista de menor peso
        

        if visitados[v_fin]:  # Si el vértice final ya ha sido visitado, continúa
            continue

        peso_total +=peso
        mst.append((v_inicio, v_fin, peso))  # Añade la arista al MST
        agregar_aristas(v_fin)  # Añade las aristas del nuevo vértice al MST
        
        arista = grafo.buscar_arista(grafo.vertices[v_inicio], grafo.vertices[v_fin])  # Obtener la arista entre los nodos
        arista.repaint("green")  # Resaltar la arista en verde

        time.sleep(0.5)  #Tiempo de espera para una mejor visualización

        if len(mst) == len(grafo.vertices) - 1:  # Si el MST tiene el número correcto de aristas, termina
            break
    
    texto_distancia.value = f"El peso total del MST con Prim es: {peso_total}"
    texto_distancia.update()

def act_kruskal(event):
    peso_total= 0
    componentes = [[nodo] for nodo in grafo.vertices]  # Cada vértice es una componente
    mst = []  # Aristas del árbol de expansión mínima
    aristas = grafo.aristas.copy()  # Copiar la lista de aristas para no modificar la original
    aristas.sort(key=lambda x: x.peso)  # Ordenar las aristas por peso
    for i in range(len(aristas)):
        v_inicio = aristas[i].origen
        v_fin = aristas[i].destino
        peso = aristas[i].peso
        
        # Verificar si los vértices están en componentes distintas
        for c in componentes:
            if v_inicio in c:
                if v_fin in c:
                    #Estan en la misma componente
                    break
                else:
                    #Estan en diferentes componentes
                    mst.append(aristas[i])
                    peso_total += peso
                    
                    #Busca la componente a la que pertenece v_fin
                    c2 = buscar_componente(v_fin, componentes)
                    c.extend(c2)
                    componentes.remove(c2)
                    time.sleep(0.5)
                    aristas[i].repaint(ft.Colors.AMBER_500)  # Resaltar la arista en amarillo
                    break
        
        if len(componentes) == 1:
            break
    texto_distancia.value = f"El peso total del MST con Kruskal es: {peso_total}"
    texto_distancia.update()
        
def suma(a : any, b : any) -> int:
        if a == None or b == None:
            return None
        else:
            return a + b
    
def lt(a : any, b : any) -> bool:
    if b is None:
        return True
    elif a is None:
        return False
    else:
        return a < b 
    
#Dijsktra  
def dijkstra(mat_pesos : list, reciclaje: list, vertice_inicial : int):
    cant_vertices = len(mat_pesos)
    s = [vertice_inicial] #Crea un arreglo con el vértice inicial
    d = [None] * cant_vertices #Crea un arreglo de tamaño n 
    p = [None] * cant_vertices            
    
    d[s[0]] = 0       
    w = s[0]
    for i in range(cant_vertices - 1):
        menor_dist = None
        for v in range(cant_vertices):
            #Si w está en s, revisa el siguiente vértice
            if v in s:
                continue
            
            dist = suma(d[w], mat_pesos[w][v])
            if menor_dist is None:
                menor_dist = v
            else:
                menor_dist = v if lt(dist, d[menor_dist]) else menor_dist
            if mat_pesos[w][v] != None and lt(dist, d[v]):
                p[v] = w
                d[v] = dist
        w = menor_dist
        s.append(w)

    aux=0
    for nodo in reciclaje: 
        if nodo!=vertice_inicial and lt(d[nodo],d[aux]): 
            aux=nodo
    indi=aux
    while(p[indi] != None): 
        aux=p[indi]
        v1 = grafo.vertices[aux]
        v2 = grafo.vertices[indi]
        arista = grafo.buscar_arista(v1, v2)  # Obtener la arista entre los nodos
        arista.repaint(ft.Colors.AMBER_200) # Resaltar la arista en amarillo

def floyd(mat : list):
    cant_vertices = len(mat)
    a = mat.copy() #Copia la matriz de costos
    pre=[]
    
    for i in range(cant_vertices):
            pre.append([i]*cant_vertices)

    for i in range(cant_vertices):
        a[i][i] = 0
        pre[i][i] = None  #La diagonal principal es nula

    for k in range(cant_vertices):
        for i in range(cant_vertices):
            for j in range(cant_vertices):
                dist = suma(a[i][k], a[k][j])
                if lt(dist, a[i][j]):  
                    a[i][j] = dist
                    pre[i][j] = pre[k][j]  # Actualiza el predecesor

    print(pre)
        
def buscar_componente(v2, componentes):
    for c2 in componentes:
        if v2 in c2:
            return c2
            
def activar_circulos(event):
    """Activa o desactiva la colocación de círculos al hacer clic en el botón."""
    global circulo_activo
    circulo_activo = not circulo_activo

    # Cambiar color del botón según el estado
    bttn_vertice.bgcolor = ft.Colors.GREEN_ACCENT_100 if circulo_activo else ft.Colors.PINK_100
    bttn_vertice.update()  # Refrescar solo cuando se cambia el estado

def presionar_boton_arista(e : ft.ControlEvent):
    
    #Validaciones
    if campo_peso.value.replace(" ","") == "":
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("Debe ingresar un peso"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
        e.page.open(alert)
        return
    
    if not campo_peso.value.isnumeric():
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("El peso debe ser un número positivo"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
        e.page.open(alert)
        return
    
    if len(seleccion) != 2:
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("Debe seleccionar dos vértices"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
        e.page.open(alert)
        return
    
    v1 = seleccion[0] #Primer vértice
    v2 = seleccion[1] #Segundo vértice

    peso = campo_peso.value  # Peso de la arista

    grafo.agregar_arista(v1, v2, int(peso))  # Agregar la conexión en la lista de adyacencia

    #Limpia la selección
    seleccion[0].boton.content.bgcolor = seleccion[0].color
    seleccion[0].boton.content.update()
    seleccion[1].boton.content.bgcolor = seleccion[1].color
    seleccion[1].boton.content.update()
    seleccion.clear()
    
    #Limpia el campo de peso
    campo_peso.value = ""
    campo_peso.update()
    
def presionar_boton_vertice(e : ft.ControlEvent):
    nodo = grafo.buscar_vertice(e.control.data)  # Obtener el nodo correspondiente al botón
    if nodo in seleccion:
        e.control.bgcolor = nodo.color
        e.control.update()
        seleccion.remove(nodo)
        return
    
    if len(seleccion) == 2:
        # Si ya hay dos nodos seleccionados, deseleccionar todo
        seleccion[0].boton.content.bgcolor = seleccion[0].color
        seleccion[0].boton.content.update()
        seleccion[1].boton.content.bgcolor = seleccion[1].color
        seleccion[1].boton.content.update()
        seleccion.clear()
        
    seleccion.append(nodo)  # Agregar el nodo a la lista de selección
    
    # Cambiar el color del botón al seleccionar
    if len(seleccion) == 1:
        # Cambiar el color del primer nodo seleccionado
        e.control.bgcolor = ft.Colors.GREEN_ACCENT_100
        e.control.update()
    else:
        # Cambiar el color del segundo nodo seleccionado
        e.control.bgcolor = ft.Colors.INDIGO
        e.control.update()
        
workarea = ft.Stack(width=650, height=525, controls=[grafo.canvas])
campo_peso = ft.TextField(label="Peso", width=70, height=40, color=ft.Colors.BLUE_400)
texto_distancia = ft.Text("", size=11, color="BLACK")

# Botón rectangular para activar/desactivar colocación de círculos
bttn_vertice =  ft.FilledButton(
    width=100, height=50,
    bgcolor=ft.Colors.PINK_100,  # Color inicial del botón
    text="VÉRTICES",
    on_click=activar_circulos  # Alternar modo de colocación al hacer clic
)

def bttn_guardar(e : ft.ControlEvent):
    """Guarda el grafo en un archivo."""
    guardar_grafo("grafo.pkl", grafo)  # Guardar el grafo en un archivo
    
def bttn_cargar(e : ft.ControlEvent):
    """Carga el grafo desde un archivo."""
    global grafo
    
    # Aquí se carga el grafo desde un archivo aleatorio
    grafo = cargar_grafo(workarea)  # Cargar el grafo desde un archivo aleatorio en el directorio
    
    if grafo is None:
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("No se pudo cargar el grafo"), [ft.TextButton("Aceptar", on_click=lambda e: e.page.close(alert))])
        e.page.open(alert)
        return
    
    for vertice in grafo.vertices:
        vertice.set_on_click(presionar_boton_vertice)
        workarea.controls.append(vertice.boton)  # Agregar el botón al área de trabajo
    
    workarea.update()  # Refrescar el área de trabajo

def screen_main(page : ft.Page):
    
    page.title = "Visual Graph"
    page.vertical_alignment = ft.MainAxisAlignment.END

    page.window.width = 900
    page.window.height = 700
    page.bgcolor = ft.Colors.WHITE
    page.window.resizable = False

        
    def on_tap_down(event: ft.TapEvent):
        """Coloca círculos si el modo está activado y el clic no fue en el botón."""
        if not circulo_activo:
            return  # No hacer nada si el modo no está activado

        x = event.local_x  # Obtener coordenadas del clic
        y = event.local_y  # Obtener coordenadas del clic
    
        print(f"Círculo colocado en las coordenadas: {x}, {y}")
        
        # Asignar aleatoriamente si es contaminado o no
        contaminado = random.choice([True, False])
        
        #Agregar un nuevo vértice al grafo
        nodo = grafo.agregar_vertice(contaminado) 
        nodo.set_on_click(presionar_boton_vertice)  # Asignar la función al evento de clic
        nodo.boton.top = y - 25  # Ajustar la posición del botón vértice
        nodo.boton.left = x - 25  # Ajustar la posición del botón vértice
        workarea.controls.append(nodo.boton)  # Agregar el botón al área de trabajo
        workarea.update()  # Actualizar el área de trabajo para mostrar el nuevo vértice
        
        # Guardar el índice del vértice en la lista correspondiente
        if contaminado:
            vertices_contaminados.append(len(grafo.vertices) - 1)
        else:
            vertices_no_contaminados.append(len(grafo.vertices) - 1)

        
        page.update()  # Actualizar la pantalla

    instrucciones = ft.Text(
                    "Para que el algoritmo Prim muestre un\n"
                    "MST debe seleccionar el nodo inicial\n"
                    "El algoritmo de Kruscal muestra\n"
                    "encuentra el MST comenzando por la\n"
                    "arista de menor peso en el grafo\n",
                    color="Black", 
                    size=11, 
                    no_wrap=False, 
                )
        
    contenedor=ft.Container(content=instrucciones,expand=False)
        
    page.add(
    ft.Column(
        [
            ft.Text("¿Qué es un grafo?", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("¿Cómo se representa un grafo en programación?", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("¿Cuál es la diferencia entre un grafo dirigido y uno no dirigido?", size=20, weight=ft.FontWeight.BOLD)
        ]
    ),
    ft.Container(width=10, height=25)
    )

    page.add(
        ft.Row(
            [
                ft.Container(
                    bgcolor=ft.Colors.BLUE_50,
                    width=650,
                    height=525,
                    content=workarea,
                    on_tap_down=on_tap_down
                ), 

                ft.Column(
                    [

                        ft.Text("Instrucciones",size=20,bgcolor=ft.Colors.INDIGO_100,weight=ft.FontWeight.BOLD,italic=True), 
                        contenedor, 
                        ft.Text("Ejecutar Algoritmo",color="BLACK"), 
                        ft.FilledTonalButton(text="Algoritmo Kruskal",bgcolor=ft.Colors.INDIGO_500,on_click=act_kruskal),
                        ft.FilledTonalButton(text="Algoritmo Prim",bgcolor=ft.Colors.INDIGO_500,on_click=act_prim), 
                        ft.FilledTonalButton(text="Algoritmo Dijkstra",bgcolor=ft.Colors.INDIGO_500,on_click=lambda e : dijkstra(grafo.matriz_costos(),[0,1],2)),
                        ft.FilledTonalButton(text="Algoritmo Floyd",bgcolor=ft.Colors.INDIGO_500,on_click=lambda e : floyd(grafo.matriz_costos())),
                        ft.FilledTonalButton(text="Recorrido Anchura",bgcolor=ft.Colors.INDIGO_500,on_click=recorrido_anchura),
                        ft.FilledTonalButton(text="Recorrido Profundidad",bgcolor=ft.Colors.INDIGO_500,on_click=recorrido_profundidad),
                        ft.FilledTonalButton(text="Cargar",bgcolor=ft.Colors.INDIGO_500,on_click=bttn_cargar),
                        texto_distancia        
                    ]
                    
                )
            ]
        
        )

    )
    
if __name__ == "__main__":
    ft.app(screen_main)