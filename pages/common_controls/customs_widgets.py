from flet_base import flet_instance as ft
from decimal import Decimal
from typing import Optional

class CustomTextDatePicker(ft.TextField):
    def __init__(self, page: ft.Page, label: Optional[str] = None):
        super().__init__()

        self.select_fecha_inicio = ft.TextField(label= label, 
                                                suffix_icon= ft.Icons.CALENDAR_TODAY, 
                                                width= 145,
                                                bgcolor= ft.Colors.WHITE,
                                                border_color= ft.Colors.GREY_400,
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
    def __init__(self, estado: str, fecha: str, numero: str, cliente: str, total: str, moneda: str):
        super().__init__()

        self.estado = estado
    
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
                        content= ft.Text(cliente, no_wrap= True),
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
                                    height= 10
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
            "Borrador": "#4E4E4E",
            "Enviada": "#2c78d0",
            "Pagada": "#028A0E",
            "XEnviar": "#4E4E4E",
        }
        return colores_de_estados[self.estado]

    def formatear_con_comas(self, texto_numero):
        # 1. Convertimos el string a Decimal para evitar errores
        numero = Decimal(texto_numero)
        
        # 2. Aplicamos formato:
        # ,  -> Agrega la coma de miles
        # .2f -> Asegura siempre 2 decimales (fixed point)
        return f"${numero:,.2f}"


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
        )

        btn_productos_menu = ft.FilledButton(
            text="Productos",
            icon=ft.Icons.INVENTORY_2,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == States._producto_location else bgcolor_btn_menu,
        )

        btn_configuracion_menu = ft.FilledButton(
            text="Configuración",
            icon=ft.Icons.SETTINGS,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == States._configuracion_location else bgcolor_btn_menu,
        )

        btn_acerca_menu = ft.FilledButton(
            text="Acerca de",
            icon=ft.Icons.INFO,
            width=with_btn_menu,
            style= styles_btn_menu,
            bgcolor= bgcolor_btn_menu_active if States.where_i_am == States._acerca_location else bgcolor_btn_menu,
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