from flet_base import flet_instance as ft
from pages.common_controls.menu import contenedor_menu
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import CustomTextDatePicker, Tabla_Factura_Row

class FormularioFactura(ft.Container):
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
        def title():
            if States.i_come_from == States._Crear_btn_loc_facturas:
                return "Crear Factura"
            if States.i_come_from == States._Crear_btn_loc_cotizacion:
                return "Crear Cotización"
        
        txt_title = title()

        txt_formulario_title = ft.Text(
            txt_title,
            size= 20,
            weight= ft.FontWeight.BOLD,
            )

        txt_info_title = ft.Text("Información General", weight= ft.FontWeight.BOLD)

        cliente_suggestions = [
            "ACME",
            "Beta S.A.",
            "Cliente 3",
            "Distribuciones López",
        ]

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

        btn_agragar_cliente = ft.FloatingActionButton(
            bgcolor= "#2c78d0",
            foreground_color= 'white',
            icon= ft.Icons.ADD,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
        )

        txt_moneda = ft.Text("Moneda:")

        def moneda_change(e):
            print(f"Moneda {e.control.value} seleccionada")

        radio_monedas = ft.RadioGroup(
            content= ft.Row(
            [
                ft.Radio(label= "CUP", value="cup"),
                ft.Radio(label= "MLC", value="mlc"),
                ft.Radio(label= "USD", value="usd"),
            ],
            ),
            on_change= moneda_change,
            value= "cup",
        )

        txt_pago = ft.Text("Pago:")

        cont_separador = ft.Container(expand= True)

        dd_pago = ft.Dropdown(
            options=[
                ft.DropdownOption("Transferencia"),
                ft.DropdownOption("Efectivo"),
            ],
            value= "Transferencia",
            border_color= ft.Colors.GREY_400,
        )

        txt_fecha = ft.Text("Fecha:")

        select_fecha_inicio = CustomTextDatePicker(page= page).Crear()

        ## Widgets objects>
        # Controls>

        # <Layout

        Row_title = ft.Row(
            controls=[txt_formulario_title],
            alignment= ft.MainAxisAlignment.START,
            height= 45
            )
        contenedor_title = ft.Container(
            content=Row_title, 
            bgcolor= ft.Colors.WHITE,
            padding= ft.padding.only(left= 25),
            border= ft.border.only(bottom=ft.border.BorderSide(1, "#CBD5E1"))
            # margin= ft.margin.only(top=30, left=15, right=15),
        )

        Row_info1 = ft.Row(
            controls=[
                ft.Icon(ft.Icons.PERSON_SEARCH),
                txt_info_title
            ]
            )
        Row_info2 = ft.Container(
            content= ft.Row(
            controls=[
                select_cliente,
                btn_agragar_cliente
            ],
            ),
            margin= ft.margin.only(top= 5)
        ) 
        Row_info3 = ft.Container(
            content= ft.Row(
            controls=[
                txt_moneda,
                radio_monedas,
                cont_separador,
                txt_pago,
                dd_pago,
                cont_separador,
                txt_fecha,
                select_fecha_inicio
            ],
            expand= True,
            alignment= ft.MainAxisAlignment.CENTER
            ),
            margin= ft.margin.only(top= 5),
        ) 
        column_info = ft.Column(
            controls=[
                Row_info1,
                Row_info2,
                Row_info3
            ]
        )
        contenedor_info = ft.Container(
            content= column_info,
            bgcolor= ft.Colors.WHITE,
            border= ft.border.all(1, "#CBD5E1"),
            border_radius= ft.border_radius.all(5),
            margin= ft.margin.only(left= 25, right=25, top=15),
            padding= ft.padding.all(25)
        )


        columna_menu = ft.Column(controls= [contenedor_menu])
        column2 = ft.Column(controls=[contenedor_title, contenedor_info], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>