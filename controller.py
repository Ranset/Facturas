from operator import or_

from models import (session, 
                    Tasa,
                    Tipo,
                    Factura,
                    DetalleFactura,
                    Cliente,
                    Producto,
                    Vendedor,
                    Config)

def get_facturas():
    facturas = session.query(Factura).filter(Factura.tipo == 2).all()
    clientes = get_clientes()
    lista_clientes = []

    for cliente in clientes["Data"]:
        cliente_dict = {
            "id": int(cliente["id"]),
            "nombre": cliente["nombre"],
        }
        lista_clientes.append(cliente_dict)

    tabla = []

    for factura in facturas:
        factura_dict = {
            "id": factura.id,
            "estado": factura.estado_rel.Estado,
            "fecha": factura.Fecha,
            "numero": factura.numero_factura,
            "cliente": factura.cliente.Nombre if factura.cliente else "Sin cliente",
            "total": f"{factura.total:.2f}",
            "moneda": factura.Moneda
        }
        tabla.append(factura_dict)

    data = {"nombre_clientes": lista_clientes, "datos_tabla": tabla}

    return {"Success": True, "Data": data}

def get_recientes_facturas():
    recientes_facturas = session.query(Factura).order_by(Factura.id.desc()).limit(5).all()

    para_tabla_resumen = []
    for factura in recientes_facturas:
        factura_tuple = (
            factura.estado_rel.Estado,
            factura.Fecha,
            factura.numero_factura,
            factura.cliente.Nombre if factura.cliente else "Sin cliente",
            f"{factura.total:.2f}",
            factura.Moneda
        )
        para_tabla_resumen.append(factura_tuple)
    
    return para_tabla_resumen

def get_cotizaciones():
    cotizaciones = session.query(Factura).filter(Factura.tipo == 1).all()
    clientes = get_clientes()
    lista_clientes = []

    for cliente in clientes["Data"]:
        cliente_dict = {
            "id": int(cliente["id"]),
            "nombre": cliente["nombre"],
        }
        lista_clientes.append(cliente_dict)

    tabla = []

    for cotizacion in cotizaciones:
        cotizacion_dict = {
            "id": cotizacion.id,
            "estado": cotizacion.estado_rel.Estado,
            "fecha": cotizacion.Fecha,
            "numero": cotizacion.numero_factura,
            "cliente": cotizacion.cliente.Nombre if cotizacion.cliente else "Sin cliente",
            "total": f"{cotizacion.total:.2f}",
            "moneda": cotizacion.Moneda
        }
        tabla.append(cotizacion_dict)

    data = {"nombre_clientes": lista_clientes, "datos_tabla": tabla}

    return {"Success": True, "Data": data}

def get_cotizaciones_por_enviar():
    cotizaciones_por_enviar = session.query(Factura).filter(Factura.tipo == 1, Factura.Estado == 2).all()
    return cotizaciones_por_enviar

def get_facturas_pagadas():
    facturas_pagadas = session.query(Factura).filter(Factura.Estado == 4).all()
    return facturas_pagadas

def get_facturas_pendientes():
    facturas_pendientes = session.query(Factura).filter(Factura.tipo == 2, Factura.Estado != 4).all()
    return facturas_pendientes

def get_factura_by_id(factura_id):
    factura = session.query(Factura).filter(Factura.id == factura_id).first()
    return factura

def get_facturas_products(factura_id):
    Productos = session.query(DetalleFactura).filter(DetalleFactura.factura_id == factura_id).all()
    return Productos

def delete_factura(factura_number):
    factura = session.query(Factura).filter(Factura.numero_factura == factura_number).first()
    if factura:
        session.delete(factura)
        session.commit()
        return {"Success": True, "Message": f"Factura {factura_number} eliminada correctamente."}
    else:
        return {"Success": False, "Message": f"Factura {factura_number} no encontrada."}

def dashboard_data():
    facturas = get_facturas_pagadas()
    facturas_por_pagar = get_facturas_pendientes()
    cotizaciones = get_cotizaciones_por_enviar()
    recientes = get_recientes_facturas()

    data = {
        "total_facturado": len(facturas),
        "monto_facturado": f"$ {sum(factura.total for factura in facturas):,.2f}",
        "cotizaciones_sin_facturar": len(cotizaciones),
        "monto_cotizaciones_sin_facturar": f"$ {sum(factura.total for factura in cotizaciones):,.2f}",
        "facturas_por_pagar": len(facturas_por_pagar),
        "monto_facturas_por_pagar": f"$ {sum(factura.total for factura in facturas_por_pagar):,.2f}",
        "datos_tabla": recientes
    }

    return {"Success": True, "Data": data}

