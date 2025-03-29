import flet as ft
import flet.canvas as cv

def screen_menu(page: ft.Page):
    page.title = "Visual Graph"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#FBFBFB'
    page.window.resizable = False

    gif=ft.Image(
        src="https://img1.picmix.com/output/stamp/normal/1/1/1/2/1472111_5d9ae.gif",
        width=900,
        height=700, 
        fit=ft.ImageFit.COVER
    )

    nombre_usuario= ft.TextField(label="Nombre", width=600, height=50, color='#93A267')

    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Guardian del bosque",
                    size=18,
                    bgcolor='#93A267',
                    color='#FBFBFB', 
                    weight=ft.FontWeight.BOLD,
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(" "), 
                nombre_usuario, 
                ft.FilledButton(text="Nivel 1",  bgcolor='#CADBB7', color='#485935', width=200,height=40),
                ft.FilledButton(text="Nivel 2", bgcolor='#CADBB7', color='#485935', width=200,height=40),
                ft.FilledButton(text="Nivel 3", bgcolor='#CADBB7', color='#485935', width=200,height=40),
                ft.FilledButton(text="Nivel 4", bgcolor='#CADBB7', color='#485935', width=200,height=40),
                ft.FilledButton(text="Nivel 5", bgcolor='#CADBB7', color='#485935', width=200,height=40),
                ft.FilledButton(text="Nivel 6", bgcolor='#CADBB7', color='#485935', width=200,height=40),
                ft.FilledButton(text="Nivel 7", bgcolor='#CADBB7', color='#485935', width=200,height=40),
                ft.FilledButton(text="Certificado", bgcolor='#CADBB7', color='#485935', width=200,height=40),
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