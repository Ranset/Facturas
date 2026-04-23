from flet_base import flet_instance as ft
from decimal import Decimal
from typing import Optional
from controller import (
                        delete_factura,
                        add_cliente,
                        update_cliente,
                        add_producto,
                        update_producto,
                        convertir_de_mxm_a_usd
                        )
from pages.common_controls.states import States

class CustomTextDatePicker(ft.TextField):
    def __init__(self, page: ft.Page, label: Optional[str] = None):
        super().__init__()

        self.select_fecha_inicio = ft.TextField(label= label, 
                                                suffix_icon= ft.Icons.CALENDAR_TODAY, 
                                                width= 145,
                                                bgcolor= ft.Colors.WHITE,
                                                border_color= ft.Colors.GREY_400,
                                                hover_color= ft.Colors.WHITE,
                                                on_click= lambda e: page.open(ft.DatePicker(on_change= self.poner_fecha))
                                                )

    def Crear(self):
        return self.select_fecha_inicio

    def poner_fecha(self, e):
        self.select_fecha_inicio.value = e.control.value.strftime("%d/%m/%Y")
        try:
            self.select_fecha_inicio.update()
        except Exception:
            pass


class CustomTextFieldAutocomplete(ft.Stack):
    def __init__(self, page: ft.Page, label: str, suggestions: list):
        super().__init__()

        def on_suggestion_click(value, price):
            from pages.common_controls.states import States
            self.select_cliente_field.value = value
            States.selected_product_price = str(price)
            try:
                self.select_cliente_field.update()
            except Exception:
                pass
            suggestions_container.visible = False
            # move wrapper back from overlay to the stack if needed
            try:
                if overlay_wrapper in page.overlay:
                    try:
                        page.overlay.remove(overlay_wrapper)
                    except Exception:
                        pass
                if overlay_wrapper not in self.select_cliente.controls:
                    self.select_cliente.controls.append(overlay_wrapper)
            except Exception:
                pass
            self.select_cliente_field.focus()
            page.update()

        def on_cliente_change(e):
            txt = e.control.value or ""
            if not txt:
                suggestions_container.content = ft.Column(controls=[])
                suggestions_container.visible = False
                page.update()
                return
            matches = [c for c in suggestions if txt.lower() in c[0].lower()]
            controls = []
            for m in matches:
                controls.append(
                    ft.Container(
                        content=ft.GestureDetector(
                            on_tap=lambda ev, v=m: on_suggestion_click(v[0], v[1]),
                            content=ft.Container(content=ft.Text(m[0])),
                        ),
                        padding=ft.padding.only(left=6, right=6),
                    )
                )
            suggestions_container.content = ft.Column(controls=controls)
            suggestions_container.visible = len(controls) > 0

            # if visible, move the overlay wrapper to page.overlay so it receives events
            try:
                if suggestions_container.visible:
                    # remove from stack controls if present
                    if overlay_wrapper in self.select_cliente.controls:
                        try:
                            self.select_cliente.controls.remove(overlay_wrapper)
                        except Exception:
                            pass
                    # add to page.overlay if not present
                    if overlay_wrapper not in page.overlay:
                        try:
                            page.overlay.append(overlay_wrapper)
                        except Exception:
                            try:
                                page.overlay.add(overlay_wrapper)
                            except Exception:
                                pass
                else:
                    # hide: ensure wrapper is back in stack
                    if overlay_wrapper in page.overlay:
                        try:
                            page.overlay.remove(overlay_wrapper)
                        except Exception:
                            pass
                    if overlay_wrapper not in self.select_cliente.controls:
                        self.select_cliente.controls.append(overlay_wrapper)
            except Exception:
                pass

            page.update()

        self.select_cliente_field = ft.TextField(
            label=label,
            expand=True,
            on_change=on_cliente_change,
            border_color= ft.Colors.GREY_400,
        )

        suggestions_container = ft.Container(
            content=ft.Column(controls=[]),
            visible=False,
            bgcolor="white",
            border=ft.border.all(1, "#cccccc"),
            padding=ft.padding.only(top=2, bottom=2),
            ignore_interactions=False,
        )


        # wrapper used both inside the Stack and (temporarily) in page.overlay
        # set a fixed width for the field+overlay so suggestions match field width
        field_overlay_width = 300
        # left_position = page.window.width / 2
        right_position = 20
        overlay_wrapper = ft.Container(content=suggestions_container, right=right_position, bottom=20, width=field_overlay_width)

        # Exponer referencias como atributos de instancia para manejar foco/overlay
        self.page = page
        self.overlay_wrapper = overlay_wrapper
        self.suggestions_container = suggestions_container

        # show suggestions as an overlay so they don't change the Row2 height
        self.select_cliente = ft.Stack(
            controls=[
                # base: the text field
                ft.Container(content=self.select_cliente_field),
                # overlay wrapper: moved to page.overlay when visible
                overlay_wrapper,
            ],
            clip_behavior=ft.ClipBehavior.NONE,
            width=field_overlay_width,
            expand=True,
        )

    def Crear(self):
        return self.select_cliente
    
    def focus_field(self, delay_ms: int = 50):
        self.select_cliente_field.focus()
        

