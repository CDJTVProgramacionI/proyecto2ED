import flet as ft
from certificado import certificado  # Importa solo la función certificada

def screen_nombre(page: ft.Page):
    page.title = "Visual Graph"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#f8fff6'
    page.window.resizable = False
    
    nombre_usuario = ft.TextField(label="Nombre", width=600, height=50, color='#93A267')
    
    btn_certificado = ft.FilledButton(
        text="Generar Certificado", bgcolor='#CADBB7', color='#485935', width=200, height=40,
        on_click=lambda _: certificado(page, nombre_usuario.value)  # Llamada a la función certificada con el nombre
    )
    
    page.clean()
    page.add(
        ft.Column([
            ft.Text("Guardian del bosque", size=18, bgcolor='#93A267', color='#FBFBFB', weight=ft.FontWeight.BOLD),
            nombre_usuario,
            btn_certificado
        ], alignment=ft.MainAxisAlignment.CENTER)
    )
    page.update()

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=screen_nombre)