def get_clientes():
    clientes = session.query(Cliente).all()
    lista_clientes = []
    for cliente in clientes:
        cliente_dict = {
            "id": cliente.id,
            "nombre": cliente.Nombre,
            "NIT": cliente.NIT,
            "REEUP": cliente.REEUP,
            "ONIE": cliente.ONIE,
            "Domicilio": cliente.Domicilio,
            "nro_cta_CUP": cliente.nro_cta_CUP,
            "nro_cta_MLC": cliente.nro_cta_MLC,
            "telefono": cliente.Telefono,
            "correo": cliente.email
        }
        lista_clientes.append(cliente_dict)
    return {"Success": True, "Data": lista_clientes}

def get_cliente_filter(search_term):
    from sqlalchemy import or_
    clientes = session.query(Cliente).filter(
        or_(
            Cliente.Nombre.ilike(f"%{search_term}%"),
            # Cliente.Domicilio.ilike(f"%{search_term}%"),
            Cliente.Telefono.ilike(f"%{search_term}%"),
            Cliente.email.ilike(f"%{search_term}%")
        )
    ).all()
    lista_clientes = []
    for cliente in clientes:
        cliente_dict = {
            "id": cliente.id,
            "nombre": cliente.Nombre,
            "NIT": cliente.NIT,
            "REEUP": cliente.REEUP,
            "ONIE": cliente.ONIE,
            "Domicilio": cliente.Domicilio,
            "nro_cta_CUP": cliente.nro_cta_CUP,
            "nro_cta_MLC": cliente.nro_cta_MLC,
            "telefono": cliente.Telefono,
            "correo": cliente.email
        }
        lista_clientes.append(cliente_dict)
    return {"Success": True, "Data": lista_clientes}

def delete_cliente(cliente_id):
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        return {"Success": True, "Message": f"Cliente {cliente.Nombre} eliminado correctamente."}
    else:
        return {"Success": False, "Message": f"Cliente con ID {cliente_id} no encontrado."}

def update_cliente(cliente_id, updated_data):
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente:
        cliente.Nombre = updated_data.get("nombre", cliente.Nombre)
        cliente.NIT = updated_data.get("NIT", cliente.NIT)
        cliente.REEUP = updated_data.get("REEUP", cliente.REEUP)
        cliente.ONIE = updated_data.get("ONIE", cliente.ONIE)
        cliente.Domicilio = updated_data.get("Domicilio", cliente.Domicilio)
        cliente.nro_cta_CUP = updated_data.get("nro_cta_CUP", cliente.nro_cta_CUP)
        cliente.nro_cta_MLC = updated_data.get("nro_cta_MLC", cliente.nro_cta_MLC)
        cliente.Telefono = updated_data.get("telefono", cliente.Telefono)
        cliente.email = updated_data.get("correo", cliente.email)

        session.commit()
        return {"Success": True, "Message": f"Cliente {cliente.Nombre} actualizado correctamente."}
    else:
        return {"Success": False, "Message": f"Cliente con ID {cliente_id} no encontrado."}

def add_cliente(cliente_data):
    nuevo_cliente = Cliente(
        Nombre=cliente_data["nombre"],
        NIT=cliente_data["NIT"],
        REEUP=cliente_data["REEUP"],
        ONIE=cliente_data["ONIE"],
        Domicilio=cliente_data["Domicilio"],
        nro_cta_CUP=cliente_data["nro_cta_CUP"],
        nro_cta_MLC=cliente_data["nro_cta_MLC"],
        Telefono=cliente_data["telefono"],
        email=cliente_data["correo"]
    )
    session.add(nuevo_cliente)
    session.commit()
    return {"Success": True, "Message": f"Cliente {nuevo_cliente.Nombre} agregado correctamente."}


