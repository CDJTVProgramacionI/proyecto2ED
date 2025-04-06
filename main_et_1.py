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
import menu_screen
import heapq

circulo_activo = False  
seleccion = [] 
vertices_contaminados = []
vertices_no_contaminados = []
grafo = Grafo()  # Se crea el grafo con los vértices
respuestas_correctas_etapa2 = {
    1: "Recorrido Anchura",
    2: "Algoritmo Dijkstra",
    3: "Algoritmo Prim"

}

respuestas_correctas_etapa3 = {
    1: "Recorrido Profundidad",
    2: "Algoritmo Floyd",
    3: "Algoritmo Kruskal"
}



def reiniciar():
    texto_distancia.value = ""
    for arista in grafo.aristas:
        arista.repaint("black")

def recorrido_anchura(event):
    # Reiniciar estados de los vértices
    for vertice in grafo.vertices:
        vertice.setEstado(0)  # Estado 0: En espera

    # Crear la cola para el recorrido en anchura
    cola = ColaLineal()
    
    # Obtener el índice del vértice inicial de la selección
    nodo_inicial = grafo.vertices[0]  # Seleccionar el primer nodo de la lista

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
    # Reiniciar estados de los vértices
    for vertice in grafo.vertices:
        vertice.setEstado(0)  # Estado 0: En espera
    
    #pila para recorrido en profundidad (DFS)
    stack = pila()
    
    # Obtener el nodo inicial de la selección
    nodo_inicial = grafo.vertices[0]  # Seleccionar el primer nodo de la lista de selección
    
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

def act_prim(event):
    peso_total= 0
    mst = []  # Lista para almacenar el árbol de expansión mínima (MST)
    aristas = grafo.aristas.copy()  # Copia de la lista de aristas
    aristas.sort(key=lambda x: x.peso)  # Ordena las aristas por pesos
    visitados = [False] * len(grafo.vertices)  # Lista para marcar los vértices visitados
    min_heap = []  # Cola de prioridad para seleccionar la arista de menor peso
    vertice_inicial = 0 # Vértice inicial para comenzar el algoritmo

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
def dijkstra(mat_pesos : list, reciclaje: list):
    vertice_inicial = 0
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

    aux=reciclaje[0]
    for nodo in reciclaje: 
        if lt(d[nodo],d[aux]): 
            aux=nodo
    indi=aux

    while(p[indi] != None): 
        aux=p[indi]
        v1 = grafo.vertices[aux]
        v2 = grafo.vertices[indi]
        arista = grafo.buscar_arista(v1, v2)  # Obtener la arista entre los nodos
        arista.repaint(ft.Colors.AMBER_200) # Resaltar la arista en amarillo
        indi=aux

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
                    
    v_inicial = vertices_contaminados[0]  # Vértice inicial para el recorrido

    for i in vertices_contaminados:
        if i != v_inicial:
            #Resaltar el camino más corto
            nodo_act = i  # Nodo actual
            while nodo_act != v_inicial:  # Mientras no lleguemos al nodo inicial
                nodo_pre = pre[v_inicial][nodo_act]  # Predecesor del nodo actual
                grafo.buscar_arista(grafo.vertices[nodo_pre], grafo.vertices[nodo_act]).repaint(ft.Colors.AMBER_200)  # Resaltar la arista en amarillo
                nodo_act = nodo_pre  # Actualizar el nodo actual
            
            time.sleep(0.5)  # Pausa para visualizar el paso a paso
        
def buscar_componente(v2, componentes):
    for c2 in componentes:
        if v2 in c2:
            return c2

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

