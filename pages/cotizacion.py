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
        inputs_height = 48
        inputs_bgcolor = ft.Colors.WHITE
        inputs_border_color= ft.Colors.GREY_400
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
            # expand= True,
            label= "Estatus",
            width= 130,
            filled= True,
            fill_color= inputs_bgcolor,
            border_color= inputs_border_color
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
            enable_filter=True,
            editable=True,
            filled= True,
            fill_color= inputs_bgcolor,
            border_color= inputs_border_color
        )

        select_fecha_inicio = CustomTextDatePicker(page= page,label= "Desde").Crear()
        select_fecha_inicio.height = inputs_height

        select_fecha_fin = CustomTextDatePicker(page= page,label= "Hasta").Crear()
        select_fecha_fin.height = inputs_height

        txt_nro_factura = ft.TextField(
            label="# Factura",
            # expand=True,
            height= inputs_height,
            width= 140,
            bgcolor= inputs_bgcolor,
            border_color= inputs_border_color
        )

        btn_buscar = ft.FloatingActionButton(
            bgcolor= "#838383",
            foreground_color= 'white',
            icon= ft.Icons.REFRESH,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
        )
        
        btn_clear = ft.FloatingActionButton(
            bgcolor= '#838383',
            foreground_color= 'white',
            icon= ft.Icons.CLEAR,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
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
                txt_nro_factura,
                btn_buscar,
                btn_clear
                ],
                vertical_alignment= ft.CrossAxisAlignment.START,
                spacing= 10
            )
        contenedor2 = ft.Container(
            content=Row2, 
            # bgcolor= "#e67979",
            margin= ft.margin.only(left=15, right=15),
            )
        
        Row3= ft.Row(
            controls=[
                select_cliente
            ]
            )
        columna_tabla = ft.Column(
            controls=[
                Row3,
                Row1
            ]
        )
        contenedor3 = ft.Container(
            content=columna_tabla,
                bgcolor= "#41da67",
                margin= ft.margin.only(left=15, right=15, top= 12),
        )

        columna_menu = ft.Column(controls= [contenedor_menu])
        column2 = ft.Column(controls=[contenedor1, contenedor2, contenedor3], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)
        # Layout>