class Tabla_Factura_Row(ft.Column):
    def __init__(self, estado: str, fecha: str, numero: str, cliente: str, total: str, moneda: str, page: ft.Page):
        super().__init__()

        self.estado = estado
        self.page = page

        self.tabla_row = ft.Column(
            alignment= ft.MainAxisAlignment.START,
            spacing= 0,
            controls=[
                ft.Row(
            controls=[
                    ft.Container(
                        content= ft.Text(
                            value= estado,
                            color= ft.Colors.WHITE,
                        ),
                        bgcolor= self._color_estado(),
                        alignment= ft.alignment.center,
                        border_radius= ft.border_radius.all(8),
                        width= 70,
                        height= 20,
                        margin= ft.margin.only(left= 15),
                        on_click= lambda e: print(f"Clic en factura {numero}")
                        ),
                    ft.Container(
                        content= ft.Text(fecha),
                        width= 80,
                        margin= ft.margin.only(left= 15),
                    ),
                    ft.Container(
                        content= ft.Text(numero),
                        width= 80,
                        margin= ft.margin.only(left= 15)
                    ),
                    ft.Container(
                        content= ft.Text(cliente, no_wrap= True, overflow= "ellipsis"),
                        expand= 4,
                        on_click= lambda e: print(f"Clic en factura {numero}")
                    ),
                    ft.Container(
                        content= ft.Text(self.formatear_con_comas(total)),
                        width= 200,
                        margin= ft.margin.only(left= 20)
                    ),
                    ft.Container(
                        content= ft.Text(moneda),
                        width= 50,
                        margin= ft.margin.only(left= 15)
                    ),
                    ft.Container(
                        content= ft.TextButton(text="Facturar"),
                        width= 80
                    ),
                    ft.Container(
                        content= ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem("Borrador", height= 10),
                                ft.PopupMenuItem("Enviada", height= 10),
                                ft.PopupMenuItem("Facturar", height= 10),
                                ft.PopupMenuItem(
                                    content= ft.Column(controls=[
                                        ft.Divider(height=8, color= "#ECEEF4"),
                                        ft.Text("PDF"),
                                    ], alignment= ft.alignment.top_center, spacing=0),
                                    height= 10),
                                ft.PopupMenuItem(
                                    content= ft.Column(controls=[
                                        ft.Divider(height=8, color= "#ECEEF4"),
                                        ft.Text("Eliminar", color= ft.Colors.RED),
                                    ], alignment= ft.alignment.top_center, spacing=0),
                                    height= 10,
                                    on_click= lambda e: self.modal(numero, page)
                                ),
                            ],
                            tooltip= "",
                            icon= ft.Icons.ARROW_DROP_DOWN_OUTLINED
                        ),
                        width= 40
                    ),
            ],
            height= 33,
            expand= True,
            alignment= ft.MainAxisAlignment.START,
            spacing= 0
        ),
        ft.Divider(height=0)
            ]
        )

    def _color_estado(self):
        colores_de_estados = {
            "Vencida": "#CA1414",
            "Borrador": "#CA1414",
            "Enviada": "#2c78d0",
            "Pagada": "#028A0E",
            "XEnviar": "#CA1414",
        }
        return colores_de_estados[self.estado]

    def formatear_con_comas(self, texto_numero):
        # 1. Convertimos el string a Decimal para evitar errores
        numero = Decimal(texto_numero)
        
        # 2. Aplicamos formato:
        # ,  -> Agrega la coma de miles
        # .2f -> Asegura siempre 2 decimales (fixed point)
        return f"${numero:,.2f}"
    
    def eliminar(self, factura_number, modal_dialog: ft.AlertDialog):
        from router import show_view
        from pages.common_controls.states import States
        eliminar_factura = delete_factura(factura_number)
        modal_dialog.open = False  # Cerrar el diálogo
        if eliminar_factura["Success"]:
            if States.where_i_am == States._inicio_location:
                show_view(self.page, "inicio")
            if States.where_i_am == States._factura_location or States.where_i_am == States._cotizacion_location:
                show_view(self.page, "factura")
        print(eliminar_factura)
    
    def modal(self, factura_number, page: ft.Page):
        def cerrar_modal(e):
            modal_dialog.open = False  # Cerrar el diálogo
            page.update()

        modal_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmación", weight= "bold"),
            content=ft.Text("¿Realmente desea eliminar esta factura/cotización?"),
            actions=[
                ft.TextButton("Si", on_click=lambda e: self.eliminar(factura_number, modal_dialog)),
                ft.TextButton("No", on_click=cerrar_modal),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        page.overlay.append(modal_dialog) # Agregar el diálogo a la superposición de la página
        modal_dialog.open = True   # Abrirlo
        page.update()


    def crear(self):
        return self.tabla_row
    

class Menu(ft.Column):
    def __init__(self):
        super().__init__()

        from pages.common_controls.states import States

        # <Functions
        def click_inicio(e):
            from router import show_view
            States.where_i_am = States._inicio_location
            show_view(States.states_page[0], States._inicio_location)

        def click_cotizacion(e):
            from router import show_view
            States.where_i_am = States._cotizacion_location
            show_view(States.states_page[0], States._cotizacion_location)

        def click_factura(e):
            from router import show_view
            States.where_i_am = States._factura_location
            show_view(States.states_page[0], States._factura_location)

        def click_clientes(e):
            from router import show_view
            States.where_i_am = States._cliente_location
            show_view(States.states_page[0], States._cliente_location)

        def click_productos(e):
            from router import show_view
            States.where_i_am = States._producto_location
            show_view(States.states_page[0], States._producto_location)
        
        def click_configuracion(e):
            from router import show_view
            States.where_i_am = States._configuracion_location
            show_view(States.states_page[0], States._configuracion_location)

        def click_acerca(e):
            from router import show_view
            States.where_i_am = States._acerca_location
            show_view(States.states_page[0], States._acerca_location)

        # Functions>

        # Controls
        ## common variables
        styles_btn_menu = ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0), 
                alignment= ft.Alignment(-1,0),
                padding= ft.padding.only(left= 30)
                )
        with_btn_menu = 200
        bgcolor_btn_menu = '#222a31'
        bgcolor_btn_menu_active = '#2c78d0'

        ## Controls
        btn_inicio_menu = ft.FilledButton(
            text="Inicio",
            icon=ft.Icons.HOME,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == "inicio" else bgcolor_btn_menu,
            on_click= click_inicio
        )

        btn_cotizaciones_menu = ft.FilledButton(
            text="Cotizaciones",
            icon=ft.Icons.DESCRIPTION,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == "cotizacion" else bgcolor_btn_menu,
            on_click= click_cotizacion
        )

        btn_facturas_menu = ft.FilledButton(
            text="Facturas",
            icon=ft.Icons.REQUEST_QUOTE,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == "factura" else bgcolor_btn_menu,
            on_click= click_factura
        )

        btn_clientes_menu = ft.FilledButton(
            text="Clientes",
            icon=ft.Icons.PERSON,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == States._cliente_location else bgcolor_btn_menu,
            on_click= click_clientes
        )

        btn_productos_menu = ft.FilledButton(
            text="Productos",
            icon=ft.Icons.INVENTORY_2,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == States._producto_location else bgcolor_btn_menu,
            on_click= click_productos
        )

        btn_configuracion_menu = ft.FilledButton(
            text="Configuración",
            icon=ft.Icons.SETTINGS,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == States._configuracion_location else bgcolor_btn_menu,
            on_click= click_configuracion
        )

        btn_acerca_menu = ft.FilledButton(
            text="Acerca de",
            icon=ft.Icons.INFO,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == States._acerca_location else bgcolor_btn_menu,
            on_click= click_acerca
        )

        # Layout
        ## Menu Lateral
        menu = ft.Column(
            controls= [
                btn_inicio_menu, 
                btn_cotizaciones_menu,
                btn_facturas_menu,
                btn_clientes_menu,
                btn_productos_menu,
                btn_configuracion_menu,
                btn_acerca_menu,
                ],
            expand= True,
            tight= True,
            alignment= ft.MainAxisAlignment.START,
            spacing= 4,
            )
        self.contenedor_menu = ft.Container(
            content=menu,
            bgcolor= '#222a31', 
            expand= True,
            width= 190,
            padding= ft.padding.only(top= 30)
            )

    def Crear(self):
        return self.contenedor_menu
        print("Menu redraw")


