import flet as ft

class CustomTextDatePicker(ft.TextField):
    def __init__(self, page: ft.Page, label: str = "Fecha"):
        super().__init__()

        self.select_fecha_inicio = ft.TextField(label= label, 
                                                # expand= True, 
                                                suffix_icon= ft.Icons.CALENDAR_TODAY, 
                                                width= 145,
                                                bgcolor= ft.Colors.WHITE,
                                                border_color= ft.Colors.GREY_400,
                                                on_click= lambda e: page.open(ft.DatePicker(on_change= self.poner_fecha))
                                                )

    def Crear(self):
        return self.select_fecha_inicio

    def poner_fecha(self, e):
        self.select_fecha_inicio.value = e.control.value.strftime("%d/%m/%Y")
        try:
            self.select_fecha_inicio.update()
        except Exception:
            pass


class CustomTextFieldAutocomplete(ft.Stack):
    def __init__(self, page: ft.Page, label: str, suggestions: list):
        super().__init__()

        def on_suggestion_click(value):
            select_cliente_field.value = value
            try:
                select_cliente_field.update()
            except Exception:
                pass
            suggestions_container.visible = False
            # move wrapper back from overlay to the stack if needed
            try:
                if overlay_wrapper in page.overlay:
                    try:
                        page.overlay.remove(overlay_wrapper)
                    except Exception:
                        pass
                if overlay_wrapper not in self.select_cliente.controls:
                    self.select_cliente.controls.append(overlay_wrapper)
            except Exception:
                pass
            page.update()

        def on_cliente_change(e):
            txt = e.control.value or ""
            if not txt:
                suggestions_container.content = ft.Column(controls=[])
                suggestions_container.visible = False
                page.update()
                return
            matches = [c for c in suggestions if txt.lower() in c.lower()]
            controls = []
            for m in matches:
                controls.append(
                    ft.Container(
                        content=ft.GestureDetector(
                            on_tap=lambda ev, v=m: on_suggestion_click(v),
                            content=ft.Container(content=ft.Text(m)),
                        ),
                        padding=ft.padding.only(left=6, right=6),
                    )
                )
            suggestions_container.content = ft.Column(controls=controls)
            suggestions_container.visible = len(controls) > 0

            # if visible, move the overlay wrapper to page.overlay so it receives events
            try:
                if suggestions_container.visible:
                    # remove from stack controls if present
                    if overlay_wrapper in self.select_cliente.controls:
                        try:
                            self.select_cliente.controls.remove(overlay_wrapper)
                        except Exception:
                            pass
                    # add to page.overlay if not present
                    if overlay_wrapper not in page.overlay:
                        try:
                            page.overlay.append(overlay_wrapper)
                        except Exception:
                            try:
                                page.overlay.add(overlay_wrapper)
                            except Exception:
                                pass
                else:
                    # hide: ensure wrapper is back in stack
                    if overlay_wrapper in page.overlay:
                        try:
                            page.overlay.remove(overlay_wrapper)
                        except Exception:
                            pass
                    if overlay_wrapper not in self.select_cliente.controls:
                        self.select_cliente.controls.append(overlay_wrapper)
            except Exception:
                pass

            page.update()

        select_cliente_field = ft.TextField(
            label=label,
            expand=True,
            on_change=on_cliente_change,
        )

        suggestions_container = ft.Container(
            content=ft.Column(controls=[]),
            visible=False,
            bgcolor="white",
            border=ft.border.all(1, "#cccccc"),
            padding=ft.padding.only(top=2, bottom=2),
            ignore_interactions=False,
        )

        def on_page_resize(e):
            left_position = page.window.width / 2
            overlay_wrapper.left = left_position
            try:
                overlay_wrapper.update()
            except Exception:
                pass

        # wrapper used both inside the Stack and (temporarily) in page.overlay
        # set a fixed width for the field+overlay so suggestions match field width
        field_overlay_width = 360
        left_position = page.window.width / 2
        overlay_wrapper = ft.Container(content=suggestions_container, left=left_position, top=140, width=field_overlay_width)
        page.on_resized = on_page_resize

        # show suggestions as an overlay so they don't change the Row2 height
        self.select_cliente = ft.Stack(
            controls=[
                # base: the text field
                ft.Container(content=select_cliente_field),
                # overlay wrapper: moved to page.overlay when visible
                overlay_wrapper,
            ],
            clip_behavior=ft.ClipBehavior.NONE,
            width=field_overlay_width,
            expand=True,
        )

    def Crear(self):
        return self.select_cliente