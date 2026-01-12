import flet as ft
from pages.common_controls.states import States

location = States.where_i_am

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
    bgcolor= bgcolor_btn_menu if States.where_i_am != States._inicio_location else bgcolor_btn_menu_active,
)

btn_cotizaciones_menu = ft.FilledButton(
    text="Cotizaciones",
    icon=ft.Icons.DESCRIPTION,
    width=with_btn_menu,
    style= styles_btn_menu,
    bgcolor= bgcolor_btn_menu_active if States.where_i_am == States._cotizacion_location else bgcolor_btn_menu,
)

btn_facturas_menu = ft.FilledButton(
    text="Facturas",
    icon=ft.Icons.REQUEST_QUOTE,
    width=with_btn_menu,
    style= styles_btn_menu,
    bgcolor= bgcolor_btn_menu if States.where_i_am != States._factura_location else bgcolor_btn_menu_active,
)

btn_clientes_menu = ft.FilledButton(
    text="Clientes",
    icon=ft.Icons.PERSON,
    width=with_btn_menu,
    style= styles_btn_menu,
    bgcolor= bgcolor_btn_menu if States.where_i_am != States._cliente_location else bgcolor_btn_menu_active,
)

btn_productos_menu = ft.FilledButton(
    text="Productos",
    icon=ft.Icons.INVENTORY_2,
    width=with_btn_menu,
    style= styles_btn_menu,
    bgcolor= bgcolor_btn_menu if States.where_i_am != States._producto_location else bgcolor_btn_menu_active,
)

btn_configuracion_menu = ft.FilledButton(
    text="Configuración",
    icon=ft.Icons.SETTINGS,
    width=with_btn_menu,
    style= styles_btn_menu,
    bgcolor= bgcolor_btn_menu if States.where_i_am != States._configuracion_location else bgcolor_btn_menu_active,
)

btn_acerca_menu = ft.FilledButton(
    text="Acerca de",
    icon=ft.Icons.INFO,
    width=with_btn_menu,
    style= styles_btn_menu,
    bgcolor= bgcolor_btn_menu if States.where_i_am != States._acerca_location else bgcolor_btn_menu_active,
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
contenedor_menu = ft.Container(
    content=menu,
    bgcolor= '#222a31', 
    expand= True,
    width= 190,
    padding= ft.padding.only(top= 30)
    )