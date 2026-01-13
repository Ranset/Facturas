import flet as ft
from pages.common_controls.menu import contenedor_menu
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import CustomTextDatePicker, CustomTextFieldAutocomplete

class Cotizacion(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # <Controls
        ## <common variables
        ## common variables>

        ## <Widgets objects
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

        cliente_suggestions = [
            "ACME",
            "Beta S.A.",
            "Cliente 3",
            "Distribuciones López",
        ]
        # select_cliente = CustomTextFieldAutocomplete(
        #     page= page,
        #     label= "Clientes",
        #     suggestions= cliente_suggestions
        # ).Crear()

        select_cliente = ft.Dropdown(
            options=[
                ft.dropdown.Option(c) for c in cliente_suggestions
            ],
            label="Clientes",
            expand=True,
        )

        select_fecha_inicio = CustomTextDatePicker(page= page,label= "Desde").Crear()

        select_fecha_fin = CustomTextDatePicker(page= page,label= "Hasta").Crear()

        txt_nro_factura = ft.TextField(
            label="# Factura",
            expand=True
        )

        ## Widgets objects>
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

        Row2 = ft.Row(
            controls=[
                select_estatus,
                select_cliente,
                select_fecha_inicio,
                select_fecha_fin,
                txt_nro_factura
                ],
                vertical_alignment= ft.CrossAxisAlignment.START,
                spacing= 10
            )
        contenedor2 = ft.Container(
            content=Row2, 
            # bgcolor= "#e67979",
            margin= ft.margin.only(left=15, right=15),
            )

        columna_menu = ft.Column(controls= [contenedor_menu])
        column2 = ft.Column(controls=[contenedor1, contenedor2], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)
        # Layout>