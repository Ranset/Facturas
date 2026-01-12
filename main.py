import flet as ft

def main(page: ft.Page):
    from router import show_view

    # Load Custom Fonts for use in the app
    page.fonts = {
        "handlee": "./assets/fonts/Handlee-Regular.ttf",
        "poppins": "./assets/fonts/Poppins-Regular.ttf",
    }

    page.theme = ft.Theme(
        font_family="poppins",
    )

    # on load
    show_view(page, "/cotizacion")

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")