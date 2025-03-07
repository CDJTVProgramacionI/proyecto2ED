import flet as ft
import flet.canvas as cv


canvas = cv.Canvas(width=100, height=100)
campo_peso = ft.TextField(label="Peso", width=70, height=40, color=ft.Colors.BLUE_400)

def presionar_boton_arista(e):
    genera_arista([10,20],[40,30])
    
def genera_arista(inicio_coord,fin_coord): 
   paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE) 
   THE_LINE=cv.Line(inicio_coord[0],inicio_coord[1],fin_coord[0],fin_coord[1], paint)
   puntomed_x = (inicio_coord[0]+fin_coord[0])/2
   puntomed_y = (inicio_coord[1]+fin_coord[1])/2
   texto=cv.Text(puntomed_x,puntomed_y, campo_peso.value,ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_500, size=14))
  
   canvas.shapes.append(THE_LINE) #mybodysonthelinenowicantfightthistimenowicanfeel
   canvas.shapes.append(texto)
   canvas.update()

def screen_main(page : ft.Page):
    page.title = "Visual Graph"
    page.vertical_alignment = ft.MainAxisAlignment.END

    page.window.width = 900
    page.window.height = 700
    page.bgcolor = ft.Colors.WHITE
    page.window.resizable = False
    
    
    page.add(
        ft.Row(
            [
                ft.FilledButton(
                    text="Generar Arista",
                    disabled=False,bgcolor=ft.Colors.BLUE_50,
                    color=ft.Colors.BLUE_400,
                    on_click=presionar_boton_arista),
                
                campo_peso,        
            ]
        ),
        ft.Container(width=10,height=25,)

    )
    
    page.add(
       ft.Container(
           bgcolor=ft.Colors.BLUE_50,
           width=650,
           height=525,
           content=canvas
        )
    )
    
if __name__ == "__main__":
    ft.app(screen_main)