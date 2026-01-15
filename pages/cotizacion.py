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

        tabla_encabezado= ft.Container(content=ft.Row(
            controls=[
                ft.Container(content= ft.Text("Estado", weight= ft.FontWeight.BOLD, size=14)),
                ft.Container(content= ft.Text("Fecha", weight= ft.FontWeight.BOLD, size=14)),
                ft.Container(content= ft.Text("Número", weight= ft.FontWeight.BOLD, size=14)),
                ft.Container(content= ft.Text("Cliente", weight= ft.FontWeight.BOLD, size=14)),
                ft.Container(content= ft.Text("Total", weight= ft.FontWeight.BOLD, size=14)),
                ft.Container(content= ft.Text("Moneda", weight= ft.FontWeight.BOLD, size=14)),
                ft.Container(content= ft.Text("Acción", weight= ft.FontWeight.BOLD, size=14)),
            ],
            height= 40
            ),
            bgcolor= ft.Colors.WHITE
            )

        divider_encabezado_de_tabla = ft.Divider(color= ft.Colors.GREY_700, height=1)



        tabla_row = ft.Row(
            controls=[
                ft.Container(
                    content= ft.Text(
                        value= "Borrador",
                        color= ft.Colors.WHITE
                    ),
                    bgcolor= "#CA1414",
                    alignment= ft.alignment.center,
                    border_radius= ft.border_radius.all(8),
                    width= 70,
                    height= 20,
                    margin= ft.margin.only(left= 15)
                    ),
                    ft.Container(
                        content= ft.Text("08-01-2025")
                    ),
                    ft.Container(
                        content= ft.Text("250001")
                    ),
                    ft.Container(
                        content= ft.Text("Empresa Importadora del Este y del oriente")
                    ),
                    ft.Container(
                        content= ft.Text("$108,526,354.25")
                    ),
                    ft.Container(
                        content= ft.Text("CUP")
                    ),
                    ft.Container(
                        content= ft.TextButton(text="Facturar")
                    ),
                    ft.Container(
                        content= ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem("Borrador", height= 10),
                                ft.PopupMenuItem("Enviada", height= 10),
                                ft.PopupMenuItem("Facturar", height= 10),
                                ft.PopupMenuItem(
                                    content= ft.Column(controls=[
                                        ft.Divider(height=8),
                                        ft.Text("PDF"),
                                    ], alignment= ft.alignment.top_center, spacing=0),
                                    height= 10),
                                ft.PopupMenuItem(
                                    content= ft.Column(controls=[
                                        ft.Divider(height=8),
                                        ft.Text("Eliminar", color= ft.Colors.RED),
                                    ], alignment= ft.alignment.top_center, spacing=0),
                                    height= 10
                                ),
                            ]
                        )
                    ),
            ],
            height= 33,
            
        )

        tabla_controls = [
            tabla_row,
        ]

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
        
        
        
        tabla = ft.Column(
            controls= tabla_controls,
            alignment= ft.MainAxisAlignment.START,
            spacing= 0,
        )
        
        columna_tabla = ft.Column(
            controls=[
                tabla_encabezado,
                divider_encabezado_de_tabla,
                tabla
            ],
            alignment= ft.MainAxisAlignment.START,
            spacing= 0
        )
        contenedor3 = ft.Container(
            content=columna_tabla,
                bgcolor= "#41da67",
                margin= ft.margin.only(left=15, right=15, top= 12)
        )

        columna_menu = ft.Column(controls= [contenedor_menu])
        column2 = ft.Column(controls=[contenedor1, contenedor2, contenedor3], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)
        # Layout>