class NewClientDialog(ft.AlertDialog):
    def __init__(self, page: ft.Page, id = None, nombre = None, NIT = None, REEUP = None, ONIE = None, Domicilio = None, nro_cta_CUP = None, nro_cta_MLC = None, telefono = None, correo = None):
        super().__init__()

        def keyboard_event_handler(e):
            if e.ctrl and e.key.lower() == "g":
                click_guardar_y_otro(e)

        page.on_keyboard_event = keyboard_event_handler

        # 1. Definir el diálogo
        txt_error = ft.Text(
                            "El campo nombre es obligatorio",
                            color= ft.Colors.RED,
                            visible= False
                            )

        txt_nombre = ft.CupertinoTextField(
                            placeholder_text="Nombre Comercial", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 600,
                            expand= True,
                            value= nombre if nombre else "",
                            autofocus= True,
                            on_submit= lambda e: click_guardar(e)
                            )

        self.txt_del_nit = ""
        
        def rellenar_formato_NIT(e):
            # Obtener el texto actual sin los caracteres de la máscara (_)
            # Esto asume que el usuario solo escribe números o letras, no '_'
            texto_limpio = e.control.value.replace("_", "")
            self.txt_del_nit += texto_limpio
            
            # Limitar la longitud a 11
            if len(self.txt_del_nit) > 11:
                self.txt_del_nit = self.txt_del_nit[:11]
                
            # Calcular cuántos guiones bajos faltan
            faltantes = 11 - len(self.txt_del_nit)
            
            # Actualizar el valor del textfield con la máscara
            e.control.value = self.txt_del_nit + ("_" * faltantes)
            
            # Mover el cursor al final de la entrada actual (opcional pero recomendado)

            
            txt_nit.update()

        def clear_txt_nit(e):
            txt_nit.value = ""
            txt_nit.update()
        
        txt_nit = ft.CupertinoTextField(
                            placeholder_text="NIT", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            expand= True,
                            value= NIT if NIT else "",
                            on_submit= lambda e: click_guardar(e),
                            input_filter= ft.InputFilter(allow=True, regex_string=r"^\d{0,11}$", replacement_string=""), # Solo números y máximo 11 dígitos
                            on_change= rellenar_formato_NIT,
                            text_align=ft.TextAlign.LEFT,
                            # Botón para limpar el TextField
                            suffix=ft.IconButton(
                                icon= ft.Icons.CLEAR, # Icono de 'X' para limpiar
                                icon_color= ft.Colors.GREY_400,
                                on_click= lambda e: clear_txt_nit(e)  # Llama a la función al hacer clic
                            )
                        )
        
        txt_reeup = ft.CupertinoTextField(
                            placeholder_text="REEUP", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            expand= True,
                            value= REEUP if REEUP else "",
                            on_submit= lambda e: click_guardar(e)
                            )
        
        txt_onie = ft.CupertinoTextField(
                            placeholder_text="ONIE", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            expand= True,
                            value= ONIE if ONIE else "",
                            on_submit= lambda e: click_guardar(e)
                            )
        
        txt_domicilio = ft.CupertinoTextField(
                            placeholder_text="Domcilio", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 600,
                            expand= True,
                            value= Domicilio if Domicilio else "",
                            on_submit= lambda e: click_guardar(e)
                            )
        
        txt_cta_cup = ft.CupertinoTextField(
                            placeholder_text="# de Cuenta CUP", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            expand= True,
                            value= nro_cta_CUP if nro_cta_CUP else "",
                            on_submit= lambda e: click_guardar(e),
                            input_filter= ft.InputFilter(allow=True, regex_string=r"^[0-9]*$", replacement_string="") # Solo números
                            )
        
        txt_cta_mlc = ft.CupertinoTextField(
                            placeholder_text="# de Cuenta MLC", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            expand= True,
                            value= nro_cta_MLC if nro_cta_MLC else "",
                            on_submit= lambda e: click_guardar(e),
                            input_filter= ft.InputFilter(allow=True, regex_string=r"^[0-9]*$", replacement_string="") # Solo números
                            )
        
        txt_telefono = ft.CupertinoTextField(
                            placeholder_text="Teléfono", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            expand= True,
                            value= telefono if telefono else "",
                            on_submit= lambda e: click_guardar(e),
                            input_filter= ft.InputFilter(allow=True, regex_string=r"^\+?\d+$", replacement_string=""), # Solo números y opcionalmente un + al inicio para códigos internacionales
                            )
        
        txt_email = ft.CupertinoTextField(
                            placeholder_text="Email", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            value= correo if correo else "",
                            on_submit= lambda e: click_guardar(e),
                            )
        
        def validar_campos():
            '''Valida que el campo nombre no esté vacío antes de guardar'''
            if not txt_nombre.value.strip():
                return False
            else:
                return True

        
        def click_guardar(e):            
            from pages.common_controls.states import States
            from router import show_view

            if not validar_campos():
                txt_error.visible = True
                page.update()
            else:
                if id is not None:
                    actualizar_cliente(e)
                else:
                    guardar(e)
                if States.where_i_am != States._formulario_factura_location:
                    self.alert_dialog.open = False
                    show_view(page, States.where_i_am)
                else:
                    self.alert_dialog.open = False
                    page.update()

        def click_guardar_y_otro(e):            
            from pages.common_controls.states import States
            from router import show_view

            if not validar_campos():
                txt_error.visible = True
                page.update()
            else:
                if id is not None:
                    actualizar_cliente(e)
                else:
                    guardar(e)
                
                # Limpiar campos para nuevo ingreso
                txt_nombre.value = ""
                txt_nit.value = ""
                txt_reeup.value = ""
                txt_onie.value = ""
                txt_domicilio.value = ""
                txt_cta_cup.value = ""
                txt_cta_mlc.value = ""
                txt_telefono.value = ""
                txt_email.value = ""
                txt_error.visible = False
                txt_nombre.focus()  # Volver a enfocar el campo nombre para agilizar ingreso

                show_view(page, States.where_i_am)
        
        def guardar(e):
            add_cliente(cliente_data= {
                "nombre": txt_nombre.value,
                "NIT": txt_nit.value,
                "REEUP": txt_reeup.value,
                "ONIE": txt_onie.value,
                "Domicilio": txt_domicilio.value,
                "nro_cta_CUP": txt_cta_cup.value,
                "nro_cta_MLC": txt_cta_mlc.value,
                "telefono": txt_telefono.value,
                "correo": txt_email.value,
            })

        def actualizar_cliente(e):
            cliente_data = {
                "nombre": txt_nombre.value,
                "NIT": txt_nit.value,
                "REEUP": txt_reeup.value,
                "ONIE": txt_onie.value,
                "Domicilio": txt_domicilio.value,
                "nro_cta_CUP": txt_cta_cup.value,
                "nro_cta_MLC": txt_cta_mlc.value,
                "telefono": txt_telefono.value,
                "correo": txt_email.value,
            }

            update_cliente(id, cliente_data)
            
        
        btn_guardar = ft.ElevatedButton(
            "Guardar",
            style= ft.ButtonStyle(bgcolor= "#2c78d0", color= "white", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_guardar
        )

        def cerrar_dialogo(e):
            self.alert_dialog.open = False
            page.update()
            page.overlay.clear()
        
        btn_cancelar = ft.OutlinedButton(
            "Canelar",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= cerrar_dialogo
        )

        btn_guardar_otra = ft.OutlinedButton(
            content= ft.Row(
                [
                    ft.Text(
                        spans= [
                            ft.TextSpan("G", style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)), # Subrayar la "G" para indicar el atajo de teclado
                            ft.TextSpan("uardar y Otro"),
                        ]
                    )
                ]
            ),
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_guardar_y_otro
        )

        row_1 = ft.Row(controls= [txt_nombre], expand= True,)
        row_2 = ft.Row(controls= [txt_nit, txt_reeup, txt_onie], expand= True)
        row_3 = ft.Row(controls= [txt_domicilio], expand= True)
        row_4 = ft.Row(controls= [txt_cta_cup, txt_cta_mlc, txt_telefono], expand= True)
        row_5 = ft.Row(
            controls= [
                txt_email,
                ft.Row(expand= True), # Divisor expansor
                btn_guardar,
                btn_guardar_otra,
                btn_cancelar,
                ], 
                expand= True
                )

        self.alert_dialog = ft.AlertDialog(
            title=ft.Text("Agregar Cliente", weight= "bold"),
            content=ft.Column(
                controls= [
                    txt_error,
                    row_1,
                    row_2,
                    row_3,
                    row_4,
                    row_5
                ],
                alignment= ft.MainAxisAlignment.START,
                spacing= 0,
                height= 250,
            ),
            on_dismiss= cerrar_dialogo,
        )

    def Crear(self):
        return self.alert_dialog
    

