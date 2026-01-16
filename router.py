from flet_base import flet_instance as ft
from pages.factura import Cotizacion
from pages.formulario_factura import FormularioFactura

def show_view(page: ft.Page, route: str):

    if route == "cotizacion":
        page.controls.clear()
        page.add(Cotizacion(page))
    if route == "formulario_factura":
        page.controls.clear()
        page.add(FormularioFactura(page))

    