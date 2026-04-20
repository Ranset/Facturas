from flet_base import flet_instance as ft
from pages.common_controls.states import States
from pages.common_controls.customs_widgets import NewProductDialog, Menu
from controller import get_productos, delete_producto, get_productos_filter

class Productos(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        #  <Carga de datos

        data = get_productos()

        # <Fin Carga de datos

        # <Controls
        ## <common variables
        inputs_height = 48
        inputs_bgcolor = ft.Colors.WHITE
        inputs_border_color= ft.Colors.GREY_400
        ## common variables>

        ## <Widgets objects
        txt_Productos_title = ft.Text(
            "Productos",
            size= 35,
            weight= ft.FontWeight.BOLD,
            )

        def abrir_dialogo(e):
            page.overlay.append(new_product_dialog) # Agregar el diálogo a la superposición de la página
            new_product_dialog.open = True   # Abrirlo
            page.update()

        btn_add_producto = ft.ElevatedButton(
            text="Agregar Producto",
            bgcolor= '#2c78d0',
            color= 'white',
            on_click= abrir_dialogo,
        )

        def click_btn_buscar(e):
            search_term = txt_buscar_producto.value
            if search_term:
                resultado = get_productos_filter(search_term)
                # Cargar resultados en la tabla
                productos.clear()
                for p in resultado["Data"]:
                    productos.append(
                        ft.DataRow(
                            [
                                ft.DataCell(ft.Text(p["nombre"])),
                                ft.DataCell(ft.Text(f"${float(p['precio']):.2f}")),
                                ft.DataCell(ft.Text(p["proveedor"])),
                                ft.DataCell(ft.Text(p["peso"])),
                                ft.DataCell(ft.Row(controls=[
                                ft.IconButton(icon=ft.Icons.EDIT_SHARP, icon_color=ft.Colors.PRIMARY, on_click= click_btn_editar, style= ft.ButtonStyle(color= "red"), data= (p["id"], p["nombre"], p["proveedor"], p["precio"], p["peso"])),
                                ft.IconButton(icon=ft.Icons.DELETE_FOREVER, icon_color=ft.Colors.RED, on_click= click_btn_eliminar, style= ft.ButtonStyle(color= "red"), data= p["id"]),
                            ],
                            spacing= 0
                            )
                        ),
                            ],
                            data= p
                        )
                    )
                
                dt_productos.rows = productos
                page.update()
            else:
                print("Término de búsqueda en blanco.")

        txt_buscar_producto = ft.TextField(
            label="Buscar Producto",
            # expand=True,
            height= inputs_height,
            width= 400,
            bgcolor= inputs_bgcolor,
            border_color= inputs_border_color,
            hover_color= inputs_bgcolor,
            on_submit= click_btn_buscar
        )

        btn_buscar = ft.FloatingActionButton(
            bgcolor= "#838383",
            foreground_color= 'white',
            icon= ft.Icons.SEARCH,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
            on_click= click_btn_buscar
        )

        def click_btn_limpiar(e):
            txt_buscar_producto.value = ""
            recargar_tabla_productos()
        
        btn_clear = ft.FloatingActionButton(
            bgcolor= '#838383',
            foreground_color= 'white',
            icon= ft.Icons.CLEAR,
            shape= ft.RoundedRectangleBorder(radius= 5),
            width= inputs_height,
            height= inputs_height,
            on_click= click_btn_limpiar
        )

        def eliminar_producto(e, modal_dialog: ft.AlertDialog):
            response = delete_producto(e.control.data)
            if response["Success"]:
                print("Producto eliminado exitosamente")
                modal_dialog.open = False  # Cerrar el diálogo
                recargar_tabla_productos()  # Recargar la tabla

        def click_btn_eliminar(id):
            def cerrar_modal(e):
                modal_dialog.open = False  # Cerrar el diálogo
                page.update()

            modal_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Confirmación", weight= "bold"),
                content=ft.Text("¿Desea eliminar los datos de este producto?"),
                actions=[
                    ft.TextButton("Si", on_click=lambda e: eliminar_producto(id, modal_dialog)),
                    ft.TextButton("No", on_click=cerrar_modal),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )

            page.overlay.append(modal_dialog) # Agregar el diálogo a la superposición de la página
            modal_dialog.open = True   # Abrirlo
            page.update()

        def click_btn_editar(e):
            new_product_dialog = NewProductDialog(page, *e.control.data).Crear()
            page.overlay.append(new_product_dialog) # Agregar el diálogo a la superposición de la página
            new_product_dialog.open = True   # Abrirlo
            page.update()

        productos = []

        def recargar_tabla_productos():
                productos.clear() 
                data = get_productos()  # Obtener los datos actualizados de los productos

                for p in data["Data"]:
                    productos.append(
                        ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(p["nombre"])),
                        ft.DataCell(ft.Text(f"${float(p['precio']):.2f}")),
                        ft.DataCell(ft.Text(p["proveedor"])),
                        ft.DataCell(ft.Text(p["peso"])),
                        ft.DataCell(ft.Row(controls=[
                                ft.IconButton(icon=ft.Icons.EDIT_SHARP, icon_color=ft.Colors.PRIMARY, on_click= click_btn_editar, style= ft.ButtonStyle(color= "red"), data= (p["id"], p["nombre"], p["proveedor"], p["precio"], p["peso"])),
                                ft.IconButton(icon=ft.Icons.DELETE_FOREVER, icon_color=ft.Colors.RED, on_click= click_btn_eliminar, style= ft.ButtonStyle(color= "red"), data= p["id"]),
                                ],
                                spacing= 0
                            )
                        ),
                    ],
                    data= p,
                )
                    )

                    dt_productos.rows = productos  # Actualizar las filas de la tabla con la nueva lista de productos
                    page.update()  

        for p in data["Data"]:
            productos.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(p["nombre"])),
                        ft.DataCell(ft.Text(f"${float(p['precio']):.2f}")),
                        ft.DataCell(ft.Text(p["proveedor"])),
                        ft.DataCell(ft.Text(p["peso"])),
                        ft.DataCell(ft.Row(controls=[
                                ft.IconButton(icon=ft.Icons.EDIT_SHARP, icon_color=ft.Colors.PRIMARY, on_click= click_btn_editar, style= ft.ButtonStyle(color= "red"), data= (p["id"], p["nombre"], p["proveedor"], p["precio"], p["peso"])),
                                ft.IconButton(icon=ft.Icons.DELETE_FOREVER, icon_color=ft.Colors.RED, on_click= click_btn_eliminar, style= ft.ButtonStyle(color= "red"), data= p["id"]),
                                ],
                                spacing= 0
                            )
                        ),
                    ],
                    data= p,
                )
            )

        dt_productos = ft.DataTable(
            columns= [
                ft.DataColumn(ft.Text("Producto", weight= ft.FontWeight.BOLD), heading_row_alignment= ft.MainAxisAlignment.CENTER),
                ft.DataColumn(ft.Text("Precio USD", weight= ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Proveedor", weight= ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Peso Kg", weight= ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Acción", weight= ft.FontWeight.BOLD)),
            ],
            rows= productos,
            heading_row_height= 40,
            data_row_max_height= 45,
        )

        new_product_dialog = NewProductDialog(page).Crear()

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
        
        column_Right = ft.Column(
            controls= [
                btn_add_producto,
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
                txt_buscar_producto,
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
        
        contenedor_tabled_productos = ft.Container(
            content= dt_productos,
            bgcolor= ft.Colors.WHITE,
            border= ft.border.all(1, "#CBD5E1"),
            border_radius= ft.border_radius.all(5),
            margin= ft.margin.only(left= 15, right=15, top=10),
            expand= True,
        )
        
        Row3 = ft.Row(
            controls=[
                contenedor_tabled_productos
            ],
            alignment= ft.MainAxisAlignment.CENTER,
        )

        lv_productos = ft.ListView(
            controls= [Row3],
            expand= True,
            height= 500
            )

        columna_menu = ft.Column(controls= [Menu().Crear()])
        column2 = ft.Column(controls=[contenedor1, contenedor2, lv_productos], expand= True)

        Row_generar = ft.Row(controls=[columna_menu, column2], alignment= ft.MainAxisAlignment.CENTER, spacing= 0, expand= True)

        page.add(Row_generar)

        # Layout>