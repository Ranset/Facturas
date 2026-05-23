from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import Menu

class Acerca(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # <Controls
        ## <common variables

        ## common variables>

        ## <Widgets objects
        txt_title = ft.Text(
            "FACTURACIÓN CM",
            size= 35,
            weight= ft.FontWeight.BOLD,
            )
        
        txt_version = ft.Text(
            "Versión 1.2.2",
            size= 20,
            )
        
        txt_job = ft.Text(
            "Desarrollado por: Ranset Fleites",
            size= 16,
            )

        img_logo = ft.Image("images/facturacion_cm_logo.png", width= 400, height= 400)

        ## Widgets objects>
        # Controls>

        # <Layout
    
        column_central = ft.Column(
            controls=[
                img_logo,
                # txt_title,
                txt_version,
                # txt_job
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        )

        contenedor_central = ft.Container(
            content= column_central,
            width= 600,
            # padding= ft.padding.only(top= 30)
        )

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[contenedor_central], expand= True, horizontal_alignment= "center")

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>