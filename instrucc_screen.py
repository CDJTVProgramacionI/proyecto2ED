import flet as ft
import flet.canvas as cv
import menu_screen


def screen_instrucciones(page: ft.Page, i=1):
    page.title = "Instrucciones"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#e9ffc3'
    page.window.resizable = False

    
    def actualiza_instructions(i):
        if i == 1: 
            nom_desafio.content = ft.Text(
                "1. Desafío: 'Compresión de Exploración de Ecosistemas'",
                color="Black", 
                size=20, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            )
            instrucciones.content = ft.Text(
                "Para identificar y recorrer eficientemente las zonas contaminadas que hay en el bosque y así poder planificar la recolección de residuos se utilizan dos tipos de recorrido:\n\n"
                "   -Recorrido a lo ancho (BFS): Nos permite encontrar dentro del bosque la zona contaminada más cercana a un centro de reciclaje.\n"
                "   -Recorrido a lo profundo (DFS): Nos permite explorar a fondo cada zona para así poder detectar problemas más extensos. Es útil para encontrar, desde un centro de reciclaje, la zona contaminada que se está ubicada en la parte más profunda del bosque.\n\n"
                "*Nota:\n"
                "Grafo: Representa el bosque.\n" 
                "Nodos naranjas: Representa las zonas contaminadas/estaciones de recolección que hay en el bosque.\n"
                "Nodos azules: Representa los centros de reciclaje dentro del bosque.",
                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD
            )
            
        elif i == 2:
            nom_desafio.content = ft.Text(
                "2. Desafío: 'Compresión de Optimización de Rutas de Recolección'",
                color="Black", 
                size=20, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            )
            instrucciones.content = ft.Text(
                "Para determinar la mejor ruta, es decir, la ruta que esté a menor distancia, para transportar residuos a un centro de reciclaje se usan los algoritmos:\n\n" 
                "   -Floyd: Nos permite encontrar la ruta más corta entre las estaciones de recolección del bosque. Útil en caso de existencia de varias zonas contaminadas conectadas entre sí.\n"
                "   -Dijkstra: Nos permite encontrar la zona contaminada más cercana desde una zona contaminada o no contaminada. Útil en caso de existencia de contaminación dispersa.",
                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD
            )
            
        elif i == 3: 
            nom_desafio.content = ft.Text(
                "3. Desafío: 'Comprensión de Diseño de Redes Ecológicas'",
                color="Black", 
                size=20, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            )
            instrucciones.content = ft.Text(
                "Para la construcción de sistemas eficientes de estaciones de reciclaje con la menor cantidad de recursos o tiempo de viaje entre estas, usamos los métodos:\n\n"
                "   -Prim: Se utiliza cuando es un bosque denso.\n"
                "   -Kruskal: Se utiliza cuando es un bosque disperso. \n\n"
                "*Nota:\n"
                "Bosque denso: Las conexiones entre zonas son numerosas.\n"
                "Bosque disperso: Las zonas están muy dispersas y hay pocos caminos.\n",
                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD
            )
            
        etapa_text.value = f"ETAPA {i}"
        
        #botones según la etapa
        if i == 1:
            boton_anterior.visible = False
            boton_siguiente.visible = True
            boton_terminar.visible = False
        elif i == 3:
            boton_anterior.visible = True
            boton_siguiente.visible = False
            boton_terminar.visible = True
        else:
            boton_anterior.visible = True
            boton_siguiente.visible = True
            boton_terminar.visible = False
            
        page.update()
        
    def go_to_menu(e):
        # Guardar que la etapa 1 fue completada
        page.session.set("etapa1_terminada", True)
        page.clean()
        menu_screen.screen_menu(page)  # Regresar al menú
       
    def next_instruction(e):
        nonlocal i
        if i < 3:
            i += 1
            actualiza_instructions(i)
    
    def prev_instruction(e):
        nonlocal i
        if i > 1:
            i -= 1
            actualiza_instructions(i)
    
    # Crear componentes que se actualizarán
    nom_desafio = ft.Container(
        bgcolor="#b5cb59",
        padding=10,
        border=ft.border.all(2, "black"),
        border_radius=10,
        alignment=ft.alignment.center
    )
    
    instrucciones = ft.Container(
        bgcolor="#c7ec99",
        padding=25,
        border=ft.border.all(2, "black"),
        border_radius=10,
        alignment=ft.alignment.center
    )
    
    etapa_text = ft.Text(
        size=28,
        bgcolor='#93A267',
        color='#FBFBFB', 
        weight=ft.FontWeight.BOLD,
        italic=True,
        text_align=ft.TextAlign.CENTER,
    )
    done=True
    boton_anterior = ft.ElevatedButton("Anterior", on_click=prev_instruction, bgcolor="#b5cb59", color="white")
    boton_siguiente = ft.ElevatedButton("Siguiente", on_click=next_instruction, bgcolor="#b5cb59", color="white")
    boton_terminar = ft.FilledButton("Terminar", bgcolor="#b5cb59", color="white", on_click=go_to_menu)
    
    #
    botones = ft.Row(
        [
            boton_anterior,
            boton_siguiente,
            boton_terminar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )
    
    
    actualiza_instructions(i)
    
    content_container = ft.Container(
        content=ft.Column(
            [
                etapa_text,
                ft.Text(" "), 
                nom_desafio,
                instrucciones,
                ft.Text(" "),
                botones, 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        padding=20,
    )
    
    page.add(
        ft.Row(
            [ft.Column([content_container], expand=True)],
            alignment=ft.MainAxisAlignment.CENTER,
        ) 
    )
    
    page.update()


if __name__ == "__main__":
    ft.app(screen_instrucciones)