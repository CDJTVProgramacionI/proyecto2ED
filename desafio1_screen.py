import flet as ft
import flet.canvas as cv


#FUNCIONES PARA CONECTAR PANTALLAS
def ir_desafio2(page: ft.Page):
    # Limpiar y cargar la pantalla 2
    page.controls.clear()
    screen_desafio2(page)


def ir_desafio3(page: ft.Page):
    # Limpiar y cargar la pantalla 3
    page.controls.clear()
    screen_desafio3(page)

#PANTALLA DE DESAFIO 1
def screen_desafio1(page: ft.Page):
    page.title = "Desafíos"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#e9ffc3'
    page.window.resizable = False
    op=2  #numero de la etapa para el desafio 1
   
    #(checar como mando el numero del desafio para aca)
    if op == 1:
        nom_desafio =  ft.Container(
            ft.Text(
                "1.	Desafío: “Compresión de Exploración de Ecosistemas” ",
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
                "Para identificar y recorrer eficientemente las zonas contaminadas que hay en el bosque y así poder planificar la recolección de residuos se utilizan dos tipos de recorrido:\n\n"
                "   -Recorrido a lo ancho (BFS): Nos permite encontrar dentro del bosque la zona contaminada más cercana a un centro de reciclaje.\n"
                "   -Recorrido a lo profundo (DFS): Nos permite explorar a fondo cada zona para así poder detectar problemas más extensos. Es útil para encontrar, desde un centro de reciclaje, la zona contaminada que se está ubicada en la parte más profunda del bosque.\n\n"
                "*Nota:\n"
                "Grafo: Representa el bosque.\n" 
                "Nodos naranjas: Representa las zonas contaminadas/estaciones de recolección que hay en el bosque.\n"
                "Nodos azules: Representa los centros de reciclaje dentro del bosque.",

                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD,
                #text_align=ft.TextAlign.CENTER,
                no_wrap=False
            ),
            bgcolor="#c7ec99",  # Color de fondo del recuadro
            padding=25,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center,  # Centrar el texto dentro del recuadro
        )    
        
    elif op == 2:
        nom_desafio =  ft.Container(
            ft.Text(
                "1.	Desafío:  Indique cuál es la zona contaminada más cercana desde la Z1.",
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
        instrucciones=  ft.Container()  # Contenedor vacío sin errores
            
    elif op == 3:
        nom_desafio = ft.Container(
            ft.Text(
                "1.	Desafío: Indique cuál es la zona contaminada más lejana desde la Z1.", 
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
        instrucciones= ft.Container()
        
    else:
        instrucciones = None # No hacer nada si no hay nivel seleccionado


    #Solo agregar el contenedor si hay instrucciones
    contenedor_instrucciones = ft.Container(content=instrucciones, expand=False) if instrucciones else None
    #Agrega al contenedor el nombre del desafío
    contenedor_desafio = ft.Container(content=nom_desafio)
    
    # Coloca Boton para navegar a otras pantallas
    boton = ft.ElevatedButton(
        "Siguiente", 
        on_click=lambda e: ir_desafio2(page),
        bgcolor="#b5cb59",  # Color de fondo
        color="white",  # Color del texto
    )
        
    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    #Texto que indica la actividad en la que se encuentre (cómo se pasa el indice de la actividad/Etapa?)
                    f"ETAPA {op}",
                    size=28,
                    bgcolor='#93A267',
                    color='#FBFBFB', 
                    weight=ft.FontWeight.BOLD,
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(" "), 
                contenedor_desafio,
                contenedor_instrucciones, #llama al contenedor con las instrucciones
                boton,  # Agrega boton para navegar

            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinear el contenido al centro
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar los botones horizontalmente
        ),
        alignment=ft.alignment.center,  # Centrar el contenedor en la columna
        padding=20,
    )
    
    #Se asignan los espacios para las columnas
    column1 = ft.Column([], expand=1,)
    column2 = ft.Column([content_container], alignment=ft.MainAxisAlignment.CENTER, expand=8)
    column3 = ft.Column([], expand=1)

    # Agregar el diseño a la página
    page.add(
        ft.Row(
            [column1, column2, column3],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ) 
    )
    page.update()
    
    
    
    
#PANTALLA DE DESAFIO 2    
def screen_desafio2(page: ft.Page):
    page.title = "Desafíos"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#e9ffc3'
    page.window.resizable = False
    op=2  #numero de la etapa para el desafio 2
   
    #(checar como mando el numero del desafio para aca)
    if op == 1:
        nom_desafio =  ft.Container(
            ft.Text(
                "2.	Desafío: “Compresión de Optimización de Rutas de Recolección” ",
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
                "Para determinar la mejor ruta, es decir, la ruta que esté a menor distancia, para transportar residuos a un centro de reciclaje se usan los algoritmos:\n\n" 
                "   -Floyd: Nos permite encontrar la ruta más corta entre las estaciones de recolección del bosque. Útil en caso de existencia de varias zonas contaminadas conectadas entre sí.\n"
                "   -Dijkstra: Nos permite encontrar la zona contaminada más cercana desde una zona contaminada o no contaminada. Útil en caso de existencia de contaminación dispersa.",

                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD,
                #text_align=ft.TextAlign.CENTER,
                no_wrap=False
            ),
            bgcolor="#c7ec99",  # Color de fondo del recuadro
            padding=25,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center,  # Centrar el texto dentro del recuadro
        )    
        
    elif op == 2:
        nom_desafio =  ft.Container(
            ft.Text(
                "2.	Desafío: Seleccione cuál de los siguientes métodos usaría para encontrar la ruta más corta para transportar los residuos a los centros de reciclaje.",
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
        instrucciones=  ft.Container()  # Contenedor vacío sin errores
            
    elif op == 3:
        nom_desafio = ft.Container(
            ft.Text(
                "2.	Desafío: Seleccione cuál de los siguientes métodos usaría para encontrar la ruta más corta para transportar los residuos a los centros de reciclaje.", 
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
        instrucciones= ft.Container()
        
    else:
        instrucciones = None # No hacer nada si no hay nivel seleccionado


    #Solo agregar el contenedor si hay instrucciones
    contenedor_instrucciones = ft.Container(content=instrucciones, expand=False) if instrucciones else None
    #Agrega al contenedor el nombre del desafío
    contenedor_desafio = ft.Container(content=nom_desafio)
    # Coloca Boton para navegar a otras pantallas
    boton = ft.ElevatedButton(
        "Siguiente", 
        on_click=lambda e: ir_desafio3(page),
        bgcolor="#b5cb59",  # Color de fondo
        color="white",  # Color del texto
    )
    
    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    #Texto que indica la actividad en la que se encuentre (cómo se pasa el indice de la actividad/Etapa?)
                    f"ETAPA {op}",
                    size=28,
                    bgcolor='#93A267',
                    color='#FBFBFB', 
                    weight=ft.FontWeight.BOLD,
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(" "), 
                contenedor_desafio,
                contenedor_instrucciones, #llama al contenedor con las instrucciones
                boton,

            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinear el contenido al centro
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar los botones horizontalmente
        ),
        alignment=ft.alignment.center,  # Centrar el contenedor en la columna
        padding=20,
    )
    
    #Se asignan los espacios para las columnas
    column1 = ft.Column([], expand=1,)
    column2 = ft.Column([content_container], alignment=ft.MainAxisAlignment.CENTER, expand=8)
    column3 = ft.Column([], expand=1)

    # Agregar el diseño a la página
    page.add(
        ft.Row(
            [column1, column2, column3],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ) 
    )
    page.update()
    
    
    
    
#PANTALLA DE DESAFIO 3
def screen_desafio3(page: ft.Page):
    page.title = "Desafíos"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#e9ffc3'
    page.window.resizable = False
    op=2  #numero de la etapa para el desafio 3
   
    ###(checar como mando el numero del desafio para aca)
    if op == 1:
        nom_desafio =  ft.Container(
            ft.Text(
                "3.	Desafío: “Comprensión de Diseño de Redes Ecológicas” ",
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
                "Para la construcción de sistemas eficientes de estaciones de reciclaje con la menor cantidad de recursos o tiempo de viaje entre estas, usamos los métodos:\n\n"
                "   -Prim: Se utiliza cuando es un bosque denso.\n"
                "   -Kruskal: Se utiliza cuando es un bosque disperso. \n\n"
                "*Nota:\n"
                "Bosque denso: Las conexiones entre zonas son numerosas.\n"
                "Bosque disperso: Las zonas están muy dispersas y hay pocos caminos.\n",

                color="Black", 
                size=16, 
                weight=ft.FontWeight.BOLD,
                #text_align=ft.TextAlign.CENTER,
                no_wrap=False
            ),
            bgcolor="#c7ec99",  # Color de fondo del recuadro
            padding=25,  # Espacio dentro del recuadro
            border=ft.border.all(2, "black"),  # Borde negro de 2px
            border_radius=10,  # Bordes redondeados
            alignment=ft.alignment.center,  # Centrar el texto dentro del recuadro
        )    
        
    elif op == 2:
        nom_desafio =  ft.Container(
            ft.Text(
                "3.	Si es un bosque denso, ¿qué algoritmo utilizarías?",
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
        instrucciones=  ft.Container()  # Contenedor vacío sin errores
            
    elif op == 3:
        nom_desafio = ft.Container(
            ft.Text(
                "3. Si es un bosque disperso, ¿qué algoritmo utilizarías?", 
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
        instrucciones= ft.Container()
        
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
                    #Texto que indica la actividad en la que se encuentre (cómo se pasa el indice de la actividad/Etapa?)
                    f"ETAPA {op}",
                    size=28,
                    bgcolor='#93A267',
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
    column1 = ft.Column([], expand=1,)
    column2 = ft.Column([content_container], alignment=ft.MainAxisAlignment.CENTER, expand=8)
    column3 = ft.Column([], expand=1)

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
    ft.app(screen_desafio1)