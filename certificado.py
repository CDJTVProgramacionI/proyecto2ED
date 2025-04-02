import flet as ft
import flet.canvas as cv

def certificado(page: ft.Page, nombre: str):
    page.title = "Visual Graph"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#FBFBFB'
    page.window.resizable = False

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
            )
        ],
        width=900,
        height=700
    )

    page.add(contenedor)
    page.update()