class NewProductDialog(ft.AlertDialog):
    def __init__(self, page: ft.Page, id = None, nombre = None, proveedor = None, precio = None, peso = None):
        super().__init__()

        def keyboard_event_handler(e):
            if e.key == "Enter":
                click_guardar(e)
            if e.ctrl and e.key.lower() == "g":
                click_guardar_y_otro(e)

        page.on_keyboard_event = keyboard_event_handler

        # 1. Definir el diálogo
        txt_error = ft.Text(
                    "El campo nombre es obligatorio",
                    color= ft.Colors.RED,
                    visible= False
                    )
        
        txt_nombre = ft.CupertinoTextField(
                            placeholder_text="Producto", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 600,
                            expand= True,
                            value= nombre if nombre else "",
                            autofocus= True,
                            )
        
        txt_precio = ft.CupertinoTextField(
                            placeholder_text="Precio", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            expand= True,
                            value= precio if precio else "",
                            )
        
        rdo_moneda = ft.Container(
            content= ft.Row(
                controls= [
                    ft.RadioGroup(
                        content= ft.Row(
                            [
                                ft.Radio(label= "USD", value="usd"),
                                ft.Radio(label= "MXN", value="mxn"),
                            ]
                        ),
                        value= "usd"
                    )
                ]
            ),
            border= ft.border.all(1, "grey"),
            border_radius= ft.border_radius.all(7),
            padding= ft.padding.only(right= 5),
            height= 40
        )

        chk_iva = ft.Checkbox(label= "Agregar IVA", value= False)
        
        txt_proveedor = ft.CupertinoTextField(
                            placeholder_text="Proveedor", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            expand= True,
                            value= proveedor if proveedor else "",
                            )
        
        txt_peso = ft.CupertinoTextField(
                            placeholder_text="Peso en Kg", 
                            placeholder_style= ft.TextStyle(
                                                    color= ft.Colors.GREY_500,
                                                    size= 14
                                                    ), 
                            width= 200,
                            value= peso if peso else "",
                            )
        
        def validar_campos():
            '''Valida que el campo nombre no esté vacío antes de guardar'''
            if not txt_nombre.value.strip():
                return False
            else:
                return True
        
        def click_guardar(e):
            from pages.common_controls.states import States
            from router import show_view
            if not validar_campos():
                txt_error.visible = True
                page.update()
            else:
                if id is not None:
                    actualizar_producto(e)
                else:
                    guardar(e)
                if States.where_i_am != States._formulario_factura_location:
                    self.alert_dialog.open = False
                    show_view(page, States.where_i_am)
                else:
                    self.alert_dialog.open = False
                    page.update()

        def click_guardar_y_otro(e):
            from pages.common_controls.states import States
            from router import show_view

            if not validar_campos():
                txt_error.visible = True
                page.update()
            else:
                if id is not None:
                    actualizar_producto(e)
                else:
                    guardar(e)
                
                # Limpiar campos para nuevo ingreso
                txt_nombre.value = ""
                txt_precio.value = ""
                txt_proveedor.value = ""
                txt_peso.value = ""
                # chk_iva.value = False # Decidí no resetear el checkbox ni la selección de moneda para agilizar ingreso de productos similares
                # rdo_moneda.content.controls[0].value = "usd" 
                txt_error.visible = False
                txt_nombre.focus()  # Volver a enfocar el campo nombre para agilizar ingreso

                show_view(page, States.where_i_am)

        def guardar(e):
            if chk_iva.value:
                txt_precio.value = str(float(txt_precio.value) * 1.16)

            if rdo_moneda.content.controls[0].value == "mxn":
                txt_precio.value = convertir_de_mxm_a_usd(float(txt_precio.value))["Monto USD"]

            add_producto(producto_data= {
                "nombre": txt_nombre.value,
                "precio": txt_precio.value if txt_precio.value else "0",
                "proveedor": txt_proveedor.value if txt_proveedor.value else "",
                "peso": txt_peso.value if txt_peso.value else "0",
            })

        def actualizar_producto(e):
            if chk_iva.value:
                txt_precio.value = str(float(txt_precio.value) * 1.16)

            if rdo_moneda.content.controls[0].value == "mxn":
                txt_precio.value = convertir_de_mxm_a_usd(float(txt_precio.value))["Monto USD"]

            product_data = {
                "nombre": txt_nombre.value,
                "precio": txt_precio.value,
                "proveedor": txt_proveedor.value,
                "peso": txt_peso.value,
            }

            update_producto(id, product_data)
        
        btn_guardar = ft.ElevatedButton(
            "Guardar",
            style= ft.ButtonStyle(bgcolor= "#2c78d0", color= "white", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_guardar
        )

        def cerrar_dialogo(e):
            self.alert_dialog.open = False
            page.update()
            page.overlay.clear()
        
        btn_cancelar = ft.OutlinedButton(
            "Canelar",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= cerrar_dialogo
        )

        btn_guardar_otra = ft.OutlinedButton(
            content= ft.Row(
                [
                    ft.Text(
                        spans= [
                            ft.TextSpan("G", style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)), # Subrayar la "G" para indicar el atajo de teclado
                            ft.TextSpan("uardar y Otro"),
                        ]
                    )
                ]
            ),
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_guardar_y_otro
        )

        row_1 = ft.Row(controls= [txt_nombre], expand= True,)
        row_2 = ft.Row(controls= [txt_precio, rdo_moneda, chk_iva, txt_proveedor], expand= True)
        row_3 = ft.Row(
            controls= [
                txt_peso,
                ft.Row(expand= True), # Divisor expansor
                btn_guardar,
                btn_guardar_otra,
                btn_cancelar,
                ], 
                expand= True
                )

        self.alert_dialog = ft.AlertDialog(
            title=ft.Text("Agregar Producto", weight= "bold"),
            content=ft.Column(
                controls= [
                    txt_error,
                    row_1,
                    row_2,
                    row_3
                ],
                alignment= ft.MainAxisAlignment.START,
                spacing= 0,
                height= 150,
            ),
            on_dismiss= cerrar_dialogo,
        )

    def Crear(self):
        return self.alert_dialog