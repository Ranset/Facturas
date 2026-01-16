from flet_base import flet_instance as ft
from pages.cotizacion import Cotizacion

def show_view(page: ft.Page, route: str):

    if route == "cotizacion":
        page.controls.clear()
        page.add(Cotizacion(page))