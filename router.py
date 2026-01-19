from flet_base import flet_instance as ft
from pages.factura import Factura
from pages.formulario_factura import FormularioFactura

def show_view(page: ft.Page, route: str):

    if route == "inicio":
        page.controls.clear()
        page.add(FormularioFactura(page))
    if route == "cotizacion" or route == "factura":
        page.controls.clear()
        page.add(Factura(page))
