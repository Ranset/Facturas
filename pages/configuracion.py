from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import Menu
from controller import get_configuration

class Configuracion(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        #  <Carga de datos
        data = get_configuration()
        # <Fin Carga de datos

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
            from router import show_view
            show_view(page, "vendedor")

        btn_editar_vendedor = ft.ElevatedButton(
            text="Editar",
            bgcolor= '#2c78d0',
            color= 'white',
            height= 40,
            width= 120,
            on_click= _btn_editar_vendedor_clicked,
        )

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
                        ft.Text("MXN", size= 22, color="white", weight="bold", text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.Text(data["Data"]["tasa_mxn"], size=30, color= "white")
                ],
                horizontal_alignment= "center"
            ),
            bgcolor= "#067429",
            padding= ft.padding.all(18),
            width= 130,
            border_radius= 20
        )
        
        ### tasa cup
        tasa_cup = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FLAG, color= "white"),
                        ft.Row(expand= True),
                        ft.Text("CUP", size= 22, color="white", weight="bold", text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.Text(data["Data"]["tasa_cup"], size=30, color= "white")
                ],
                horizontal_alignment= "center"
            ),
            bgcolor= "red",
            padding= ft.padding.all(18),
            width= 130,
            border_radius= 20
        )
        
        ### tasa mlc
        tasa_mlc = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FLAG, color= "white"),
                        ft.Row(expand= True),
                        ft.Text("MLC", size= 22, color="white", weight="bold", text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.Text(data["Data"]["tasa_mlc"], size=30, color= "white")
                ],
                horizontal_alignment= "center"
            ),
            bgcolor= "#305BAB",
            padding= ft.padding.all(18),
            width= 130,
            border_radius= 20
        )

        def edit_tasa_click (e):
            tasas.content.controls[0].visible= False
            tasas.content.controls[1].visible= True
            tasas.update()

        btn_editar_tasa = ft.FloatingActionButton(
            bgcolor= "#2c78d0",
            foreground_color= 'white',
            icon= ft.Icons.EDIT,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= 35,
            height= 118,
            on_click= edit_tasa_click
        )

        ### tasa mxn edit
        tasa_mxn_edit = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FLAG, color= "white"),
                        ft.Row(expand= True),
                        ft.Text("MXN", size= 22, color="white", weight="bold", text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.TextField(value= data["Data"]["tasa_mxn"], bgcolor= inputs_bgcolor, max_length= 6)
                ],
                horizontal_alignment= "center"
            ),
            bgcolor= "#067429",
            padding= ft.padding.all(18),
            width= 130,
            border_radius= 20
        )
        
        ### tasa cup edit
        tasa_cup_edit = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FLAG, color= "white"),
                        ft.Row(expand= True),
                        ft.Text("CUP", size= 22, color="white", weight="bold", text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.TextField(value= data["Data"]["tasa_cup"], bgcolor= inputs_bgcolor, max_length= 6)
                ],
                horizontal_alignment= "center"
            ),
            bgcolor= "red",
            padding= ft.padding.all(18),
            width= 130,
            border_radius= 20
        )
        
        ### tasa mlc edit
        tasa_mlc_edit = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FLAG, color= "white"),
                        ft.Row(expand= True),
                        ft.Text("MLC", size= 22, color="white", weight="bold", text_align= ft.TextAlign.END)
                    ], expand= True),
                    ft.TextField(value= data["Data"]["tasa_mlc"], bgcolor= inputs_bgcolor, max_length= 6)
                ],
                horizontal_alignment= "center"
            ),
            bgcolor= "#305BAB",
            padding= ft.padding.all(18),
            width= 130,
            border_radius= 20
        )

        def check_tasa_click (e):
            tasas.content.controls[1].visible= False
            tasas.content.controls[0].visible= True
            tasas.update()

        btn_check_tasa = ft.FloatingActionButton(
            bgcolor= "#2c78d0",
            foreground_color= 'white',
            icon= ft.Icons.CHECK,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= 35,
            height= 120,
            on_click= check_tasa_click
        )

        tasas = ft.Container(
            ft.Column(
                controls= [
                    ft.Row(
                        controls= [
                            tasa_mxn,
                            tasa_cup,
                            tasa_mlc,
                            btn_editar_tasa
                        ],
                        spacing= 35
                    ),
                    ft.Row(
                        controls= [
                            tasa_mxn_edit,
                            tasa_cup_edit,
                            tasa_mlc_edit,
                            btn_check_tasa
                        ],
                        spacing= 35,
                        visible= False
                    )
                ]
            ),
            margin= ft.margin.only(left= 20, right= 20)
        )

        def tasa_fiscal_change(e):
            btn_tasa_fiscal.visible = True
            page.update()

        tasa_fiscal_tile = ft.Text("Tasas Fiscal", size= 25)
        tasa_fiscal_icon = ft.Icon(ft.Icons.ACCOUNT_BALANCE, "black", 40)
        tasa_fiscal = ft.TextField(
                    data["Data"]["tasa_fiscal"],
                    suffix= ft.Text("%"),
                    border_color= inputs_border_color,
                    max_length= 2,
                    bgcolor= inputs_bgcolor,
                    width= 70,
                    on_change= lambda e: tasa_fiscal_change(e)
                )
        
        def click_btn_tasa_fiscal(e):
            import asyncio

            btn_tasa_fiscal.visible = False
            txt_salvado.visible = True
            page.update()
            
            async def hide_message():
                await asyncio.sleep(2)
                txt_salvado.visible = False
                page.update()
            
            asyncio.run(hide_message())

        btn_tasa_fiscal = ft.FloatingActionButton(
            bgcolor= "#838383",
            foreground_color= 'white',
            icon= ft.Icons.CHECK,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
            visible= False,
            on_click= click_btn_tasa_fiscal
        )
        txt_salvado = ft.Text("Salvado!!", color= "green", visible= False)

        def click_btn_nota(e):
            import asyncio

            btn_nota.visible = False
            txt_salvado_nota.visible = True
            page.update()
            
            async def hide_message():
                await asyncio.sleep(2)
                txt_salvado_nota.visible = False
                page.update()
            
            asyncio.run(hide_message())

        btn_nota = ft.FloatingActionButton(
            bgcolor= "#838383",
            foreground_color= 'white',
            icon= ft.Icons.CHECK,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
            visible= False,
            on_click= click_btn_nota
        )

        txt_salvado_nota = ft.Text("Salvado!!", color= "green", visible= False)

        def tasa_nota_change(e):
            btn_nota.visible = True
            page.update()

        nota = ft.TextField(
            data["Data"]["nota"],
            border_color= inputs_border_color,
            max_length= 150,
            bgcolor= inputs_bgcolor,
            expand= True,
            label= "Nota de términos",
            on_change= lambda e: tasa_nota_change(e)
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

        Row2 = ft.Row(controls=[
            ft.Column([ft.Container(txt_tasas_title, padding= ft.padding.only(left=20)),tasas]),
            ft.Container(ft.Column(
                [
                    tasa_fiscal_tile,
                    ft.Row([tasa_fiscal_icon, tasa_fiscal, btn_tasa_fiscal, txt_salvado]),
                    ft.Container(ft.Row([nota, btn_nota, txt_salvado_nota]), margin= ft.margin.only(top= 20)),
                    
                ],
                spacing= 5
                    ),
                    expand= True,
                    margin= ft.margin.only(right= 20)
                    )
        ],
        vertical_alignment= ft.CrossAxisAlignment.START,
        spacing= 70,
        )

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[
            contenedor1, 
            Row2
            ], expand= True, spacing= 20)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>