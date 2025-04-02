import flet as ft
import main_screen
import certificado
import screen_nombre 
import flet.canvas as cv

def screen_menu(page: ft.Page):
    page.title = "Visual Graph"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#EAF0E4'
    page.window.resizable = False

    gif=ft.Image(
        src="https://img1.picmix.com/output/stamp/normal/1/1/1/2/1472111_5d9ae.gif",
        width=900,
        height=700, 
        fit=ft.ImageFit.COVER
    )

    #Definimos checkbox para cada boton en caso de terminar el nivel 
    checkbox1= ft.Checkbox(value=False, disabled=True,check_color="#697A55")
    checkbox2= ft.Checkbox(value=False, disabled=True,check_color="#697A55")
    checkbox3= ft.Checkbox(value=False, disabled=True,check_color="#697A55")
    checkbox4= ft.Checkbox(value=False, disabled=True,check_color="#697A55")
    checkbox5= ft.Checkbox(value=False, disabled=True,check_color="#697A55")
    checkbox6= ft.Checkbox(value=False, disabled=True,check_color="#697A55")
    checkbox7= ft.Checkbox(value=False, disabled=True,check_color="#697A55")

  
    def go_to_main(e): 
        page.clean()
        main_screen.screen_main(page)

    def go_to_nombre(e): 
        page.clean()
        screen_nombre.screen_nombre(page)

    def completar_nivel(e):
        import time
        time.sleep(1)  #Pasar la funcion que valida el nivel 
        checkbox1.value = True
        page.update()

    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Guardián del bosque",
                    size=18,
                    bgcolor='#93A267',
                    color='#FBFBFB', 
                    weight=ft.FontWeight.BOLD,
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(" "), 
                ft.Row([
                    ft.FilledButton(text="Etapa 1",  bgcolor='#CADBB7', color='#485935', width=180,height=65,on_click=go_to_main),
                    checkbox1,
                ], alignment=ft.MainAxisAlignment.CENTER), 
                ft.Row([
                    ft.FilledButton(text="Etapa 2", bgcolor='#CADBB7', color='#485935', width=180,height=65,on_click=go_to_main),
                    checkbox2,
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.FilledButton(text="Etaopa 3", bgcolor='#CADBB7', color='#485935', width=180,height=65,on_click=go_to_main),
                    checkbox3,
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Text(" "), 
                ft.FilledButton(text="Certificado", bgcolor='#CADBB7', color='#485935', width=180,height=60,on_click=go_to_nombre),
                gif, 
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinear el contenido al centro
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar los botones horizontalmente
        ),
        alignment=ft.alignment.center,  # Centrar el contenedor en la columna
        padding=20,
    )

    column1 = ft.Column([], expand=True,)
    column2 = ft.Column([content_container], alignment=ft.MainAxisAlignment.CENTER, expand=1)
    column3 = ft.Column([], expand=True)

    # Agregar el diseño a la página
    page.add(
        ft.Row(
            [column1, column2, column3],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ), 
        gif, 
    )
    page.update()

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(screen_menu)