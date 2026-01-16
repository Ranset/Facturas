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
    where_i_am = _formulario_factura_location # Página actual

    i_come_from = _Crear_btn_loc_cotizacion # De donde viene flag