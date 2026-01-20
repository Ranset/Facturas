from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import CustomTextDatePicker, Tabla_Factura_Row, Menu, CustomTextFieldAutocomplete

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
            txt_total.value = f"Total {e.control.value.upper()}:"
            page.update()

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

        txt_finanzas_title = ft.Text("Configuración financiera", weight= ft.FontWeight.BOLD)

        cup_tasa = ft.Row(
            controls=[
                ft.Text("CUP:"),
                ft.TextField("460.74",border_color= ft.Colors.GREY_400,width= 80)
            ]
        )
        
        mlc_tasa = ft.Row(
            controls=[
                ft.Text("MLC:"),
                ft.TextField("460.74",border_color= ft.Colors.GREY_400,width= 80)
            ]
        )
        
        tasa_fiscal = ft.Row(
            controls=[
                ft.Text("Tasa Fiscal:"),
                ft.TextField("10", suffix= ft.Text("%"),border_color= ft.Colors.GREY_400,width= 80)
            ]
        )

        txt_title_add_product = ft.Text("Agregar Producto", weight= ft.FontWeight.BOLD)

        btn_new_product = ft.ElevatedButton("Nuevo", bgcolor="#2c78d0", color= "white", width= 80, height= 25)

        product_suggestions = [
            #(nombre, precio, moneda, iva[bool], proveedor, peso, id)
            ("Impresora Multifuncional",105.25,"USD",True,"CVA",10,1),
            ("Laptop Gamer",1500.00,"USD",True,"Amazon",5,2),
            ("Monitor 24 pulgadas",200.75,"MXN",False,"ML",15,3),
            ("Teclado Mecánico",85.50,"USD",True,"Ciberpuerta",20,4),
            ("Ratón Inalámbrico",45.00,"MXN",False,"CVA",25,5),
        ]

        def update_price():
            precio.value = States.selected_product_price
            precio.update()
        
        select_product_instance = CustomTextFieldAutocomplete(
            page,
            "Producto",
            product_suggestions,
            )
        select_product = select_product_instance.Crear()

        # Actualizar precio del producto seleccionado
        select_product.controls[0].content.on_focus = lambda e: update_price()

        cantidad = ft.TextField(label="Cantidad",width= 95, border_color= inputs_border_color)
        
        precio = ft.TextField(label="Precio USD", width= 150, border_color= inputs_border_color)

        def click_add_product(e):
            # Validar entradas antes de crear la fila de producto
            nombre_producto = select_product_instance.select_cliente_field.value
            if not nombre_producto:
                print("Nombre de producto vacío")
                return
            try:
                qty = int(cantidad.value)
            except Exception:
                print("Cantidad inválida")
                return
            try:
                price = float(precio.value)
            except Exception:
                print("Precio inválido")
                return
            # Creando nueva fila de producto
            new_product = (nombre_producto, price, qty, price * porciento_fiscal(tasa_fiscal), qty * price * porciento_fiscal(tasa_fiscal))
            new_row = ft.DataRow(
                    [
                        ft.DataCell(ft.Text(new_product[0], no_wrap= True)),
                        ft.DataCell(ft.Text(Tabla_Factura_Row.formatear_con_comas(self,new_product[1]))),
                        ft.DataCell(ft.Text(str(new_product[2]))),
                        ft.DataCell(ft.Text(Tabla_Factura_Row.formatear_con_comas(self,new_product[3]))),
                        ft.DataCell(ft.Text(Tabla_Factura_Row.formatear_con_comas(self,new_product[4]))),
                    ],
                    on_select_changed= on_select_row,
                    data= new_product
                )
            dt_factura.rows.append(new_row)
            actualizar_totales()
            # Limpiar valores usando la instancia
            select_product_instance.select_cliente_field.value = ""
            cantidad.value = ""
            precio.value = ""
            States.selected_product_price = ""
            # Enfocar de forma robusta
            try:
                select_product_instance.focus_field()
            except Exception:
                try:
                    select_product.controls[0].content.autofocus = True
                except Exception:
                    pass
            page.update()

        btn_add_product = ft.FloatingActionButton(
            bgcolor= "#2c78d0",
            foreground_color= 'white',
            icon= ft.Icons.ADD_SHOPPING_CART,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
            on_click= click_add_product
        )

        def click_editar(e):
            select_filter = False
            # Dejar solo la primera fila seleccionada
            for row in dt_factura.rows:
                if row.selected:
                    if not select_filter:
                        select_filter = True
                    else:
                        row.selected = False
            # Rellenar los campos con los datos de la fila seleccionada
            for row in dt_factura.rows:
                if row.selected:
                    select_product_instance.select_cliente_field.value = row.data[0]
                    precio.value = str(row.data[1])
                    cantidad.value = str(row.data[2])
                    # Actualizar el precio seleccionado en el estado
                    States.selected_product_price = str(row.data[1])
            dt_factura.rows = [row for row in dt_factura.rows if not row.selected]
            actualizar_totales()
            page.update()

        btn_editar = ft.TextButton(
            "Editar",
            style= ft.ButtonStyle(color= "#2c78d0", text_style= ft.TextStyle(weight= ft.FontWeight.BOLD)),
            on_click= click_editar
            )
        
        def click_borrar(e):
            # Filtrar las filas que NO están seleccionadas
            dt_factura.rows = [row for row in dt_factura.rows if not row.selected]
            actualizar_totales()
            page.update()
        
        btn_borrar = ft.TextButton(
            "Borrar",
            style= ft.ButtonStyle(color= "#d52525", text_style= ft.TextStyle(weight= ft.FontWeight.BOLD)),
            on_click= click_borrar
            )

        def on_select_row(e):
            # Cambiar el estado de selección de la fila
            e.control.selected = not e.control.selected
            # Actualizar la vista
            page.update()

        dt_factura = ft.DataTable(
            columns= [
                ft.DataColumn(ft.Text("Producto", weight= ft.FontWeight.BOLD), heading_row_alignment= ft.MainAxisAlignment.CENTER),
                ft.DataColumn(ft.Text("Precio", weight= ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Qty", weight= ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Precio + Tasa", weight= ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Importe", weight= ft.FontWeight.BOLD)),
            ],
            rows= [],
            show_checkbox_column= True,
            heading_row_height= 40,
            data_row_max_height= 45
        )

        btn_guardar_otra = ft.OutlinedButton(
            "Guardar y otra",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            
        )

        btn_guardar = ft.ElevatedButton(
            "Guardar",
            style= ft.ButtonStyle(bgcolor= "#2c78d0", color= "white", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
        )

        btn_cancelar = ft.OutlinedButton(
            "Cancelar",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#6d6d6d"), color= "#6d6d6d", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
        )

        def chk_descuento_changed(e):
            if e.control.value:
                column_descuento.controls[1].visible = True
                descuento.disabled = False
                txt_subtotal.visible = True
                txt_subtotal_value.visible = True
                txt_descuento.visible = True
                txt_descuento_value.visible = True
            else:
                column_descuento.controls[1].visible = False
                descuento.disabled = True
                txt_subtotal.visible = False
                txt_subtotal_value.visible = False
                txt_descuento.visible = False
                txt_descuento_value.visible = False
            actualizar_totales()
            page.update()

        chk_descuento = ft.Checkbox(
            label="Descuento",
            on_change= chk_descuento_changed,
        )

        def descuento_changed(e):
            actualizar_totales()
            page.update()

        descuento = ft.TextField(
            width= 90,
            bgcolor= inputs_bgcolor,
            border_width= 0,
            height= 25,
            hover_color= inputs_bgcolor,
            text_size= 14,
            cursor_height= 14,
            text_vertical_align= -1.0,
            content_padding= ft.padding.only(top= 0, bottom=0, left=10, right=5),
            value= "10",
            disabled= True,
            on_change= descuento_changed
        )

        txt_porciento_descuento = ft.Text("Porciento")

        def sw_descuento_changed(e):
            actualizar_totales()
            page.update()

        sw_descuento = ft.Switch(
            value=False,
            height= 20,
            inactive_thumb_color= "white",
            inactive_track_color= "#36618E",
            on_change= sw_descuento_changed
        )
        txt_catidad_descuento = ft.Text("Cantidad")

        txt_subtotal = ft.Text("Subtotal:", size= 18, visible= False)
        txt_descuento = ft.Text("Descuento:", size= 18, visible= False)
        txt_total = ft.Text(f"Total {radio_monedas.value.upper()}:", weight= "bold", size= 18)

        txt_subtotal_value = ft.Text("0.00", size= 18, visible= False)
        txt_descuento_value = ft.Text("0.00", size= 18, visible= False)
        txt_total_value = ft.Text("0.00", weight= "bold", size= 18)

        ## Widgets objects>
        # Controls>

        # <Functions
        
        def porciento_fiscal(tasa) -> float:
            coeficiente = "1." + tasa.controls[1].value.replace("%","")
            return float(coeficiente)
        
        def recalcular_monedas():
            pass

        def actualizar_totales():
            from decimal import Decimal
            
            subtotal = Decimal("0")

            for row in dt_factura.rows:
                subtotal += Decimal(row.data[4])
            
            descuento_total = float(subtotal) * float(descuento.value) / 100
            
            txt_subtotal_value.value = f"{subtotal:,.2f}"
            txt_descuento_value.value = f"{descuento_total:,.2f}"
            # txt_total_value.value = f"{subtotal:,.2f}" if not chk_descuento.value else f"{(subtotal - descuento_total):,.2f}"
            print(f"Descuento: {descuento_total}")

        # Functions>

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
            margin= ft.margin.only(left= 25, right=25, top=10),
            padding= ft.padding.all(25)
        )

        Row_finanzas1 = ft.Row(
            controls=[
                ft.Icon(ft.Icons.CURRENCY_EXCHANGE),
                txt_finanzas_title
            ]
            )
        
        Row_finanzas2 = ft.Container(
            content= ft.Row(
            controls=[
                cup_tasa,
                ft.Container(width=10), # Divisor
                mlc_tasa,
                ft.Container(width=40), # Divisor
                tasa_fiscal
            ],
            ),
            margin= ft.margin.only(top= 5)
        )

        column_financiera = ft.Column(
            controls=[
                Row_finanzas1,
                Row_finanzas2,
            ]
        )
        contenedor_finanzas = ft.Container(
            content= column_financiera,
            bgcolor= ft.Colors.WHITE,
            border= ft.border.all(1, "#CBD5E1"),
            border_radius= ft.border_radius.all(5),
            margin= ft.margin.only(left= 25, right=25, top=10),
            padding= ft.padding.all(25)
        )

        Row_add_product1 = ft.Row(
            controls=[
                ft.Icon(ft.Icons.RECEIPT),
                txt_title_add_product,
                btn_new_product
            ]
            )
        
        Row_add_product2 = ft.Row(
            controls=[
                select_product,
                cantidad,
                precio,
                btn_add_product
            ],
            expand= True
            )

        column_add_product = ft.Column(
            controls=[
                Row_add_product1,
                Row_add_product2
            ]
        )
        contenedor_add_product = ft.Container(
            content= column_add_product,
            bgcolor= ft.Colors.WHITE,
            border= ft.border.all(1, "#CBD5E1"),
            border_radius= ft.border_radius.all(5),
            margin= ft.margin.only(left= 25, right=25, top=10),
            padding= ft.padding.all(25)
        )

        row_editar_product_table = ft.Row(
            controls=[
                btn_editar,
                btn_borrar
            ],
            alignment= ft.MainAxisAlignment.START,
            spacing= 0
        )

        contenedor_editar_product_table = ft.Container(
            content= row_editar_product_table,
            margin= ft.margin.only(left= 25, right=25, top=10),
        )

        contenedor_tabled_products = ft.Container(
            content= dt_factura,
            bgcolor= ft.Colors.WHITE,
            border= ft.border.all(1, "#CBD5E1"),
            border_radius= ft.border_radius.all(5),
            margin= ft.margin.only(left= 25, right=25, top=10),
            # padding= ft.padding.all(25)
        )

        factura_body = ft.ListView(
            controls=[
                contenedor_info,
                contenedor_finanzas,
                contenedor_add_product,
                contenedor_editar_product_table,
                contenedor_tabled_products
            ],
            expand= True
        )

        column_descuento = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        chk_descuento,
                        descuento
                    ]
                ),
                ft.Row(
                    controls=[
                        txt_porciento_descuento,
                        sw_descuento,
                        txt_catidad_descuento
                    ],
                    visible= False
                )
            ],
            spacing= 0
        )

        Row_footer = ft.Container(
            content= ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls= [btn_guardar_otra, btn_guardar]
                            ),
                            ft.Row(controls= [btn_cancelar]),
                        ]
                    ),
                    ft.Column(expand= True), # Espaciador
                    ft.Column(
                        controls=[
                            ft.Container(
                                content= column_descuento,
                                border= ft.border.all(2, "black"),
                                border_radius= ft.border_radius.all(5),
                                padding= ft.padding.all(10),
                                # height= 78,
                                margin= ft.margin.only(right= 30)
                            )
                        ]
                    ),
                    ft.Column(
                        controls=[
                                    txt_subtotal,
                                    txt_descuento,
                                    txt_total,
                                ],
                        horizontal_alignment= ft.CrossAxisAlignment.END,
                        alignment= ft.MainAxisAlignment.START,
                        spacing= 0
                    ),
                    ft.Column(
                        controls=[
                                    txt_subtotal_value,
                                    txt_descuento_value,
                                    txt_total_value,
                                ],
                        horizontal_alignment= ft.CrossAxisAlignment.END,
                        alignment= ft.MainAxisAlignment.START,
                        spacing= 0
                    ),
                ],
                expand= True,
                vertical_alignment= ft.CrossAxisAlignment.START,
        ),
            margin= ft.margin.only(left= 25, right=25)
        )
        
        

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[contenedor_title, factura_body, Row_footer], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>