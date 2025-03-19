import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import lex

def main(page: Page):
    page.title = "Compilador de Java-Python"
    page.window_resizable = True
    page.window_center()
    page.padding = 10

    textArea1 = ft.TextField(label="Codigo Java", multiline=True)
    resultTable = ft.DataTable(
        columns=[
            ft.DataColumn(label=Text("Line")),
            ft.DataColumn(label=Text("Type")),
            ft.DataColumn(label=Text("Value")),
            ft.DataColumn(label=Text("Position")),
        ],
        rows=[],
        expand=True
    )

    # Usar ListView para habilitar el scroll
    resultTableContainer = ft.ListView(
        controls=[resultTable],
        expand=True,
        height=300,  # Altura fija para habilitar el scroll
    )

    executeButton = ft.ElevatedButton(text="Analizar", disabled=True)

    def validate(e: ft.ControlEvent) -> None:
        executeButton.disabled = textArea1.value == ""
        page.update()

    def executeLex(e: ft.ControlEvent) -> None:
        result = lex.execute(textArea1.value)
        resultTable.rows.clear()
        for token in result:
            resultTable.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(Text(str(token["lineno"]))),
                    ft.DataCell(Text(token["type"])),
                    ft.DataCell(Text(token["value"])),
                    ft.DataCell(Text(str(token["lexpos"]))),
                ])
            )
        page.update()

    textArea1.on_change = validate
    executeButton.on_click = executeLex

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        # Menu
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Menú'), bgcolor='blue'),
                    Text(value='Compilador\nSamuel Molina y Angelo Polgrossi', size=30, text_align="CENTER"),
                    ElevatedButton(text='  Analizador Lexico  ', on_click=lambda _: page.go('/lex'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        # Pagina Analizador Lexico
        if page.route == '/lex':
            page.views.append(
                View(
                    route='/lex',
                    controls=[
                        AppBar(title=Text('Analizador Lexico'), bgcolor='blue'),
                        Text(value='Analizador Lexico', size=30),
                        ft.Column(
                            controls=[
                                textArea1,
                                executeButton,
                                resultTableContainer,  # Usar el ListView con scroll
                            ],
                            expand=True,
                            spacing=10
                        )
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=20,
                )
            )
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)