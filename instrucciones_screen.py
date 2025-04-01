import flet as ft
import flet.canvas as cv

def screen_menu(page: ft.Page):
    page.title = "Instrucciones"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#e9ffc3'
    page.window.resizable = False
    op=1  #numero de desafio provisional
    i=1 #indice provisional

    #Desafios del nivel: 1=BFS y DSF, 2=Dijstrak y Floys, 3=Prim y Kruskal
    #(checar como mando el numero del desafio para aca, op es el numero de desafio)
    if op == 1:
        nom_desafio =  ft.Container(
            ft.Text(
                "Exploración de Ecosistemas",
                color="Black", 
                size=20, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
                ),
            bgcolor="#b5cb59",  # Color de fondo del recuadro
            padding=10,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center  # Centrar el texto dentro del recuadro
        )
        instrucciones= ft.Container(
            
            content=ft.Text(
                "BFS: Se utiliza para encontrar la zona contaminada más cercana.\n\n"
                "DFS: Se utiliza para explorar a fondo una zona para así identificar problemas más extensos.\n", 
                
                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False
            ),
            bgcolor="#c7ec99",  # Color de fondo del recuadro
            padding=25,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center  # Centrar el texto dentro del recuadro
        )    
        
    elif op == 2:
        nom_desafio =  ft.Container(
            ft.Text(
                "Optimización de Rutas de Recolección",
                color="Black", 
                size=20, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
                ),
            bgcolor="#b5cb59",  # Color de fondo del recuadro
            padding=10,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center  # Centrar el texto dentro del recuadro
        )
        instrucciones= ft.Container(
            
            content=ft.Text(
                "DIJKSTRA: Se utiliza para encontrar la ruta más corta entre un punto especifico y una zona contaminada. "
                "Útil si la contaminación es dispersa.\n\n"
                "FLOYD - WARSHALL: Se utiliza para encontrar las rutas más cortas entre todas las estaciones de recolección. "
                "Útil si hay varias zonas contaminadas conectadas entre sí.\n", 
                
                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False
            ),
            bgcolor="#c7ec99",  # Color de fondo del recuadro
            padding=25,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center  # Centrar el texto dentro del recuadro
        )
            
    elif op == 3:
        nom_desafio =  ft.Container(
            ft.Text(
                "Diseño de Redes Ecológicas",
                color="Black", 
                size=20, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False 
                ),
            bgcolor="#b5cb59",  # Color de fondo del recuadro
            padding=10,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center  # Centrar el texto dentro del recuadro
        )
        instrucciones= ft.Container(
            
            content=ft.Text(
                "PRIM: Se utiliza si se tiene un bosque denso, es decir, si las conexiones entre las zonas son numerosas.\n\n"
                "KRUSKAL: Se utiliza si se tiene un bosque disperso, es decir, si las zonas están muy esparcidas y hay pocos caminos.\n", 
                
                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                no_wrap=False
            ),
            bgcolor="#c7ec99",  # Color de fondo del recuadro
            padding=25,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center  # Centrar el texto dentro del recuadro
        )    
        
    else:
        instrucciones = None # No hacer nada si no hay nivel seleccionado


    #Solo agregar el contenedor si hay instrucciones
    contenedor_instrucciones = ft.Container(content=instrucciones, expand=False) if instrucciones else None
    #Agrega al contenedor el nombre del desafío
    contenedor_desafio = ft.Container(content=nom_desafio)
    
    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "INSTRUCCIONES",
                    size=28,
                    bgcolor='#93A267',
                    color='#FBFBFB', 
                    weight=ft.FontWeight.BOLD,
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(" "), 
                #Texto que indica el nivel en el que se encuentre (cómo se pasa el indice del nivel?)
                ft.Text(
                    f"NIVEL {i}",
                    size=24,
                    bgcolor='#b5c732',
                    color='#FBFBFB', 
                    weight=ft.FontWeight.BOLD,
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                    ), 
                ft.Text(" "),
                contenedor_desafio,
                contenedor_instrucciones, #llama al contenedor con las instrucciones
                ft.Text(" "),

            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinear el contenido al centro
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar los botones horizontalmente
        ),
        alignment=ft.alignment.center,  # Centrar el contenedor en la columna
        padding=20,
    )
    
    #Se asignan los espacios para las columnas
    column1 = ft.Column([], expand=2,)
    column2 = ft.Column([content_container], alignment=ft.MainAxisAlignment.CENTER, expand=6)
    column3 = ft.Column([], expand=2)

    # Agregar el diseño a la página
    page.add(
        ft.Row(
            [column1, column2, column3],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ) 
    )
    page.update()

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(screen_menu)