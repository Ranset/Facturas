from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import Menu
from controller import get_configuration, update_vendedor

class Vendedor(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        #  <Carga de datos

        data = get_configuration()

        datos_vendedor = (
            data["Data"]["nombre_vendedor"],
            data["Data"]["nit_vendedor"],
            data["Data"]["telf_vendedor"],
            data["Data"]["direccion_vendedor"],
            data["Data"]["cuenta_cup_vendedor"],
            data["Data"]["tarjeta_cup_vendedor"],
            data["Data"]["cuenta_mlc_vendedor"],
            data["Data"]["tarjeta_mlc_vendedor"],
            data["Data"]["email_vendedor"]
        )

        # <Fin Carga de datos

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
                            value= datos_vendedor[0],
                            label="Nombre Comercial",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            )
        
        txt_nit = ft.TextField(
                            value= datos_vendedor[1],
                            label="NIT",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            expand= True,
                            )
        
        txt_telefono = ft.TextField(
                            value= datos_vendedor[2],
                            label="Teléfono",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            expand= True,
                            )
        
        txt_email = ft.TextField(
                            value= datos_vendedor[8],
                            label="Email",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            expand= True
                            )
        
        txt_domicilio = ft.TextField(
                            value= datos_vendedor[3],
                            label="Domicilio",
                            height= 96,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            multiline= True,
                            )
        
        txt_cta_cup = ft.TextField(
                            value= datos_vendedor[4],
                            label="# de Cuenta CUP",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            expand= True,
                            )
        
        txt_cta_mlc = ft.TextField(
                            value= datos_vendedor[5],
                            label="# de Cuenta MLC",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            expand= True,
                            )
        
        txt_tarjeta_cup = ft.TextField(
                            value= datos_vendedor[6],
                            label="# de Tarjeta CUP",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            expand= True,
                            )
        
        txt_tarjeta_mlc = ft.TextField(
                            value= datos_vendedor[7],
                            label="# de Tarjeta MLC",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
                            expand= True,
                            )
        
        def click_guardar(e):
            from router import show_view
            update_vendedor(
                {
                    "nombre_vendedor": txt_nombre.value,
                    "nit_vendedor": txt_nit.value,
                    "telf_vendedor": txt_telefono.value,
                    "email_vendedor": txt_email.value,
                    "direccion_vendedor": txt_domicilio.value,
                    "cuenta_cup_vendedor": txt_cta_cup.value,
                    "tarjeta_cup_vendedor": txt_tarjeta_cup.value,
                    "cuenta_mlc_vendedor": txt_cta_mlc.value,
                    "tarjeta_mlc_vendedor": txt_tarjeta_mlc.value
                }
            )

            show_view(page, States._configuracion_location)
        
        btn_guardar = ft.ElevatedButton(
            "Guardar",
            style= ft.ButtonStyle(bgcolor= "#2c78d0", color= "white", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            height= inputs_height,
            expand= True,
            on_click= click_guardar
        )

        def click_cancelar(e):
            from router import show_view
            show_view(page, States._configuracion_location)
        
        btn_cancelar = ft.OutlinedButton(
            "Canelar",
            style= ft.ButtonStyle(side= ft.BorderSide(1, "#2c78d0"), color= "#2c78d0", shape= ft.RoundedRectangleBorder(radius= 5)),
            width= 120,
            height= inputs_height,
            on_click= click_cancelar,
            expand= True
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
                ], expand= True),
                txt_domicilio,
                ft.Row([
                    txt_cta_cup,
                    txt_cta_mlc,
                    btn_guardar
                ]),
                ft.Row([
                    txt_tarjeta_cup,
                    txt_tarjeta_mlc,
                    btn_cancelar
                ]),
            ]
        )

        contenedor_formulario = ft.Container(
            content= column_formulario,
            width= 600,
        )

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[contenedor1, contenedor_formulario], expand= True, horizontal_alignment= "center")

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>