import flet as ft
import flet.canvas as cv
import math
import random
import time
from listaAdyacencia import ListaAdyacencia
import heapq

circulo_activo = False  
mov_activo = False
seleccion = [] 
lista_vertices = []
lista_aristas = []
vertices_contaminados = []
vertices_no_contaminados = []
grafo = ListaAdyacencia()  # Se crea el grafo con los vértices

def reiniciar():
    texto_distancia.value = ""
    for i in range(len(grafo)):
        nodo = grafo.obtener_iesimo_vertice(i)
        for j in range(nodo.adyacentes.len):
            boton=nodo.adyacentes.getAt(j)[0] 
            x1 = lista_vertices[i].left + 25
            y1 = lista_vertices[i].top + 25
            x2 = lista_vertices[boton].left + 25
            y2 = lista_vertices[boton].top + 25

            genera_arista([x1,y1],[x2,y2],"BLACK")
    canvas.update()

def borrar(e : ft.ControlEvent):
    global grafo
    seleccion.clear()
    lista_vertices.clear()
    grafo = ListaAdyacencia()
    canvas.shapes.clear()
    canvas.update()
    workarea.controls = [canvas]
    workarea.update()

def hexa_random (): 
    num=random.randint(0,16777215)
    hexa=hex(num)
    hexa=hexa.replace('0x', '#')
    return hexa

def matriz_costos():
    a = [[None] * len(grafo) for _ in range(len(grafo))] #Crea un arreglo de tamaño n*n
    for i in range (len(grafo)):
        a[i][i]= 0
        nodo = grafo.obtener_iesimo_vertice(i)
        
        for j in range (nodo.adyacentes.len): 
            v,p=nodo.adyacentes.getAt(j)
            a[i][v]=p
            
    return a

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

