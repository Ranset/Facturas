from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import NewClientDialog, Menu

class Clientes(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        #  <Carga de datos

        data = {
            "Sucess": True,
            "Data": [
                    {"id": 1, "nombre": "Empresa de suministros integrales y cooperación económica", "telefono": "123456789", "correo": "empresa@importadora.com"},
                    {"id": 2, "nombre": "Pedro", "telefono": "987654321", "correo": "pedro@cliente.com"}
            ]
        }

        # <Fin Carga de datos

        # <Controls
        ## <common variables
        inputs_height = 48
        inputs_bgcolor = ft.Colors.WHITE
        inputs_border_color= ft.Colors.GREY_400
        ## common variables>

        ## <Widgets objects
        txt_Clientes_title = ft.Text(
            "Clientes",
            size= 35,
            weight= ft.FontWeight.BOLD,
            )

        def abrir_dialogo(e):
            page.overlay.append(new_client_dialog) # Agregar el diálogo a la superposición de la página
            new_client_dialog.open = True   # Abrirlo
            page.update()

        btn_add_client = ft.ElevatedButton(
            text="Agregar Cliente",
            bgcolor= '#2c78d0',
            color= 'white',
            on_click= abrir_dialogo,
        )

        txt_buscar_persona = ft.TextField(
            label="Buscar Cliente",
            # expand=True,
            height= inputs_height,
            width= 400,
            bgcolor= inputs_bgcolor,
            border_color= inputs_border_color,
            hover_color= inputs_bgcolor
        )

        btn_buscar = ft.FloatingActionButton(
            bgcolor= "#838383",
            foreground_color= 'white',
            icon= ft.Icons.PERSON_SEARCH,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
        )
        
        btn_clear = ft.FloatingActionButton(
            bgcolor= '#838383',
            foreground_color= 'white',
            icon= ft.Icons.CLEAR,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
        )

        clientes = []

        for c in data["Data"]:
            clientes.append(
                ft.DataRow(
                    [
                        ft.DataCell(ft.Text(c["nombre"])),
                        ft.DataCell(ft.Text(c["telefono"])),
                        ft.DataCell(ft.Text(c["correo"])),
                        ft.DataCell(ft.TextButton("Eliminar", on_click= lambda e: print("Eliminar cliente"), style= ft.ButtonStyle(color= "red"))),
                    ],
                    # on_select_changed= on_select_row,
                    data= c
                )
            )

        dt_clientes = ft.DataTable(
            columns= [
                ft.DataColumn(ft.Text("Nombre Comercial", weight= ft.FontWeight.BOLD), heading_row_alignment= ft.MainAxisAlignment.CENTER),
                ft.DataColumn(ft.Text("Teléfono", weight= ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Correo", weight= ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Acción", weight= ft.FontWeight.BOLD)),
            ],
            rows= clientes,
            heading_row_height= 40,
            data_row_max_height= 45,
        )

        new_client_dialog = NewClientDialog(page).Crear()

        ## Widgets objects>
        # Controls>

        # <Layout
        column_left = ft.Column(
            controls= [
                txt_Clientes_title,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.START,
            expand= True,
        )
        
        column_Right = ft.Column(
            controls= [
                btn_add_client,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.END,
            expand= True,
        )

        Row1 = ft.Row(controls=[column_left, column_Right], alignment= ft.MainAxisAlignment.CENTER)
        contenedor1 = ft.Container(
            content=Row1, 
            # bgcolor= "#7979e6",
            margin= ft.margin.only(top=30, left=15, right=15),
        )

        Row2 = ft.Row(
            controls=[
                ft.Column(expand= True),  # Espaciador a la izquierda
                txt_buscar_persona,
                btn_buscar,
                btn_clear
                ],
                vertical_alignment= ft.CrossAxisAlignment.END,
                spacing= 10
            )
        contenedor2 = ft.Container(
            content=Row2, 
            margin= ft.margin.only(left=15, right=15),
            )
        
        contenedor_tabled_clientes = ft.Container(
            content= dt_clientes,
            bgcolor= ft.Colors.WHITE,
            border= ft.border.all(1, "#CBD5E1"),
            border_radius= ft.border_radius.all(5),
            margin= ft.margin.only(left= 15, right=15, top=10),
            expand= True,
        )

        Row3 = ft.Row(
            controls=[
                contenedor_tabled_clientes
            ],
            alignment= ft.MainAxisAlignment.CENTER,
        )

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[contenedor1, contenedor2, Row3], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>