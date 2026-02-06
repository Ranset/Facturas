from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import Menu

class Configuracion(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # <Controls
        ## <common variables
        inputs_height = 48
        inputs_bgcolor = ft.Colors.WHITE
        inputs_border_color= ft.Colors.GREY_400
        text_size = 22
        spacig = 35
        ## common variables>

        ## <Widgets objects
        txt_Vendedor_title = ft.Text(
            "Vendedor",
            size= 35,
            weight= ft.FontWeight.BOLD,
            )
        
        def _btn_editar_vendedor_clicked(e):
            pass

        btn_editar_vendedor = ft.ElevatedButton(
            text="Editar",
            bgcolor= '#2c78d0',
            color= 'white',
            height= 40,
            width= 120,
            on_click= _btn_editar_vendedor_clicked,
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
        
        txt_nombre = ft.Text(datos_vendedor[0], size= text_size)
        txt_nit = ft.Text(f"NIT: {datos_vendedor[1]}", size= text_size)
        txt_telf = ft.Text(f"Telf: {datos_vendedor[2]}", size= text_size)
        txt_direccion = ft.Text(datos_vendedor[3], expand= True, overflow= "clip", size= text_size)
        txt_cuenta_cup = ft.Text(f"Cuenta CUP: {datos_vendedor[4]}", size= text_size)
        txt_tarjeta_cup = ft.Text(f"Tarjeta CUP: {datos_vendedor[5]}", size= text_size)
        txt_cuenta_mlc = ft.Text(f"Cuenta MLC {datos_vendedor[6]}", size= text_size)
        txt_tarjeta_mlc = ft.Text(f"Tarjeta MLC: {datos_vendedor[7]}", size= text_size)
        txt_email = ft.Text(f"Email: {datos_vendedor[8]}", size= text_size)

        txt_tasas_title = ft.Text("Tasas de cambios", size= 25)

        ### tasa mxn
        tasa_mxn = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FLAG, color= "white"),
                        ft.Row(expand= True),
                        ft.Text("MXN", color="white", weight="bold", text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.Text("999.99", size=30, color= "white")
                ],
                horizontal_alignment= "center"
            ),
            bgcolor= "#067429",
            padding= ft.padding.all(18),
            width= 130
        )

        tasas = ft.Container(
            ft.Column(
                controls= [
                    ft.Row(
                        controls= [
                            tasa_mxn,
                        ]
                    )
                ]
            )
        )

        ## Widgets objects>
        # Controls>

        # <Layout
        column_left = ft.Column(
            controls= [
                txt_Vendedor_title,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.START,
            expand= True,
        )
        
        column_Right = ft.Column(
            controls= [
                btn_editar_vendedor,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.END,
            expand= True,
        )

        Row1 = ft.Row(controls=[column_left, column_Right], alignment= ft.MainAxisAlignment.CENTER)
        column_vendedor = ft.Column(controls=[
            Row1,
            ft.Row(controls=[txt_nombre,txt_nit,txt_telf], spacing= spacig),
            ft.Row(controls=[txt_direccion], spacing= spacig),
            ft.Row(controls=[txt_cuenta_cup, txt_tarjeta_cup], spacing= spacig),
            ft.Row(controls=[txt_cuenta_mlc, txt_tarjeta_mlc], spacing= spacig),
            ft.Row(controls=[txt_email], spacing= spacig),
            ],
        spacing= 2
        )

        contenedor1 = ft.Container(
            content=column_vendedor, 
            margin= ft.margin.only(top=30, left=20, right=20),
            padding= ft.padding.all(15),
            border= ft.border.all(2, "grey"),
            border_radius= ft.border_radius.all(15)
        )

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[
            contenedor1, 
            ft.Container(txt_tasas_title, padding= ft.padding.only(left=20)),
            tasas
            ], expand= True, spacing= 20)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>