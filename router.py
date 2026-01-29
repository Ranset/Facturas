from flet_base import flet_instance as ft
from pages.factura import Factura
from pages.formulario_factura import FormularioFactura
from pages.clientes import Clientes

def show_view(page: ft.Page, route: str):

    if route == "inicio":
        page.controls.clear()
        page.add(FormularioFactura(page))
    if route == "cotizacion" or route == "factura":
        page.controls.clear()
        page.add(Factura(page))
    if route == "formulario_factura":
        page.controls.clear()
        page.add(FormularioFactura(page))
    if route == "cliente":
        page.controls.clear()
        page.add(Clientes(page))
