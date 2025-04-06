import flet as ft
import main_screen
import screen_nombre
import instrucc_screen
import main_et_1
import flet.canvas as cv

def screen_menu(page: ft.Page):
    page.title = "Visual Graph"
    page.window.width = 900
    page.window.height = 700
    page.bgcolor = '#EAF0E4'
    page.window.resizable = False

    gif=ft.Image(
        src="https://img1.picmix.com/output/stamp/normal/1/1/1/2/1472111_5d9ae.gif",
        width=200,
        height=280, 
        fit=ft.ImageFit.COVER
    )

    #Definimos checkbox para cada boton en caso de terminar el nivel 
    etapa1_completa = page.session.get("etapa1_terminada") == True
    etapa2_completa = page.session.get("etapa2_terminada") == True
    etapa3_completa = page.session.get("etapa3_terminada") == True
    # Checkbox para etapa 1
    checkbox1 = ft.Checkbox(
        value=etapa1_completa,
        disabled=True,
        check_color="#697A55",
        fill_color="#CADBB7" if etapa1_completa else "#cccccc")
    checkbox2 = ft.Checkbox(
        value=etapa2_completa,
        disabled=True,
        check_color="#697A55",
        fill_color="#CADBB7" if etapa1_completa else "#cccccc")
    checkbox3 = ft.Checkbox(
        value=etapa3_completa,
        disabled=True,
        check_color="#697A55",
        fill_color="#CADBB7" if etapa1_completa else "#cccccc")
    
    tree=ft.Image(
        src="https://openclipart.org/image/2400px/svg_to_png/215526/PixelTree.png", 
        width=200, 
        height=280, 
        fit=ft.ImageFit.COVER
    )

    def go_to_et_1(e): 
        if is_playing.current:
            audio1.pause()  # Detenemos el audio
        page.clean()
        main_et_1.screen_main(page,1,"etapa2")
        
    def go_to_et_2(e): 
        if is_playing.current:
            audio1.pause()  # Detenemos el audio
        page.clean()
        main_et_1.screen_main(page,1,"etapa3")

    def go_to_main(e):
        if is_playing.current:
            audio1.pause()  # Detenemos el audio 
        page.clean()
        main_screen.screen_main(page)

    def go_to_nombre(e):
        if is_playing.current:
            audio1.pause()  # Detenemos el audio
        page.clean()
        screen_nombre.screen_nombre(page)

    def go_to_instrucc(e): 
        if is_playing.current:
            audio1.pause()  # Detenemos el audio
        global cb1
        cb1=True
        page.clean()
        instrucc_screen.screen_instrucciones(page)
    
    def completar_nivel(e):
        import time
        time.sleep(1)  #Pasar la funcion que valida el nivel 
        checkbox1.value = True
        page.update()
        page.session["etapa1_terminada"] = True  # Guardar el estado de la etapa en la sesión

    image_container= ft.Container(
        content=tree, 
        alignment=ft.alignment.center,  # Asegura el centrado
        expand=True,
    )


    audio1 = ft.Audio(
        src=r"C:\Users\Viridiana\Downloads\proyecto2ED-version2_21\menu.mp3",  # La ruta al archivo local
        autoplay=False,
    )
    page.overlay.append(audio1)

    is_playing = ft.Ref[bool]()
    is_playing.current = False

    play_pause_button = ft.ElevatedButton(
        icon=ft.icons.PLAY_ARROW,
        text=" ", 
        bgcolor='#CADBB7', 
        color='#485935' 
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

    page.add(
        ft.Column(
            controls=[
                play_pause_button
            ],
        )
    )

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
                    ft.FilledButton("Etapa 2", bgcolor='#CADBB7', color='#485935', width=180, height=65, on_click=go_to_et_1),
                    checkbox2
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.FilledButton("Etapa 3", bgcolor='#CADBB7', color='#485935', width=180, height=65, on_click=go_to_et_2),
                    checkbox3
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.FilledButton(text="Mapa libre", bgcolor='#CADBB7', color='#485935', width=180,height=65,on_click=go_to_main),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Text(" "), 
                ft.FilledButton(text="Certificado", bgcolor='#CADBB7', color='#485935', width=180,height=60,on_click=go_to_nombre, visible=etapa1_completa and etapa2_completa and etapa3_completa),
                gif, 
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinear el contenido al centro
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar los botones horizontalmente
        ),
        alignment=ft.alignment.center,  # Centrar el contenedor en la columna
        padding=20,
    )

    column1 = ft.Column([image_container], alignment=ft.MainAxisAlignment.CENTER,expand=True,)
    column2 = ft.Column([content_container], alignment=ft.MainAxisAlignment.CENTER, expand=1)
    column3 = ft.Column([image_container], alignment=ft.MainAxisAlignment.CENTER,expand=True)

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