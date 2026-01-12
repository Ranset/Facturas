from models import (session, 
                    Tasa,
                    Tipo,
                    Factura,
                    DetalleFactura)

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

if __name__ == "__main__":
    # facturas = get_facturas()
    # print("Cantidad de facturas:", len(facturas))
    # for factura in facturas:
    #     print(factura.numero_factura, factura.vendedor.Nombre, factura.tipo_rel.tipo_factura)

    Productos = get_facturas_products(1)
    total = 0
    for producto in Productos:
        total_producto = producto.Precio_venta * producto.Cantidad
        print(f"{producto.producto.Nombre} {producto.Precio_venta:.2f} x {producto.Cantidad} = {total_producto:.2f}")
        total += total_producto
    print(f"Total: {total:.2f}")