import flet as ft
import flet.canvas as cv

def certificado(page: ft.Page, nombre: str):
    page.title = "Visual Graph"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#FBFBFB'
    page.window.resizable = False
    
    page.clean()
    
    btn_volver = ft.FilledButton(
        text="Regresar", bgcolor='#CADBB7', color='#485935', width=200, height=40,
        on_click=lambda _: go_to_menu(page)  # Cambia a la función de menú
    )

    imagen = ft.Image(
        src=f"Imagenes/certificado.jpg",
        fit=ft.ImageFit.FILL,
        width=900,
        height=600
    )

    texto_nombre = ft.Text(
        nombre, size=30, color="black", weight=ft.FontWeight.BOLD
    )

    contenedor = ft.Stack(
        [
            imagen,
            ft.Container(
                content=texto_nombre,
                alignment=ft.alignment.center,  
                width=900,
                height=700
            ),
            btn_volver
        ],
        width=900,
        height=700
    )

    page.add(contenedor)
    page.update()
    
def go_to_menu(page : ft.Page):
    import menu_screen
    page.clean()
    menu_screen.screen_menu(page)  # Regresar al menú