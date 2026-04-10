from models import (session, 
                    Tasa,
                    Tipo,
                    Factura,
                    DetalleFactura,
                    Cliente,
                    Producto)

def get_facturas():
    facturas = session.query(Factura).filter(Factura.tipo == 2).all()
    return facturas

def get_cotizaciones():
    cotizaciones = session.query(Factura).filter(Factura.tipo == 1).all()
    return cotizaciones

def get_factura_by_id(factura_id):
    factura = session.query(Factura).filter(Factura.id == factura_id).first()
    return factura

def get_facturas_products(factura_id):
    Productos = session.query(DetalleFactura).filter(DetalleFactura.factura_id == factura_id).all()
    return Productos

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

def get_productos():
    productos = session.query(Producto).all()
    lista_productos = []
    for producto in productos:
        producto_dict = {
            "id": producto.id,
            "nombre": producto.Nombre,
            "proveedor": producto.Proveedor,
            "precio": producto.Precio,
            "peso": float(producto.peso)
        }
        lista_productos.append(producto_dict)
    return {"Success": True, "Data": lista_productos}


if __name__ == "__main__":
    # facturas = get_facturas()
    # print("Cantidad de facturas:", len(facturas))
    # for factura in facturas:
    #     print(factura.numero_factura, factura.vendedor.Nombre, factura.tipo_rel.tipo_factura)

    # Productos = get_facturas_products(1)
    # total = 0
    # for producto in Productos:
    #     total_producto = producto.Precio_venta * producto.Cantidad
    #     print(f"{producto.producto.Nombre} {producto.Precio_venta:.2f} x {producto.Cantidad} = {total_producto:.2f}")
    #     total += total_producto
    # print(f"Total: {total:.2f}")

    clientes = get_clientes()
    print(clientes)