def get_productos():
    productos = session.query(Producto).all()
    lista_productos = []
    for producto in productos:
        producto_dict = {
            "id": producto.id,
            "nombre": producto.Nombre,
            "precio": producto.Precio,
            "proveedor": producto.Proveedor,
            "peso": float(producto.peso),
        }
        lista_productos.append(producto_dict)
    return {"Success": True, "Data": lista_productos}

def get_productos_filter(search_term):
    productos = session.query(Producto).filter(
        or_(
            Producto.Nombre.ilike(f"%{search_term}%"),
            Producto.Proveedor.ilike(f"%{search_term}%"),
        )
    ).all()
    lista_productos = []
    for producto in productos:
        producto_dict = {
            "id": producto.id,
            "nombre": producto.Nombre,
            "precio": producto.Precio,
            "proveedor": producto.Proveedor,
            "peso": float(producto.peso),
        }
        lista_productos.append(producto_dict)
    return {"Success": True, "Data": lista_productos}

def delete_producto(producto_id):
    producto = session.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        session.delete(producto)
        session.commit()
        return {"Success": True, "Message": f"Producto {producto.Nombre} eliminado correctamente."}
    else:
        return {"Success": False, "Message": f"Producto con ID {producto_id} no encontrado."}
    
def update_producto(producto_id, updated_data):
    producto = session.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        producto.Nombre = updated_data.get("nombre", producto.Nombre)
        producto.Proveedor = updated_data.get("proveedor", producto.Proveedor)
        producto.Precio = updated_data.get("precio", producto.Precio)
        producto.peso = updated_data.get("peso", producto.peso)

        session.commit()
        return {"Success": True, "Message": f"Producto {producto.Nombre} actualizado correctamente."}
    else:
        return {"Success": False, "Message": f"Producto con ID {producto_id} no encontrado."}
    
def add_producto(producto_data):
    nuevo_producto = Producto(
        Nombre=producto_data["nombre"],
        Proveedor=producto_data["proveedor"],
        Precio=producto_data["precio"],
        peso=producto_data["peso"]
    )
    session.add(nuevo_producto)
    session.commit()
    return {"Success": True, "Message": f"Producto {nuevo_producto.Nombre} agregado correctamente."}

def get_configuration():
    tasas = session.query(Tasa).all()
    vendedor = session.query(Vendedor).first()
    config = session.query(Config).first()

    list_tasa = []

    for tasa in tasas:
        list_tasa.append((tasa.Divisa, f"{tasa.tasa:.2f}"))

    dict_data = {
        "nombre_vendedor": vendedor.Nombre,
        "nit_vendedor": vendedor.NIT,
        "telf_vendedor": vendedor.Telefono,
        "direccion_vendedor": vendedor.Domicilio,
        "cuenta_cup_vendedor": vendedor.nro_cta_CUP,
        "tarjeta_cup_vendedor": vendedor.Tarjeta_CUP,
        "cuenta_mlc_vendedor": vendedor.nro_cta_MLC,
        "tarjeta_mlc_vendedor": vendedor.Tarjeta_MLC,
        "email_vendedor": vendedor.email,
        "tasa_mxn": list_tasa[2][1],
        "tasa_cup": list_tasa[0][1],
        "tasa_mlc": list_tasa[1][1],
        "tasa_fiscal": config.porciento_cta_fiscal,
        "nota": config.nota_terminos,
    }

    return {"Success": True, "Data": dict_data}

def convertir_de_mxm_a_usd(monto_mxn: float):
    tasa_mxn = session.query(Tasa).filter(Tasa.Divisa == "MXN").first()
    if tasa_mxn:
        monto_usd = monto_mxn / float(tasa_mxn.tasa)
        return {"Success": True, "Monto USD": f"{monto_usd:.2f}"}
    else:
        return {"Success": False, "Message": "Tasa para MXN no encontrada."}



if __name__ == "__main__":
    cliente = get_cliente_filter("contacto")
    print(cliente)

    # for factura in facturas:
    #     print(factura.numero_factura, factura.vendedor.Nombre, factura.tipo_rel.tipo_factura)

    # Productos = get_facturas_products(1)
    # total = 0
    # for producto in Productos:
    #     total_producto = producto.Precio_venta * producto.Cantidad
    #     print(f"{producto.producto.Nombre} {producto.Precio_venta:.2f} x {producto.Cantidad} = {total_producto:.2f}")
    #     total += total_producto
    # print(f"Total: {total:.2f}")