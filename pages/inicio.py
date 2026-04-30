from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import Tabla_Factura_Row, Menu
from controller import dashboard_data

class Inicio(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        #  <Carga de datos
        
        data = dashboard_data()

        # <Fin Carga de datos

        # <Controls
        ## <common variables
        inputs_height = 48
        inputs_bgcolor = ft.Colors.WHITE
        inputs_border_color= ft.Colors.GREY_400

        ## common variables>

        ## <Widgets objects
        txt_Cotizacion_title = ft.Text(
            "Dashboard",
            size= 35,
            weight= ft.FontWeight.BOLD,
            )
        
        def _btn_crear_cotizacion_clicked(e):
            from router import show_view
            
            States.i_come_from = States._Crear_btn_loc_cotizacion
            States.where_i_am = States._formulario_factura_location
            show_view(page, States._formulario_factura_location)
        
        def _btn_crear_factura_clicked(e):
            from router import show_view
            
            States.i_come_from = States._Crear_btn_loc_facturas
            States.where_i_am = States._formulario_factura_location
            show_view(page, States._formulario_factura_location)

        btn_crear = ft.SubmenuButton(
            content= ft.Text("    +  Crear    "),
            style= ft.ButtonStyle(
                bgcolor= '#2c78d0',
                color= 'white',
            ),
            controls= [
                ft.MenuItemButton(content=ft.Text("Factura"), on_click= _btn_crear_factura_clicked),
                ft.MenuItemButton(content=ft.Text("Cotización"), on_click= _btn_crear_cotizacion_clicked),
            ]
        )

        total_facturado = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Container(content= ft.Icon(ft.Icons.PAYMENTS_OUTLINED, color= "#005BAF"), bgcolor= "#DBEAFE", width= 40, height= 40, border_radius= ft.border_radius.all(8), margin= ft.margin.only(bottom= 10)),
                        ft.Row(expand= True),
                        ft.Text(data["Data"]["total_facturado"], size= 27, color="#005BAF", weight= ft.FontWeight.BOLD, text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.Text("Total Facturado", size= 12, color="#64748B", weight="normal", text_align= ft.TextAlign.START),
                    ft.Text(data["Data"]["monto_facturado"], size=30, color= "black", weight= ft.FontWeight.BOLD)
                ],
                horizontal_alignment= "start",
                alignment= ft.MainAxisAlignment.START,
                spacing= 0
            ),
            bgcolor= inputs_bgcolor,
            padding= ft.padding.all(18),
            expand= True,
            border_radius= 20,
            shadow= ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=2,
                            color=ft.Colors.BLUE_GREY_200,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
                        ),
            margin= ft.margin.only(right= 20)
        )
        
        cotizaciones_por_facturar = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Container(content= ft.Icon(ft.Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED, color= "#D97706"), bgcolor= "#FEF3C7", width= 40, height= 40, border_radius= ft.border_radius.all(8), margin= ft.margin.only(bottom= 10)),
                        ft.Row(expand= True),
                        ft.Text(data["Data"]["cotizaciones_sin_facturar"], size=27, color= "#D97706", weight= ft.FontWeight.BOLD, text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.Text("Cotizaciones Sin Enviar", size= 12, color="#64748B", weight="normal", text_align= ft.TextAlign.START),
                    ft.Text(data["Data"]["monto_cotizaciones_sin_facturar"], size=30, color= "black", weight= ft.FontWeight.BOLD)
                ],
                horizontal_alignment= "start",
                alignment= ft.MainAxisAlignment.START,
                spacing= 0
            ),
            bgcolor= inputs_bgcolor,
            padding= ft.padding.all(18),
            expand= True,
            border_radius= 20,
            shadow= ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=2,
                            color=ft.Colors.BLUE_GREY_200,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
                        ) 
        )

        facturas_por_pagar = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Container(content= ft.Icon(ft.Icons.REQUEST_QUOTE_OUTLINED, color= "#9333EA"), bgcolor= "#F3E8FF", width= 40, height= 40, border_radius= ft.border_radius.all(8), margin= ft.margin.only(bottom= 10)),
                        ft.Row(expand= True),
                        ft.Text(data["Data"]["facturas_por_pagar"], size=27, color= "#9333EA", weight= ft.FontWeight.BOLD, text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.Text("Facturas Por Pagar", size= 12, color="#64748B", weight="normal", text_align= ft.TextAlign.START),
                    ft.Text(data["Data"]["monto_facturas_por_pagar"], size=30, color= "black", weight= ft.FontWeight.BOLD)
                ],
                horizontal_alignment= "start",
                alignment= ft.MainAxisAlignment.START,
                spacing= 0
            ),
            bgcolor= inputs_bgcolor,
            padding= ft.padding.all(18),
            expand= True,
            border_radius= 20,
            shadow= ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=2,
                            color=ft.Colors.BLUE_GREY_200,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
                        ),
            margin= ft.margin.only(left= 20)
        )

        tabla_title = ft.Container(content= ft.Row(controls=[ft.Text("Actividad Reciente", size= 18, weight= ft.FontWeight.BOLD)], alignment= ft.MainAxisAlignment.START), margin= ft.margin.only(left=15, bottom= 7, top= 7))

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
            bgcolor= "#F4F5F7",
            )

        divider_encabezado_de_tabla = ft.Divider(color= "#DFE1E4", height=1)


        self.tabla_controls = []

        for dato in data["Data"]["datos_tabla"]:
            self.tabla_controls.append(Tabla_Factura_Row(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], page).crear())

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
                btn_crear,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.END,
        )

        Row1 = ft.Row(controls=[column_left, column_Right], alignment= ft.MainAxisAlignment.CENTER)
        contenedor1 = ft.Container(
            content=Row1, 
            margin= ft.margin.only(top=30, left=15, right=15, bottom= 12),
        )

        Row2 = ft.Row(
            controls=[
                    total_facturado,
                    cotizaciones_por_facturar,
                    facturas_por_pagar
                ],
                vertical_alignment= ft.CrossAxisAlignment.START,
                spacing= 10
            )
        contenedor2 = ft.Container(
            content=Row2, 
            margin= ft.margin.only(left=15, right=15, bottom= 12),
            )
        
        
        
        tabla = ft.ListView(
            controls= self.tabla_controls,
            expand= True
        )
        
        columna_tabla = ft.Column(
            controls=[
                tabla_title,
                divider_encabezado_de_tabla,
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