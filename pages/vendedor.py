from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import Menu

class Vendedor(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # <Controls
        ## <common variables
        inputs_height = 48
        inputs_bgcolor = ft.Colors.WHITE
        inputs_border_color= ft.Colors.GREY_400
        ## common variables>

        ## <Widgets objects
        txt_Productos_title = ft.Text(
            "Vendedor",
            size= 35,
            weight= ft.FontWeight.BOLD,
            )

        txt_nombre = ft.TextField(
                            label="Nombre Comercial",
                            
                            # expand= True,
                            )
        
        txt_nit = ft.TextField(
                            label="NIT",
                            
                            # expand= True,
                            )
        
        txt_telefono = ft.TextField(
                            label="Teléfono",
                            
                            # expand= True,
                            )
        
        txt_email = ft.TextField(
                            label="Email",
                            
                            )
        
        txt_domicilio = ft.TextField(
                            label="Domcilio",
                            
                            # expand= True,
                            )
        
        txt_cta_cup = ft.TextField(
                            label="# de Cuenta CUP",
                            
                            # expand= True,
                            )
        
        txt_cta_mlc = ft.TextField(
                            label="# de Cuenta MLC",
                            
                            # expand= True,
                            )
        
        txt_tarjeta_cup = ft.TextField(
                            label="# de Cuenta CUP",
                            
                            # expand= True,
                            )
        
        txt_tarjeta_mlc = ft.TextField(
                            label="# de Cuenta MLC",
                            
                            # expand= True,
                            )
        
        btn_guardar = ft.ElevatedButton(
            "Guardar",
            style= ft.ButtonStyle(bgcolor= "#2c78d0", color= "white", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
        )

        def click_cancelar(e):
            pass
        
        btn_cancelar = ft.OutlinedButton(
            "Canelar",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            on_click= click_cancelar
        )

        ## Widgets objects>
        # Controls>

        # <Layout
        column_left = ft.Column(
            controls= [
                txt_Productos_title,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.START,
            expand= True,
        )
        
        Row1 = ft.Row(controls=[column_left], alignment= ft.MainAxisAlignment.CENTER)
        contenedor1 = ft.Container(
            content=Row1, 
            margin= ft.margin.only(top=30, left=15, right=15),
        )

        column_formulario = ft.Column(
            controls=[
                txt_nombre,
                ft.Row([
                    txt_nit,
                    txt_telefono,
                    txt_email
                ]),
                txt_domicilio,
                ft.Row([
                    txt_cta_cup,
                    txt_cta_mlc
                ]),
                ft.Row([
                    txt_tarjeta_cup,
                    txt_tarjeta_mlc
                ]),
            ]
        )

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[contenedor1], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>