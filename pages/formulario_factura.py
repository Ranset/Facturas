from flet_base import flet_instance as ft
from datetime import datetime
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import CustomTextDatePicker, Tabla_Factura_Row, NewClientDialog, NewProductDialog, CustomTextFieldAutocomplete
from controller import get_clientes, get_configuration, get_productos, guardar_nueva_factura, get_factura_by_numero

class FormularioFactura(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        #  <Carga de datos
        clientes_data = get_clientes()
        clientes = []

        for cliente in clientes_data["Data"]:
            clientes.append([cliente["id"], cliente["nombre"]])

        configuracion = get_configuration()
        usd = 1
        cup = float(configuracion["Data"]["tasa_cup"])
        mlc = float(configuracion["Data"]["tasa_mlc"])
        tasa_fiscal = configuracion["Data"]["tasa_fiscal"]

        productos = get_productos()

        factura = None

        duplicated_data = None

        if States.factura_numero is not None: # Si es una edición de una factura
            factura = get_factura_by_numero(States.factura_numero)
            States.factura_numero = None # Limpiar el número de factura en el estado para evitar problemas al volver a cargar el formulario después de guardar una factura o cotización, ya que ese número solo se usa para editar facturas existentes, no para nuevas facturas

            if factura.tipo == 1:
                States.i_come_from = States._Crear_btn_loc_cotizacion
            elif factura.tipo == 2:
                States.i_come_from = States._Crear_btn_loc_facturas

            if factura.Moneda == "CUP":
                cup = factura.tasa_cambio
            elif factura.Moneda == "MLC":
                mlc = factura.tasa_cambio
            
            tasa_fiscal = factura.porciento_cta_fiscal
        elif States.duplicated_number is not None: # Si es una duplicación de una factura
            duplicated_data = get_factura_by_numero(States.duplicated_number)
            States.duplicated_number = None # Limpiar el número de factura en el estado para evitar problemas al volver a cargar el formulario después de guardar una factura o cotización, ya que ese número solo se usa para duplicar facturas existentes, no para nuevas facturas

            if duplicated_data.tipo == 1:
                States.i_come_from = States._Crear_btn_loc_cotizacion
            elif duplicated_data.tipo == 2:
                States.i_come_from = States._Crear_btn_loc_facturas

            if duplicated_data.Moneda == "CUP":
                cup = duplicated_data.tasa_cambio
            elif duplicated_data.Moneda == "MLC":
                mlc = duplicated_data.tasa_cambio
            
            tasa_fiscal = duplicated_data.porciento_cta_fiscal

        # <Fin Carga de datos

        # <Controls
        ## @note <common variables
        inputs_height = 48
        inputs_bgcolor = ft.Colors.WHITE
        inputs_border_color= ft.Colors.GREY_400

        self.price_multiply = 1.0

        tipo = 2 if States.i_come_from == States._Crear_btn_loc_facturas else 1 # 1 cotización, 2 factura

        ## common variables>

        ## @note <Widgets objects
        def title():
            if States.i_come_from == States._Crear_btn_loc_facturas:
                return "Crear Factura" if factura is None else f"Editar Factura #{factura.numero_factura}"
            if States.i_come_from == States._Crear_btn_loc_cotizacion:
                return "Crear Cotización" if factura is None else f"Editar Cotización #{factura.numero_factura}"
        
        txt_title = title()

        txt_formulario_title = ft.Text(
            txt_title,
            size= 20,
            weight= ft.FontWeight.BOLD,
            )

        txt_info_title = ft.Text("Información General", weight= ft.FontWeight.BOLD)

        select_cliente = ft.Dropdown(
            options=[
                ft.dropdown.Option(c[0], c[1]) for c in clientes
            ],
            label="Clientes",
            expand=True,
            enable_filter=True,
            editable=True,
            filled= True,
            fill_color= inputs_bgcolor,
            border_color= inputs_border_color,
            value= factura.Cliente if factura is not None else (duplicated_data.Cliente if duplicated_data is not None else None)
        )

        new_client_dialog = NewClientDialog(page).Crear()

        def abrir_dialogo(e):
            page.overlay.append(new_client_dialog) # Agregar el diálogo a la superposición de la página
            new_client_dialog.open = True   # Abrirlo
            page.update()

        btn_agragar_cliente = ft.FloatingActionButton(
            bgcolor= "#2c78d0",
            foreground_color= 'white',
            icon= ft.Icons.ADD,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
            on_click= abrir_dialogo
        )

        txt_moneda = ft.Text("Moneda:")

        def moneda_change(e):
            txt_total.value = f"Total {e.control.value.upper()}:"
            recalcular_monedas(e.control.value)

        radio_monedas = ft.RadioGroup(
            content= ft.Row(
            [
                ft.Radio(label= "CUP", value="cup"),
                ft.Radio(label= "MLC", value="mlc"),
                ft.Radio(label= "USD", value="usd"),
            ],
            ),
            on_change= moneda_change,
            value= str(factura.Moneda).lower() if factura is not None else (str(duplicated_data.Moneda).lower() if duplicated_data is not None else "cup"),
        )

        txt_pago = ft.Text("Pago:")

        cont_separador = ft.Container(expand= True)

        dd_pago = ft.Dropdown(
            options=[
                ft.DropdownOption("1", "Transferencia"),
                ft.DropdownOption("2", "Efectivo"),
            ],
            value= str(factura.metodo_pago) if factura is not None else (str(duplicated_data.metodo_pago) if duplicated_data is not None else "1"),
            border_color= ft.Colors.GREY_400,
        )

        txt_fecha = ft.Text("Fecha:")

        select_fecha_inicio = CustomTextDatePicker(page= page).Crear()
        select_fecha_inicio.value = factura.Fecha if factura is not None else datetime.now().strftime("%d/%m/%Y")

        txt_finanzas_title = ft.Text("Configuración financiera", weight= ft.FontWeight.BOLD)

        cup_tasa = ft.Row(
            controls=[
                ft.Text("CUP:"),
                ft.TextField(str(f"{cup:.2f}"),
                            border_color= ft.Colors.GREY_400,
                            width= 80,
                            on_change= lambda e: recalcular_monedas(radio_monedas.value)
                            )
            ]
        )
        
        mlc_tasa = ft.Row(
            controls=[
                ft.Text("MLC:"),
                ft.TextField(str(f"{mlc:.2f}"),
                            border_color= ft.Colors.GREY_400,
                            width= 80,
                            on_change= lambda e: recalcular_monedas(radio_monedas.value)
                            )
            ]
        )
        
        tasa_fiscal = ft.Row(
            controls=[
                ft.Text("Tasa Fiscal:"),
                ft.TextField(
                    str(tasa_fiscal),
                    suffix= ft.Text("%"),
                    border_color= ft.Colors.GREY_400,width= 80,
                    max_length= 2,
                    on_change= lambda e: recalcular_monedas(radio_monedas.value)
                )
            ]
        )

        txt_title_add_product = ft.Text("Agregar Producto", weight= ft.FontWeight.BOLD)

        new_prouct_dialog = NewProductDialog(page).Crear()

        def abrir_product_dialog(e):
            page.overlay.append(new_prouct_dialog) # Agregar el diálogo a la superposición de la página
            new_prouct_dialog.open = True   # Abrirlo
            page.update()

        btn_new_product = ft.ElevatedButton("Nuevo", bgcolor="#2c78d0", color= "white", width= 80, height= 25, on_click= abrir_product_dialog)

        product_suggestions = []

        for producto in productos["Data"]:
            product_suggestions.append((producto["nombre"], float(producto["precio"]), producto["moneda"], producto["iva"], producto["proveedor"], producto["peso"], producto["id"]))

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

        def click_add_product(e, product_name= None, product_price= None, product_qty= None):
            # Remover overlay si está presente
            if select_product_instance.overlay_wrapper in page.overlay:
                page.overlay.remove(select_product_instance.overlay_wrapper)
            # Validar entradas antes de crear la fila de producto
            nombre_producto = product_name if product_name is not None else select_product_instance.select_cliente_field.value
            if not nombre_producto:
                print("Nombre de producto vacío")
                return
            try:
                qty = product_qty if product_qty is not None else int(cantidad.value)
            except Exception:
                print("Cantidad inválida")
                return
            try:
                price = product_price if product_price is not None else float(precio.value)
            except Exception:
                print("Precio inválido")
                return
            # Precio segun moneda seleccionada
            if radio_monedas.value == "cup":
                self.price_multiply = float(cup_tasa.controls[1].value)
            elif radio_monedas.value == "mlc":
                self.price_multiply = float(mlc_tasa.controls[1].value)
            else:
                self.price_multiply = 1.0
            # Creando nueva fila de producto
            new_product = (nombre_producto, price, qty, price * porciento_fiscal(tasa_fiscal), qty * price * porciento_fiscal(tasa_fiscal))
            new_row = ft.DataRow(
                    [
                        ft.DataCell(ft.Text(new_product[0], no_wrap= True)),
                        ft.DataCell(ft.Text(Tabla_Factura_Row.formatear_con_comas(self,new_product[1]*self.price_multiply))),
                        ft.DataCell(ft.Text(str(new_product[2]))),
                        ft.DataCell(ft.Text(Tabla_Factura_Row.formatear_con_comas(self,new_product[3]*self.price_multiply))),
                        ft.DataCell(ft.Text(Tabla_Factura_Row.formatear_con_comas(self,new_product[4]*self.price_multiply))),
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

        def click_guardar_otra(e):
            from router import show_view
            i_come_before = States.i_come_from
            guardar = click_guardar(e) # Guardar la factura actual
            States.i_come_from = i_come_before # Restaurar el estado de dónde vengo para evitar problemas al volver a cargar el formulario
            if guardar is not False: # Si la factura se guardó correctamente, cargar un nuevo formulario
                show_view(page, States._formulario_factura_location) # Volver a cargar el formulario para crear otra factura

        btn_guardar_otra = ft.OutlinedButton(
            "Guardar y otra",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_guardar_otra,
            visible= True if factura is None else False # Solo mostrar el botón de "Guardar y otra" si no se está editando una factura existente, ya que tiene más sentido crear una nueva factura después de guardar una nueva que después de editar una existente
        )

        def click_duplicar(e):
            from router import show_view

            States.duplicated_number = factura.numero_factura
            show_view(page, States._formulario_factura_location)  # Redirigir al formulario de factura para mostrar la factura duplicada
        
        btn_duplicar = ft.OutlinedButton(
            "Duplicar",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_duplicar,
            visible= True if factura is not None else False # Solo mostrar el botón de "Duplicar" si se está editando una factura existente
        )

        def click_guardar(e):
            # 1. Validar que haya productos en la factura
            if len(dt_factura.rows) == 0:
                print("No hay productos en la factura")
                return False
            # 2. Validar que se haya seleccionado un cliente
            if not select_cliente.value:
                print("No se ha seleccionado un cliente")
                return False
            
            tipo_descuento = 0

            if chk_descuento.value:
                if not sw_descuento.value:
                    tipo_descuento = 1
                else:
                    tipo_descuento = 2

            tasa_de_cambio = 1.00

            if radio_monedas.value == "cup":
                tasa_de_cambio = cup_tasa.controls[1].value
            elif radio_monedas.value == "mlc":
                tasa_de_cambio = mlc_tasa.controls[1].value
            
            factura_data = {
                "cliente_id": select_cliente.value,
                "moneda": radio_monedas.value,
                "metodo_pago": int(dd_pago.value),
                "fecha": select_fecha_inicio.value,
                "tasa_cambio": tasa_de_cambio,
                "tasa_fiscal": tasa_fiscal.controls[1].value,
                "descuento": float(descuento.value) if descuento.value else 0.0,
                "descuento_tipo": tipo_descuento,
                "total": txt_total_value.value,
                "tipo": tipo,
                "productos": [
                    {
                        "nombre": row.data[0],
                        "precio": row.data[1],
                        "cantidad": row.data[2],
                        # "precio_con_tasa": row.data[3],
                        # "importe": row.data[4]
                    }
                    for row in dt_factura.rows
                ]
            }

            guardar_nueva_factura(factura_data)
            click_cancelar(e) # Volver a la vista anterior después de guardar

        btn_guardar = ft.ElevatedButton(
            "Guardar",
            style= ft.ButtonStyle(bgcolor= "#2c78d0", color= "white", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_guardar,
            visible= True if factura is None else False # Solo mostrar el botón de "Guardar" si no se está editando una factura existente
        )

        def click_cancelar(e):
            from router import show_view

            if States.i_come_from == States._Crear_btn_loc_cotizacion:
                States.where_i_am = States._cotizacion_location
                States.i_come_from = States._formulario_factura_location
                show_view(page, States._cotizacion_location)
            if States.i_come_from == States._Crear_btn_loc_facturas:
                States.where_i_am = States._factura_location
                States.i_come_from = States._formulario_factura_location
                show_view(page, States._factura_location)

        btn_cancelar = ft.OutlinedButton(
            "Cancelar",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#6d6d6d"), color= "#6d6d6d", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_cancelar
        )

        def click_actualizar(e):
            # El proceso de actualización es básicamente el mismo que el de guardar,
            # pero en lugar de crear una nueva factura, se actualiza la existente.
            # Para simplificar el código, se puede reutilizar la función de guardar
            # y simplemente pasar un parámetro adicional que indique que se trata de
            # una actualización y cuál es el ID de la factura a actualizar. Sin embargo,
            # para mantener la claridad, se implementará una función separada para la actualización.
            from controller import update_factura

            if factura is None:
                print("No hay factura para actualizar")
                return
            
            # Validar que haya productos en la factura
            if len(dt_factura.rows) == 0:
                print("No hay productos en la factura")
                return
            # Validar que se haya seleccionado un cliente
            if not select_cliente.value:
                print("No se ha seleccionado un cliente")
                return
            
            tipo_descuento = 0

            if chk_descuento.value:
                if not sw_descuento.value:
                    tipo_descuento = 1
                else:
                    tipo_descuento = 2

            tasa_de_cambio = 1.00

            if radio_monedas.value == "cup":
                tasa_de_cambio = cup_tasa.controls[1].value
            elif radio_monedas.value == "mlc":
                tasa_de_cambio = mlc_tasa.controls[1].value
            
            factura_data = {
                "id": factura.id,
                "cliente_id": select_cliente.value,
                "moneda": radio_monedas.value.upper(),
                "metodo_pago": int(dd_pago.value),
                "fecha": select_fecha_inicio.value,
                "tasa_cambio": tasa_de_cambio,
                "tasa_fiscal": tasa_fiscal.controls[1].value,
                "descuento": float(descuento.value) if descuento.value else 0.0,
                "descuento_tipo": tipo_descuento,
                "total": float(txt_total_value.value.replace(",", "")),
                "tipo": tipo,
                "estado": 2, # Asumimos que al actualizar una factura, esta pasa a estado "XEnviar" (2)
                "vendedor_id": 1, # Asumimos un vendedor fijo por simplicidad
                "productos": [
                    {
                        "nombre": row.data[0],
                        "precio": row.data[1],
                        "cantidad": row.data[2],
                    }
                    for row in dt_factura.rows
                ]
            }

            update_factura(factura.numero_factura, factura_data)
            click_cancelar(e) # Volver a la vista anterior después de actualizar

        btn_actualizar = ft.ElevatedButton(
            "Actualizar",
            style= ft.ButtonStyle(bgcolor= "#2c78d0", color= "white", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_actualizar,
            visible= True if factura is not None else False # Solo mostrar el botón de "Actualizar" si se está editando una factura existente
        )

        def chk_descuento_changed(e):
            checkbox = getattr(e, "control", None) or e # Manejar ambos casos: on_change pasa el control directamente, mientras que on_click pasa un evento con el control como atributo
            if checkbox.value:
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
            value= str(f"{factura.descuento:.2f}") if factura is not None else (str(f"{duplicated_data.descuento:.2f}") if duplicated_data is not None else "10"),
            disabled= True,
            on_change= descuento_changed
        )

        txt_porciento_descuento = ft.Text("Porciento")

        def sw_descuento_changed(e):
            actualizar_totales()
            page.update()

        sw_descuento = ft.Switch(
            value= True if factura is not None and factura.descuento_tipo == 2 else (True if duplicated_data is not None and duplicated_data.descuento_tipo == 2 else False),
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

        # @note <Functions
        
        def porciento_fiscal(tasa) -> float:
            clean_tasa = tasa.controls[1].value.replace("%","")
            delante = "1."
            if len(clean_tasa) == 1:
                clean_tasa = "0" + clean_tasa
            coeficiente = delante + clean_tasa
            return float(coeficiente)
        
        def recalcular_monedas(moeneda: str):
            if moeneda == "cup":
                self.price_multiply = float(cup_tasa.controls[1].value)
            elif moeneda == "mlc":
                self.price_multiply = float(mlc_tasa.controls[1].value)
            else:
                self.price_multiply = 1.0
            recargar_tabla()
            actualizar_totales()
            page.update()

        def recargar_tabla():
            for row in dt_factura.rows:
                # Recalcular los valores de la fila según la nueva moneda
                precio = row.data[1]
                qty = row.data[2]
                precio_con_tasa = precio * porciento_fiscal(tasa_fiscal)
                importe = qty * precio_con_tasa
                # Actualizar las celdas de la fila
                row.cells[1].content.value = Tabla_Factura_Row.formatear_con_comas(self,precio * self.price_multiply)
                row.cells[3].content.value = Tabla_Factura_Row.formatear_con_comas(self,precio_con_tasa * self.price_multiply)
                row.cells[4].content.value = Tabla_Factura_Row.formatear_con_comas(self,importe * self.price_multiply)
                row.data = (row.data[0], precio, qty, precio_con_tasa, importe)
            

        def actualizar_totales():
            subtotal = float("0")

            for row in dt_factura.rows:
                subtotal += float(row.data[4]) * float(self.price_multiply)
            
            if not sw_descuento.value and descuento.value != "":
                descuento_total = float(subtotal) * float(descuento.value) / 100
                txt_descuento.value = f"Descuento {descuento.value}%:"
            else:
                descuento_total = float(descuento.value) if descuento.value != "" else 0.0
                txt_descuento.value = "Descuento:"
            
            txt_subtotal_value.value = f"{subtotal:,.2f}"
            txt_descuento_value.value = f"{descuento_total:,.2f}"
            txt_total_value.value = f"{subtotal:,.2f}" if not chk_descuento.value else f"{(subtotal - float(descuento_total)):,.2f}"

        # Functions>

        # Agregar productos de la factura a la tabla si es una edición
        if factura is not None:
            from controller import get_facturas_products
            productos = get_facturas_products(factura.id)
            for producto in productos:
                click_add_product(e=None, product_name= producto.Nombre, product_price= float(producto.Precio_venta), product_qty= producto.Cantidad)
        
        if duplicated_data is not None:
            from controller import get_facturas_products
            productos = get_facturas_products(duplicated_data.id)
            for producto in productos:
                click_add_product(e=None, product_name= producto.Nombre, product_price= float(producto.Precio_venta), product_qty= producto.Cantidad)

        # @note <Layout

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
                # btn_agragar_cliente
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
                # btn_new_product
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
                                controls= [btn_duplicar, btn_guardar_otra, btn_guardar, btn_actualizar]
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
        
        

        # columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[contenedor_title, factura_body, Row_footer], expand= True)

        Row_generar = ft.Row(controls=[
            # columna_menu,
            column2
            ],
            alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>

        if factura is not None and factura.descuento_tipo > 0:
            chk_descuento.value = True
            chk_descuento_changed(chk_descuento) # Forzar la actualización del estado del descuento para mostrar los campos correspondientes
        
        if duplicated_data is not None and duplicated_data.descuento_tipo > 0:
            chk_descuento.value = True
            chk_descuento_changed(chk_descuento) # Forzar la actualización del estado del descuento para mostrar los campos correspondientes
