import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, FilePicker, FilePickerResultEvent
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import lex
import sintax  # Importar el analizador sintáctico
from gemini import compile, semantic

def main(page: Page):
    page.title = "Java-Python Compiler"
    page.window_resizable = True
    page.window_center()
    page.padding = 10
    page.scroll=ft.ScrollMode.ALWAYS

    # Text area for input
    textArea1 = ft.TextField(label="Java Code", multiline=True)
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

    # Scrollable container for the result table
    resultTableContainer = ft.ListView(
        controls=[resultTable],
        expand=True,
        height=300,  # Fixed height to enable scrolling
    )

    executeButtonLex = ft.ElevatedButton(text="Analyze Lexically", disabled=True)
    executeButtonSyntax = ft.ElevatedButton(text="Analyze Syntactically", disabled=True)
    executeButtonSemantic = ft.ElevatedButton(text="Analyze Semantically", disabled=True)
    executeButtonCompile = ft.ElevatedButton(text="Compile", disabled=True)

    # File picker for loading files
    filePicker = FilePicker()
    page.overlay.append(filePicker)

    def validate(e: ft.ControlEvent) -> None:
        executeButtonLex.disabled = textArea1.value == ""
        executeButtonSyntax.disabled = textArea1.value == ""
        executeButtonSemantic.disabled = textArea1.value == ""
        executeButtonCompile.disabled = textArea1.value == ""
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

    def executeSyntax(e: ft.ControlEvent) -> None:
        result = sintax.execute_sintax(textArea1.value)
        resultTable.rows.clear()
        for line in result:
            resultTable.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(Text(line)),  # Display the syntax analysis result
                    ft.DataCell(Text("")),
                    ft.DataCell(Text("")),
                    ft.DataCell(Text("")),
                ])
            )
        page.update()

    def executeCompile(e: ft.ControlEvent) -> None:
        result = compile(textArea1.value)
        resultTable.rows.clear()
        for line in result.split("\n"):
            if (line.strip() == ""):
                continue
            resultTable.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(Text(line)),  # Display the syntax analysis result
                    ft.DataCell(Text("")),
                    ft.DataCell(Text("")),
                    ft.DataCell(Text("")),
                ])
            )
        page.update()

    def executeSemantic(e: ft.ControlEvent) -> None:
        result = semantic(textArea1.value)
        resultTable.rows.clear()
        for line in result.split(";"):
            if (line.strip() == "" or line.strip() == " " or line.strip() == "\n"):
                continue
            resultTable.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(Text(line)),  # Display the syntax analysis result
                    ft.DataCell(Text("")),
                    ft.DataCell(Text("")),
                    ft.DataCell(Text("")),
                ])
            )
        page.update()

    def loadFile(e: FilePickerResultEvent) -> None:
        if e.files:
            file_path = e.files[0].path
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    textArea1.value = file.read()
                    validate(None)  # Enable buttons if content is loaded
                    page.update()
            except Exception as ex:
                print(f"Error reading file: {ex}")

    filePicker.on_result = loadFile

    # Button to open file picker
    loadFileButton = ft.ElevatedButton(
        text="Load File",
        on_click=lambda _: filePicker.pick_files(allowed_extensions=["java", "txt"])
    )

    textArea1.on_change = validate
    executeButtonLex.on_click = executeLex
    executeButtonSyntax.on_click = executeSyntax
    executeButtonCompile.on_click = executeCompile
    executeButtonSemantic.on_click = executeSemantic

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        # Main menu
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Menu'), bgcolor='blue'),
                    ft.Column(
                        controls=[
                            Text(value='Java-Python Compiler\nSamuel Molina and Angelo Polgrossi', size=30, text_align="CENTER"),
                            ElevatedButton(text='Lexical Analyzer', on_click=lambda _: page.go('/lex')),
                            ElevatedButton(text='Syntax Analyzer', on_click=lambda _: page.go('/syntax')),
                            ElevatedButton(text='Semantic Analyzer', on_click=lambda _: page.go('/semantic')),
                            ElevatedButton(text='Compiler', on_click=lambda _: page.go('/compile')),
                        ],
                        expand=True,
                        spacing=20,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    )
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26,
                scroll=ft.ScrollMode.ALWAYS  # Habilitar scroll en el menú principal
            )
        )
    
        # Lexical Analyzer Page
        if page.route == '/lex':
            page.views.append(
                View(
                    route='/lex',
                    controls=[
                        AppBar(title=Text('Lexical Analyzer'), bgcolor='blue'),
                        ft.Column(
                            controls=[
                                Text(value='Lexical Analyzer', size=30),
                                textArea1,
                                loadFileButton,  # Botón para cargar archivos
                                executeButtonLex,
                                resultTableContainer,  # Tabla de resultados
                            ],
                            expand=True,
                            spacing=10,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        )
                    ],
                    scroll=ft.ScrollMode.ALWAYS  # Habilitar scroll en la página del analizador léxico
                )
            )
    
        # Syntax Analyzer Page
        if page.route == '/syntax':
            page.views.append(
                View(
                    route='/syntax',
                    controls=[
                        AppBar(title=Text('Syntax Analyzer'), bgcolor='blue'),
                        ft.Column(
                            controls=[
                                Text(value='Syntax Analyzer', size=30),
                                textArea1,
                                loadFileButton,  # Botón para cargar archivos
                                executeButtonSyntax,
                                resultTableContainer,  # Tabla de resultados
                            ],
                            expand=True,
                            spacing=10,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        )
                    ],
                    scroll=ft.ScrollMode.ALWAYS  # Habilitar scroll en la página del analizador sintáctico
                )
            )

        if page.route == '/semantic':
            page.views.append(
                View(
                    route='/semantic',
                    controls=[
                        AppBar(title=Text('Semantic Analyzer'), bgcolor='blue'),
                        ft.Column(
                            controls=[
                                Text(value='Semantic Analyzer', size=30),
                                textArea1,
                                loadFileButton,  # Botón para cargar archivos
                                executeButtonSemantic,
                                resultTableContainer,  # Tabla de resultados
                            ],
                            expand=True,
                            spacing=10,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        )
                    ],
                    scroll=ft.ScrollMode.ALWAYS  # Habilitar scroll en la página del compilador
                )
            )
    
        # Compiler Page
        if page.route == '/compile':
            page.views.append(
                View(
                    route='/compile',
                    controls=[
                        AppBar(title=Text('Compiler'), bgcolor='blue'),
                        ft.Column(
                            controls=[
                                Text(value='Compiler', size=30),
                                textArea1,
                                loadFileButton,  # Botón para cargar archivos
                                executeButtonCompile,
                                resultTableContainer,  # Tabla de resultados
                            ],
                            expand=True,
                            spacing=10,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        )
                    ],
                    scroll=ft.ScrollMode.ALWAYS  # Habilitar scroll en la página del compilador
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