import flet as ft
from pages.common_controls.menu import contenedor_menu
from pages.common_controls.states import States

class Cotizacion(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # <Controls
        ## <common variables
        ## common variables>

        ## <Controls objects
        txt_Cotizacion_title = ft.Text(
            "Cotizaciones",
            size= 35,
            weight= ft.FontWeight.BOLD,
            )

        btn_crear_cotizacion = ft.ElevatedButton(
            text="Crear Cotización",
        )
        ## Controls objects>
        # Controls>

        # <Layout
        column_left = ft.Column(
            controls= [
                txt_Cotizacion_title,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.START,
            expand= True,
        )
        
        column_Right = ft.Column(
            controls= [
                btn_crear_cotizacion,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.END,
            expand= True,
        )

        Row1 = ft.Row(controls=[column_left, column_Right], alignment= ft.MainAxisAlignment.CENTER)
        contenedor2 = ft.Container(
            content=Row1, 
            bgcolor= "#7979e6",
            margin= ft.margin.only(top=30, left=15, right=15),
            )

        columna_menu = ft.Column(controls= contenedor_menu)
        column2 = ft.Column(controls=[contenedor2], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)
        # Layout>