def act_prim(event): 
    if len(seleccion) == 0:
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("Debe seleccionar un nodo inicial"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
        event.page.open(alert)
        return
    
    peso_total= 0
    mst = []  # Lista para almacenar el árbol de expansión mínima (MST)
    aristas = lista_aristas.copy()  # Copia de la lista de aristas
    aristas.sort(key=lambda x: x[2])  # Ordena las aristas por peso
    visitados = [False] * len(grafo)  # Lista para marcar los vértices visitados
    min_heap = []  # Cola de prioridad para seleccionar la arista de menor peso
    vertice_inicial = lista_vertices.index(seleccion[0])  # Vértice inicial para comenzar el algoritmo

    def agregar_aristas(v):
        visitados[v] = True  # Marca el vértice como visitado
        nodo = grafo.obtener_iesimo_vertice(v)  # Obtiene el nodo correspondiente al vértice
        for j in range(nodo.adyacentes.len):  # Itera sobre los adyacentes del nodo
            vecino, peso = nodo.adyacentes.getAt(j)  # Obtiene el vecino y el peso de la arista
            if not visitados[vecino]:  # Si el vecino no ha sido visitado
                heapq.heappush(min_heap, (peso, v, vecino))  # Añade la arista a la cola de prioridad

    agregar_aristas(vertice_inicial)  # Añade las aristas del vértice inicial a la cola de prioridad

    while min_heap:  # Mientras haya aristas en la cola de prioridad
        peso, v_inicio, v_fin = heapq.heappop(min_heap)  # Extrae la arista de menor peso
        

        if visitados[v_fin]:  # Si el vértice final ya ha sido visitado, continúa
            continue

        peso_total +=peso
        mst.append((v_inicio, v_fin, peso))  # Añade la arista al MST
        agregar_aristas(v_fin)  # Añade las aristas del nuevo vértice al MST

        # Genera una arista visual en la interfaz gráfica
        genera_arista([lista_vertices[v_inicio].left + 25, lista_vertices[v_inicio].top + 25],
                      [lista_vertices[v_fin].left + 25, lista_vertices[v_fin].top + 25],
                      "YELLOW")

        time.sleep(0.5)  #Tiempo de espera para una mejor visualización

        if len(mst) == len(grafo) - 1:  # Si el MST tiene el número correcto de aristas, termina
            break
    
    texto_distancia.value = f"El peso total del MST con Prim es: {peso_total}"
    texto_distancia.update()
    canvas.update()

def act_kruskal(event):
    peso_total= 0
    componentes = [[i] for i in range(len(grafo))]  # Cada vértice es una componente
    mst = []  # Aristas del árbol de expansión mínima
    aristas = lista_aristas.copy()  # Copiar la lista de aristas para no modificar la original
    aristas.sort(key=lambda x: x[2])  # Ordenar las aristas por peso
    for i in range(len(aristas)):
        v_inicio = aristas[i][0]
        v_fin = aristas[i][1]
        peso = aristas[i][2]
        
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
                    genera_arista([lista_vertices[v_inicio].left + 25, lista_vertices[v_inicio].top + 25],
                                  [lista_vertices[v_fin].left + 25, lista_vertices[v_fin].top + 25],
                                  ft.Colors.AMBER_500)
                    break
        
        if len(componentes) == 1:
            break
    texto_distancia.value = f"El peso total del MST con Kruskal es: {peso_total}"
    texto_distancia.update()
    canvas.update()
    
#Dijsktra  
def dijkstra(grafo : list, reciclaje: list, vertice_inicial : int):
    cant_vertices = len(grafo)
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
            
            dist = suma(d[w], grafo[w][v])
            if menor_dist is None:
                menor_dist = v
            else:
                menor_dist = v if lt(dist, d[menor_dist]) else menor_dist
            if grafo[w][v] != None and lt(dist, d[v]):
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
        x1 = lista_vertices[aux].left + 25
        y1 = lista_vertices[aux].top + 25
        x2 = lista_vertices[indi].left + 25
        y2 = lista_vertices[indi].top + 25
        genera_arista([x1,y1],[x2,y2],ft.Colors.AMBER_200)
        indi=aux

def floyd(grafo : list):
    cant_vertices = len(grafo)
    a = [[None] * cant_vertices for _ in range(cant_vertices)] #Crea un arreglo de tamaño n*n

    #Inicializar matriz de distancias con la de costos
    for i in range(cant_vertices):
        for j in range(cant_vertices):
            a[i][j] = grafo[i][j]
            

    for i in range(cant_vertices):
        a[i][i] = 0

    for k in range(cant_vertices):
        for i in range(cant_vertices):
            for j in range(cant_vertices):
                dist = suma(a[i][k], a[k][j])
                if lt(dist, a[i][j]):  
                    a[i][j] = dist


    return a #Retorna la matriz de distancias
        
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

def activar_movimiento(event):
     """Activa o desactiva el movimiento de los circulos al hacer clic en el botón."""
     global mov_activo
     mov_activo = not mov_activo
     #Cambiar color del botón según el estado
     bttn_moverNodo.bgcolor = ft.Colors.GREEN_ACCENT_100 if mov_activo else ft.Colors.PINK_100
     bttn_moverNodo.update()  # Refrescar solo cuando se cambia el estado

def presionar_boton_arista(e : ft.ControlEvent):
    
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
    
    v1 = lista_vertices.index(seleccion[0])  # Nombre del primer vértice
    v2 = lista_vertices.index(seleccion[1])  # Nombre del segundo vértice

    peso = campo_peso.value  # Peso de la arista

    grafo.agregar_arista(v1, v2, int(peso))  # Agregar la conexión en la lista de adyacencia

    x1 = seleccion[0].left + 25
    y1 = seleccion[0].top + 25
    seleccion[0].content.bgcolor = "blue"
    seleccion[0].update()
    
    x2 = seleccion[1].left + 25
    y2 = seleccion[1].top + 25
    seleccion[1].content.bgcolor = "blue"
    seleccion[1].update()
    
    seleccion.clear()
    genera_arista([x1, y1],[x2,y2],"BLACK")
    
    puntomed_x = (x1+x2)/2
    puntomed_y = (y1+y2)/2
    texto=cv.Text(puntomed_x,puntomed_y, campo_peso.value,ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_500, size=14))
    campo_peso.value = ""
    campo_peso.update()
    canvas.shapes.append(texto)
    canvas.update()  
    
    # Agregar la arista, vértice inicio y vértice final a la lista_aristas
    lista_aristas.append([v1, v2,int(peso)])  # Se agrega la arista con su peso y los vértices
    
def presionar_boton_vertice(e : ft.ControlEvent):
    if e.control.parent in seleccion:
        e.control.bgcolor = "blue"
        e.control.update()
        seleccion.remove(e.control.parent)
        return
    
    if len(seleccion) == 2:
        seleccion[0].content.bgcolor = "blue"
        seleccion[0].content.update()
        seleccion[1].content.bgcolor = "blue"
        seleccion[1].content.update()
        seleccion.clear()
        
    seleccion.append(e.control.parent)
    
    if len(seleccion) == 1:
        e.control.bgcolor = ft.Colors.GREEN_ACCENT_100
        e.control.update()
    else:
        e.control.bgcolor = ft.Colors.INDIGO
        e.control.update()
    
        
    
def genera_arista(inicio_coord,fin_coord,color): 
   paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE,color=color) 
   THE_LINE=cv.Line(inicio_coord[0],inicio_coord[1],fin_coord[0],fin_coord[1], paint)
  
   canvas.shapes.append(THE_LINE) #mybodysonthelinenowicantfightthistimenowicanfeel
   canvas.update()
   
   
