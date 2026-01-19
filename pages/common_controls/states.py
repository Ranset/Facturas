class States:

    # Pages
    _inicio_location = "inicio"
    _cotizacion_location = "cotizacion"
    _factura_location = "factura"
    _cliente_location = "cliente"
    _producto_location = "producto"
    _configuracion_location = "configuracion"
    _acerca_location = "acerca"

    _formulario_factura_location = "formulario_factura"

    _Crear_btn_loc_cotizacion = "btn_cotizacion_page" # Botón crear cotización de la página cotización
    _Crear_btn_loc_facturas = "btn_facturas_page" # Botón crear cotización de la página cotización

    # Variables
    where_i_am = _inicio_location # Página actual

    i_come_from = _Crear_btn_loc_cotizacion # De donde viene flag

    states_page = []

    # Inicializar la lista como variable de clase
    products_list: list = []

    selected_product_price = ""

    @classmethod
    def set_product_row(cls, index):
        cls.products_list.append(index)

    @classmethod
    def remove_product_row(cls, index):
        if index in cls.products_list:
            cls.products_list.remove(index)