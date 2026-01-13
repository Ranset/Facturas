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
            bgcolor= '#2c78d0',
            color= 'white',
        )

        select_estatus = ft.Dropdown(
            options=[
                # ft.dropdown.Option("Todas"),
                ft.dropdown.Option("Borrador"),
                ft.dropdown.Option("Enviada"),
                ft.dropdown.Option("Vencida"),
            ],
            # value="Todas",
            expand= True,
            label= "Estatus"
        )

        # sample suggestions for clientes
        cliente_suggestions = [
            "ACME",
            "Beta S.A.",
            "Cliente 3",
            "Distribuciones López",
        ]

        def on_suggestion_click(value):
            select_cliente_field.value = value
            suggestions_container.visible = False
            page.update()

        def on_cliente_change(e):
            txt = e.control.value or ""
            if not txt:
                suggestions_container.content = ft.Column(controls=[])
                suggestions_container.visible = False
                page.update()
                return
            matches = [c for c in cliente_suggestions if txt.lower() in c.lower()]
            controls = []
            for m in matches:
                controls.append(
                    ft.Container(
                        content=ft.TextButton(text=m, on_click=lambda ev, v=m: on_suggestion_click(v)),
                        padding=ft.padding.only(left=6, right=6),
                    )
                )
            suggestions_container.content = ft.Column(controls=controls)
            suggestions_container.visible = len(controls) > 0
            page.update()

        select_cliente_field = ft.TextField(
            label="Clientes",
            expand=True,
            on_change=on_cliente_change,
        )

        suggestions_container = ft.Container(
            content=ft.Column(controls=[]),
            visible=False,
            bgcolor="white",
            border=ft.border.all(1, "#cccccc"),
            padding=ft.padding.only(top=2, bottom=2),
        )

        # stack the text field and the suggestions container so suggestions appear below the field
        select_cliente = ft.Stack(controls=[select_cliente_field, suggestions_container], expand=True)

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
        contenedor1 = ft.Container(
            content=Row1, 
            # bgcolor= "#7979e6",
            margin= ft.margin.only(top=30, left=15, right=15),
            )
        
        Row2 = ft.Row(controls=[select_estatus, select_cliente])
        contenedor2 = ft.Container(
            content=Row2, 
            bgcolor= "#e67979",
            margin= ft.margin.only(left=15, right=15),
            )

        columna_menu = ft.Column(controls= [contenedor_menu])
        column2 = ft.Column(controls=[contenedor1, contenedor2], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)
        # Layout>