canvas = cv.Canvas(width=650, height=525)
workarea = ft.Stack(width=650, height=525, controls=[canvas])
campo_peso = ft.TextField(label="Peso", width=70, height=40, color=ft.Colors.BLUE_400)
texto_distancia = ft.Text("", size=11, color="BLACK")

# Botón rectangular para activar/desactivar colocación de círculos
bttn_vertice =  ft.FilledButton(
    width=100, height=50,
    bgcolor=ft.Colors.PINK_100,  # Color inicial del botón
    text="VÉRTICES",
    on_click=activar_circulos  # Alternar modo de colocación al hacer clic
)

bttn_moverNodo = ft.FilledButton(
    width=100, height=50,
    bgcolor=ft.Colors.PINK_100,  # Color inicial del botón
    text="MOVER VÉRTICE",
    on_click=activar_movimiento  # Alternar modo de colocación al hacer clic
)

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
        
        
        def mover_circulo(e: ft.DragUpdateEvent):
            if not mov_activo:
                return
            
            # Actualizar la posición del vértice
            circulo.top = max(0, circulo.top + e.delta_y)
            circulo.left = max(0, circulo.left + e.delta_x)
            circulo.update()
            
            
            # Actualizar las posiciones de las aristas
            canvas.shapes.clear()  # Limpiar el canvas antes de redibujar las aristas

            
            # Recorrer todas las aristas y redibujar
            for v1, v2, peso in lista_aristas:
               
                # Obtener las nuevas posiciones de los vértices
                x1 = lista_vertices[v1].left + 25
                y1 = lista_vertices[v1].top + 25
                x2 = lista_vertices[v2].left + 25
                y2 = lista_vertices[v2].top + 25
            
                # Redibujar la arista entre v1 y v2
                genera_arista([x1, y1], [x2, y2], "BLACK")
            
                # Redibujar el peso de la arista
                puntomed_x = (x1 + x2) / 2
                puntomed_y = (y1 + y2) / 2
                texto = cv.Text(puntomed_x, puntomed_y, str(peso),
                                    ft.TextStyle(weight=ft.FontWeight.BOLD,
                                         color=ft.Colors.INDIGO_500,
                                         size=14))
                canvas.shapes.append(texto)

            canvas.update()  # Actualizar el canvas con los cambios
            
        print(f"Círculo colocado en las coordenadas: {x}, {y}")
        
         # Asignar color aleatorio al vértice
        color_vertice = random.choice(["#0000FF", "#FFA500"])  # Azul o Naranja

        circulo = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=50,
            on_pan_update=mover_circulo,
            content=ft.FilledButton(
                text=f"V{len(lista_vertices) + 1}",
                width=50, height=50,
                bgcolor=color_vertice,
                on_click=presionar_boton_vertice,
            )
        )
        
        circulo.top = y - 25
        circulo.left = x - 25
        
        grafo.agregar_vertice(len(lista_vertices))  # Agregar el vértice a la lista de adyacencia        
        lista_vertices.append(circulo)
        workarea.controls.append(circulo)  # Agregar el círculo al canvas
        
            # Guardar el índice del vértice en la lista correspondiente
        if color_vertice == "#FFA500":
            vertices_contaminados.append(len(lista_vertices) - 1)
        else:
            vertices_no_contaminados.append(len(lista_vertices) - 1)

        
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
        ft.Row(
            [
                bttn_vertice,
                bttn_moverNodo,
                ft.FilledButton(
                    text="Generar Arista",
                    bgcolor=ft.Colors.BLUE_50,
                    color=ft.Colors.BLUE_400,
                    on_click=presionar_boton_arista), 
                campo_peso,
                ft.FilledButton(text="Reiniciar",bgcolor=ft.Colors.BLUE_50,on_click=lambda e : reiniciar()),
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color=ft.Colors.RED_500,
                    icon_size=40,
                    tooltip="Borrar grafo",
                    on_click=borrar
                )
                  
            ]
        ),
        ft.Container(width=10,height=25,)

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
                        ft.FilledTonalButton(text="Algoritmo Floyd",bgcolor=ft.Colors.INDIGO_500,on_click=lambda e: floyd()),
                        ft.FilledTonalButton(text="Algoritmo Dijkstra",bgcolor=ft.Colors.INDIGO_500,on_click=lambda e : dijkstra(matriz_costos(),[0,1],2)),
                        texto_distancia
                       
                    ]
                    
                )
            ]
        
        )

    )
    
if __name__ == "__main__":
    hexa_random()
    ft.app(screen_main)