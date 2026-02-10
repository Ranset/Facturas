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
        
        datos_vendedor = (
            "Yadira Hernández Herrera",
            "88042108175",
            "+5354132764",
            "Calle Serafina #12 e/ Ulacia y Castillo, Reparto Juanelo, San Miguel del Padrón. La Habana, Cuba. C.P. 11000.",
            "0598770015216512",
            "9212959871557908",
            "0598770015216512",
            "9212959871557908",
            "yadirahernandez0421@gmail.com"
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
                            label="Domcilio",
                            height= inputs_height,
                            bgcolor= inputs_bgcolor,
                            border_color= inputs_border_color,
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