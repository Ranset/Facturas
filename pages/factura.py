from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import CustomTextDatePicker, Tabla_Factura_Row, Menu

class Factura(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # <Carga de datos
        if States.where_i_am == States._cotizacion_location:
            data = {
                "Sucess": True,
                "Data": {
                    "nombre_clientes": [
                                    {"id": 1, "nombre": "ACME"},
                                    {"id": 2, "nombre": "Beta S.A."},
                                    {"id": 3, "nombre": "Cliente 3"},
                                    {"id": 4, "nombre": "Distribuciones López"},
                    ],
                    "datos_tabla": [
                                {"estado": "XEnviar", "fecha": "15-01-2025", "numero": "250012", "cliente": "Empresa de suministros integrales y cooperación económica", "total": "158548.52", "moneda": "CUP"},
                                {"estado": "Enviada", "fecha": "15-01-2025", "numero": "250013", "cliente": "Pedro", "total": "150158548.00", "moneda": "CUP"},
                                {"estado": "XEnviar", "fecha": "15-01-2025", "numero": "250015", "cliente": "Carlos Ace", "total": "548.99", "moneda": "USD"},
                                {"estado": "Enviada", "fecha": "15-01-2025", "numero": "250012", "cliente": "Empresa de suministros integrales y cooperación económica", "total": "158548.52", "moneda": "CUP"},
                    ]
                }
            }
        else:
            data = {
                "Sucess": True,
                "Data": {
                    "nombre_clientes": [
                                    {"id": 1, "nombre": "ACME"},
                                    {"id": 2, "nombre": "Beta S.A."},
                                    {"id": 3, "nombre": "Cliente 3"},
                                    {"id": 4, "nombre": "Distribuciones López"},
                    ],
                    "datos_tabla": [
                                {"estado": "Pagada", "fecha": "15-01-2025", "numero": "250012", "cliente": "Empresa de suministros integrales y cooperación económica", "total": "158548.52", "moneda": "CUP"},
                {"estado": "Enviada", "fecha": "15-01-2025", "numero": "250013", "cliente": "Pedro", "total": "150158548.00", "moneda": "CUP"},
                {"estado": "XEnviar", "fecha": "15-01-2025", "numero": "250015", "cliente": "Carlos Ace", "total": "548.99", "moneda": "USD"},
                    ]
                }
            }

        # <Fin de carga de datos>

        # <Controls
        ## <common variables
        inputs_height = 48
        inputs_bgcolor = ft.Colors.WHITE
        inputs_border_color= ft.Colors.GREY_400
        ## common variables>

        ## <Widgets objects
        txt_Cotizacion_title = ft.Text(
            "Cotizaciones" if States.where_i_am == States._cotizacion_location else "Facturas",
            size= 35,
            weight= ft.FontWeight.BOLD,
            )
        
        def _btn_crear_cotizacion_clicked(e):
            from router import show_view
            
            if States.where_i_am == States._cotizacion_location:
                States.i_come_from = States._Crear_btn_loc_cotizacion
                States.where_i_am = States._formulario_factura_location
            else:
                States.i_come_from = States._Crear_btn_loc_facturas
                States.where_i_am = States._formulario_factura_location
            show_view(page, States._formulario_factura_location)

        btn_crear_cotizacion = ft.ElevatedButton(
            text="Crear Cotización" if States.where_i_am == States._cotizacion_location else "Crear Factura",
            bgcolor= '#2c78d0',
            color= 'white',
            on_click= _btn_crear_cotizacion_clicked,
        )

        if States.where_i_am == States._cotizacion_location:
            select_estatus = ft.Dropdown(
                options=
                [
                    ft.dropdown.Option("XEnviar"),
                    ft.dropdown.Option("Enviada"),
                ],
                label= "Estatus",
                width= 130,
                filled= True,
                fill_color= inputs_bgcolor,
                border_color= inputs_border_color,
                hover_color= inputs_bgcolor
            )
        else:
            select_estatus = ft.Dropdown(
                options=
                [
                    ft.dropdown.Option("XEnviar"),
                    ft.dropdown.Option("Enviada"),
                    ft.dropdown.Option("Pagada"),
                ],
                label= "Estatus",
                width= 130,
                filled= True,
                fill_color= inputs_bgcolor,
                border_color= inputs_border_color,
                hover_color= inputs_bgcolor
            )

        select_cliente = ft.Dropdown(
            options=[
                ft.dropdown.Option(c) for c in data["Data"]["nombre_clientes"]
            ],
            label="Clientes",
            expand=True,
            enable_filter=True,
            editable=True,
            filled= True,
            fill_color= inputs_bgcolor,
            border_color= inputs_border_color,
            hover_color= ft.Colors.WHITE
        )

        select_fecha_inicio = CustomTextDatePicker(page= page,label= "Desde").Crear()
        select_fecha_inicio.height = inputs_height

        select_fecha_fin = CustomTextDatePicker(page= page,label= "Hasta").Crear()
        select_fecha_fin.height = inputs_height

        txt_nro_factura = ft.TextField(
            label="# Cotización" if States.where_i_am == States._cotizacion_location else "# Factura",
            # expand=True,
            height= inputs_height,
            width= 140,
            bgcolor= inputs_bgcolor,
            border_color= inputs_border_color,
            hover_color= inputs_bgcolor
        )

        def click_buscar (e):
            self.tabla_controls = [Tabla_Factura_Row("Pagada", "15-01-2025", "250015", "Carlos Ace", "548.99", "USD").crear(),]
            tabla.controls.clear()
            for row in self.tabla_controls:
                tabla.controls.append(row)
            tabla.update()


        btn_buscar = ft.FloatingActionButton(
            bgcolor= "#838383",
            foreground_color= 'white',
            icon= ft.Icons.REFRESH,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
            on_click= click_buscar
        )

        def click_clear (e):
            self.tabla_controls = [
            Tabla_Factura_Row("Vencida", "15-01-2025", "250012", "Empresa de suministros integrales y cooperaci'on econ'omica", "158548.52", "CUP").crear(),
            Tabla_Factura_Row("Borrador", "15-01-2025", "250013", "Pedro", "150158548.00", "CUP").crear(),
            Tabla_Factura_Row("XEnviar", "15-01-2025", "250015", "Carlos Ace", "548.99", "USD").crear(),
            Tabla_Factura_Row("Pagada", "15-01-2025", "250015", "Carlos Ace", "548.99", "USD").crear(),
            Tabla_Factura_Row("Enviada", "15-01-2025", "250015", "Carlos Ace", "548.99", "USD").crear(),
            ]

            select_estatus.value = None
            select_cliente.value = None
            select_fecha_inicio.value = ""
            select_fecha_fin.value = ""
            txt_nro_factura.value = ""

            tabla.controls.clear()
            for row in self.tabla_controls:
                tabla.controls.append(row)
            page.update()
        
        btn_clear = ft.FloatingActionButton(
            bgcolor= '#838383',
            foreground_color= 'white',
            icon= ft.Icons.CLEAR,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
            on_click= click_clear
        )

        tabla_encabezado= ft.Container(content=ft.Row(
            controls=[
                ft.Container(content= ft.Text("Estado", weight= ft.FontWeight.BOLD, size=14), width= 70, margin= ft.margin.only(left= 15)),
                ft.Container(content= ft.Text("Fecha", weight= ft.FontWeight.BOLD, size=14), width= 80, margin= ft.margin.only(left= 15)),
                ft.Container(content= ft.Text("Número", weight= ft.FontWeight.BOLD, size=14), width= 80, margin= ft.margin.only(left= 15)),
                ft.Container(content= ft.Text("Cliente", weight= ft.FontWeight.BOLD, size=14), expand= True),
                ft.Container(content= ft.Text("Total", weight= ft.FontWeight.BOLD, size=14), width= 200),
                ft.Container(content= ft.Text("Moneda", weight= ft.FontWeight.BOLD, size=14), width= 100),
                ft.Container(content= ft.Text("Acción", weight= ft.FontWeight.BOLD, size=14), width= 80),
            ],
            height= 40,
            expand= True,
            alignment= ft.MainAxisAlignment.START,
            spacing= 0
            ),
            bgcolor= ft.Colors.WHITE,
            )

        divider_encabezado_de_tabla = ft.Divider(color= ft.Colors.GREY_700, height=1)

        self.tabla_controls = []

        for row in data["Data"]["datos_tabla"]:
                self.tabla_controls.append(
                    Tabla_Factura_Row(
                        estado= row["estado"],
                        fecha= row["fecha"],
                        numero= row["numero"],
                        cliente= row["cliente"],
                        total= row["total"],
                        moneda= row["moneda"]
                    ).crear()
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
        
        
        
        tabla = ft.ListView(
            controls= self.tabla_controls,
            expand= True
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
                bgcolor= ft.Colors.WHITE,
                margin= ft.margin.only(left=15, right=15, top= 12),
                border= ft.border.all(1,inputs_border_color),
                border_radius= ft.border_radius.all(5),
                expand= True
        )

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[contenedor1, contenedor2, contenedor3], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>