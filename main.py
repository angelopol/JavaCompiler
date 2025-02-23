import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import lex

def main(page: Page):
    page.title = "Compilador de Java-Python"
    page.window_width = 600
    page.window_height = 670
    page.window_resizable = False
    page.window_center()
    page.padding = 0


    item1 = []
    item2 = []
    item3 = []

    textArea1 = ft.TextField(label="Codigo Java", multiline=True,width=500)
    executeButton = ft.ElevatedButton(text="Analizar",disabled=True)
    textArea2 = ft.TextField(label="Resultado", value="Line    Type                Value           Position\n",multiline=True,read_only=True,width=500)
    item1.append(textArea1)
    item2.append(executeButton)
    item3.append(textArea2)
    row1 = ft.Row(spacing=10, controls=item1)
    row2 = ft.Row(spacing=10, controls=item2)
    row3 = ft.Row(spacing=10, controls=item3)

    def validate(e: ft.ControlEvent)->None:
        if textArea1.value == "":
            executeButton.disabled = True
        else:
            executeButton.disabled = False
        page.update()

    def executeLex(e: ft.ControlEvent)->None:
        cadena = ""
        for i in range(len(lex.execute(textArea1.value))):
            cadena += lex.execute(textArea1.value)[i]
        textArea2.value += cadena
        page.update()

    textArea1.on_change = validate
    executeButton.on_click = executeLex

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        #Menu
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Menú'),bgcolor = 'blue'), #Barra superior
                    Text(value = 'Compilador\nSamuel Molina y Angelo Polgrossi',size = 30,text_align="CENTER"), #Funciona como una etiqueta
                    ElevatedButton(text='  Analizador Lexico  ', on_click=lambda _: page.go('/lex'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        #Pagina Gauss Seidel
        if page.route == '/lex':
            page.views.append(
                View(
                    route='/lex',
                    controls=[
                        AppBar(title=Text('Analizador Lexico'),bgcolor = 'blue'),
                        Text(value = 'Analizador Lexico',size = 30),
                        row1,
                        row2,
                        row3
                        #ElevatedButton(text='Regresar a menu', on_click=lambda _: page.go('/'))#Boton que va en el borde superior
                    ],
                    vertical_alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=20,
                    
                )
            )
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)
    #page.add(contenedor)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)