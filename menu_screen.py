import flet as ft
import main_screen
import screen_nombre
import instrucc_screen
import main_et_1
import flet.canvas as cv

#def main(page: ft.Page):  
#   screen_menu(page,False,False,False,False)

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
    etapa1_completa = page.session.get("etapa1_terminada") == True

    # Checkbox para etapa 1
    checkbox1 = ft.Checkbox(
        value=etapa1_completa,
        disabled=True,
        check_color="#697A55",
        fill_color="#CADBB7" if etapa1_completa else "#cccccc")
    checkbox2= ft.Checkbox(value=False, disabled=True,check_color="#697A55")
    checkbox3= ft.Checkbox(value=False, disabled=True,check_color="#697A55")
    checkbox4= ft.Checkbox(value=False, disabled=True,check_color="#697A55") 

    def go_to_et_1(e): 
        page.clean()
        main_et_1.screen_main(page,1)
        
    def go_to_et_2(e): 
        page.clean()
        main_et_1.screen_main(page,2)

    def go_to_main(e): 
        page.clean()
        main_screen.screen_main(page)

    def go_to_nombre(e): 
        page.clean()
        screen_nombre.screen_nombre(page)

    def go_to_instrucc(e): 
        global cb1
        cb1=True
        page.clean()
        instrucc_screen.screen_instrucciones(page)

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
                    ft.FilledButton(text="Etapa 1",  bgcolor='#CADBB7', color='#485935', width=180,height=65,on_click=go_to_instrucc),
                    checkbox1,
                ], alignment=ft.MainAxisAlignment.CENTER), 
                ft.Row([
                    ft.FilledButton(text="Etapa 2", bgcolor='#CADBB7', color='#485935', width=180,height=65,on_click=go_to_et_1),
                    checkbox2,
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.FilledButton(text="Etapa 3", bgcolor='#CADBB7', color='#485935', width=180,height=65,on_click=go_to_et_2),
                    checkbox3,
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.FilledButton(text="Mapa libre", bgcolor='#CADBB7', color='#485935', width=180,height=65,on_click=go_to_main),
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