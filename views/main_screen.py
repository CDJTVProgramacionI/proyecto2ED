import flet as ft

def screen_main(page : ft.Page):
    page.title = "Visual Graph"
    page.vertical_alignment = ft.MainAxisAlignment.END

    page.window.width = 900
    page.window.height = 700
    page.bgcolor = ft.Colors.WHITE
    page.window.resizable = False
    
    page.add(
       ft.Container(
           bgcolor=ft.Colors.BLUE_50,
           width=650,
           height=525
       ) 
    )
    
if __name__ == "__main__":
    ft.app(screen_main)