def screen_main(page : ft.Page,  i=1, etapa="etapa2"):
    
    page.title = "Visual Graph"
    page.vertical_alignment = ft.MainAxisAlignment.END

    page.window.width = 900
    page.window.height = 700
    page.bgcolor = ft.Colors.WHITE
    page.window.resizable = False
    
    audio1 = ft.Audio(
        src=r"C:\Users\Viridiana\Downloads\proyecto2ED-version2_21\desafios.mp3",
        autoplay=False,
    )
    page.overlay.append(audio1)

    is_playing = ft.Ref[bool]()
    is_playing.current = False

    play_pause_button = ft.ElevatedButton(
        text=".",
        icon=ft.icons.PLAY_ARROW,
    )

    def toggle_audio(e):
        if is_playing.current:
            audio1.pause()
            play_pause_button.icon = ft.icons.PLAY_ARROW
        else:
            audio1.play()
            play_pause_button.icon = ft.icons.PAUSE
        is_playing.current = not is_playing.current
        page.update()

    play_pause_button.on_click = toggle_audio

    def actualiza_pregunta(j, etapa):
        
        if etapa == "etapa2":
            if j == 1: 
               nom_desafio.content =  ft.Text(
                "1.	Desafío:  ¿Qué algoritmo emplearía para identificar la zona contaminada más cercana a partir del nodo V1?.",
                size=14, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
                )
            elif j == 2:
               nom_desafio.content =  ft.Text(
                "2.	Desafío: Seleccione cuál de los siguientes métodos usaría para encontrar la ruta más corta para transportar los residuos a los centros de reciclaje.",
                size=14, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
                )
            elif j == 3: 
                nom_desafio.content= ft.Text(
                "3.	Si es un bosque denso, ¿qué algoritmo utilizarías?",
                size=14, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
            )      
        elif etapa == "etapa3":
            if j == 1: 
                nom_desafio.content = ft.Text(
                "1.	Desafío: Indique cuál algoritmo utilizaría para encontrar la zona contaminada más lejana desde V1.",
                size=16, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
                )
            elif j == 2:
                nom_desafio.content = ft.Text(
            "2.	Desafío: ¿Qué método utilizaría para determinar la ruta más corta para transportar los residuos de una zona contaminada a otra zona contaminada?.",
                size=16, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
                )
            elif j == 3: 
                nom_desafio.content =  ft.Text(
                "3. Si es un bosque disperso, ¿qué algoritmo utilizarías?",
                size=16, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
                )
        page.update()
    
   
    def go_to_menu(e):
        if is_playing.current:
            audio1.pause()  # Detenemos el audio
        # Guardar que la etapa 2 fue completada
        etapa_terminada = "etapa2_terminada" if etapa == "etapa2" else "etapa3_terminada"
        page.session.set(etapa_terminada, True)
        page.clean()
        menu_screen.screen_menu(page)  # Regresar al menú

    def go_to_validar(e):
        nonlocal i
        validar_respuesta(e,i)
        page.update()
    

    def next_instruction(e):
        nonlocal i
        if i < 3:
            i += 1
            actualiza_pregunta(i, etapa)
        boton_siguiente.visible = False
        reiniciar()
        page.update()
  
    def prev_instruction(e):
        nonlocal i
        if i > 1:
            i -= 1
            actualiza_pregunta(i, etapa)
        page.update()
    
    # Crear componentes que se actualizarán
    nom_desafio = ft.Container(
        width=900,
        height=60,
        bgcolor="#b5cb59",  # Color de fondo del recuadro
        padding=6,  # Espacio dentro del recuadro
        border=ft.border.all(1, "black"),  # Borde negro de 2px
        border_radius=10,  # Bordes redondeados
        alignment=ft.alignment.center  # Centrar el texto dentro del recuadro
    )
    
    
    done=True
    boton_siguiente = ft.ElevatedButton("Siguiente", on_click=next_instruction, bgcolor="#b5cb59", color="white")
    boton_terminar = ft.FilledButton("Terminar", bgcolor="#b5cb59", color="white", on_click=go_to_menu)

    boton_siguiente.visible = False
    boton_terminar.visible = False
    def validar_respuesta(e,i):
        if etapa == "etapa2":
            if e.control.text == respuestas_correctas_etapa2[i]:
                alert = ft.AlertDialog(True, ft.Text("Correcto"), ft.Text("Felicidades!"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
                e.page.open(alert)
                if i == 1:
                    boton_siguiente.visible = True
                    boton_terminar.visible = False
                    recorrido_anchura(e)
                elif i == 3:
                    boton_siguiente.visible = False
                    boton_terminar.visible = True
                    act_prim(e)
                elif i==2:
                    boton_siguiente.visible = True
                    boton_terminar.visible = False
                    dijkstra(grafo.matriz_costos(), vertices_contaminados)  # Llamar a Dijkstra con la matriz de pesos y los nodos reciclables
            else:
                alert = ft.AlertDialog(True, ft.Text("Incorrecto"), ft.Text("Intenta de nuevo"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
                e.page.open(alert)
                if i == 1:
                    boton_siguiente.visible = False
                    boton_terminar.visible = False
                elif i == 3:
                    boton_siguiente.visible = False
                    boton_terminar.visible = False
                elif i==2:
                    boton_siguiente.visible = False
                    boton_terminar.visible = False
        elif etapa == "etapa3":
            if e.control.text == respuestas_correctas_etapa3[i]:
                alert = ft.AlertDialog(True, ft.Text("Correcto"), ft.Text("Felicidades!"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
                e.page.open(alert)
                if i == 1:
                    boton_siguiente.visible = True
                    boton_terminar.visible = False
                    recorrido_profundidad(e)
                    print("Ejecutando profundidad")
                elif i==2:
                    boton_siguiente.visible = True
                    boton_terminar.visible = False
                    floyd(grafo.matriz_costos())
                elif i == 3:
                    boton_siguiente.visible = False
                    boton_terminar.visible = True
                    act_kruskal(e)
                
                    
                # Después de cualquier cambio de visibilidad:
                boton_siguiente.update()
                boton_terminar.update()
                    
            else:
                alert = ft.AlertDialog(True, ft.Text("Incorrecto"), ft.Text("Intenta de nuevo"),[ft.TextButton("Aceptar",on_click=lambda e: e.page.close(alert))])
                e.page.open(alert)
                if i == 1:
                    boton_siguiente.visible = False
                    boton_terminar.visible = False
                elif i == 3:
                    boton_siguiente.visible = False
                    boton_terminar.visible = False
                elif i==2:
                    boton_siguiente.visible = False
                    boton_terminar.visible = False
        
    actualiza_pregunta(i,etapa)
    
    
    instrucciones = ft.Text(
                    "Carga el grafo a tu elección o dibuja uno \n"
                    "y por cada pregunta elige el botón \n"
                    "correcto.",
                    color="Black", 
                    size=11, 
                    no_wrap=False, 
                )
        
    contenedor=ft.Container(content=instrucciones,expand=False)
        
    # Agregarlos a una fila (uno al lado del otro)
    fila_botones = ft.Row(
        controls=[
            boton_siguiente,
            boton_terminar],
        alignment=ft.MainAxisAlignment.CENTER  # Opcional, para centrar los botones
    )


    page.add(
    ft.Column(
        [   
            nom_desafio,
            fila_botones
        ]
        ),
    ft.Container(width=10, height=0)
    )

    page.add(
        ft.Column(
            controls=[
                play_pause_button
            ],
        )
    )

    page.add(
        ft.Row(
            [
                ft.Container(
                    bgcolor=ft.Colors.BLUE_50,
                    width=650,
                    height=525,
                    content=workarea
                ), 

                ft.Column(
                    [
                        
                        ft.Text("Instrucciones",size=20,bgcolor=ft.Colors.INDIGO_100,weight=ft.FontWeight.BOLD,italic=True), 
                        contenedor, 
                        ft.Text("Ejecutar Algoritmo",color="BLACK"), 
                        ft.FilledTonalButton(text="Algoritmo Kruskal",bgcolor=ft.Colors.INDIGO_500,on_click=go_to_validar),
                        ft.FilledTonalButton(text="Algoritmo Prim",bgcolor=ft.Colors.INDIGO_500,on_click=go_to_validar), 
                        ft.FilledTonalButton(text="Algoritmo Dijkstra",bgcolor=ft.Colors.INDIGO_500,on_click=go_to_validar),
                        ft.FilledTonalButton(text="Algoritmo Floyd",bgcolor=ft.Colors.INDIGO_500,on_click=go_to_validar),
                        ft.FilledTonalButton(text="Recorrido Anchura",bgcolor=ft.Colors.INDIGO_500,on_click=go_to_validar),
                        ft.FilledTonalButton(text="Recorrido Profundidad",bgcolor=ft.Colors.INDIGO_500,on_click=go_to_validar),
                        texto_distancia
                    ]
                    
                )
            ]
        
        )

    )

    page.update()
    page.update()

    global grafo
    
    vertices_contaminados.clear()  # Limpiar la lista de contaminados
    vertices_no_contaminados.clear()  # Limpiar la lista de no contaminados
    
    #dependiendo del nivel saldra el grafo 1 o 2 
    if etapa == "etapa2": 
        grafo = cargar_grafo("grafo1", workarea)  # Cargar el grafo desde un archivo aleatorio en el directorio
    else: 
        grafo = cargar_grafo("grafo2", workarea)
    
    if grafo is None:
        alert = ft.AlertDialog(True, ft.Text("Error"), ft.Text("No se pudo cargar el grafo"), [ft.TextButton("Aceptar", on_click=lambda e: e.page.close(alert))])
        page.open(alert)
        return
    
    for vertice in grafo.vertices:
        vertice.set_on_click(presionar_boton_vertice)
        if vertice.contaminado:
            vertices_contaminados.append(grafo.vertices.index(vertice))  # Guardar el índice del vértice contaminado
        else:
            vertices_no_contaminados.append(grafo.vertices.index(vertice))  # Guardar el índice del vértice no contaminado
        workarea.controls.append(vertice.boton)  # Agregar el botón al área de trabajo
    
    workarea.update()  # Refrescar el área de trabajo

   
    
if __name__ == "__main__":
    ft.app(screen_main)