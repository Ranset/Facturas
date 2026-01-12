import flet as ft

class Cotizacion(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Controls
        btn_inicio = ft.FilledButton(
            text="Inicio",
            icon=ft.Icons.ADD_OUTLINED,
            width=200,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
        )

        text2 = ft.Text("Panel 2")

        # Layout
        menu = ft.Column(
            controls= [btn_inicio, ],
            expand= True,
            tight= True,
            )
        contenedor_menu = ft.Container(
            content=menu,
            bgcolor= '#222a31', 
            expand= True,
            width= 200
            )

        Row2 = ft.Row(controls=[text2, ft.Text("Para contenido")], alignment= ft.MainAxisAlignment.CENTER)
        contenedor2 = ft.Container(content=Row2, bgcolor= '#f3f1f3', expand= True)

        columna_menu = ft.Column(controls=[contenedor_menu])
        column2 = ft.Column(controls=[contenedor2], expand= True)

        Row_centro = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_centro)