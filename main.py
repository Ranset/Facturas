from flet_base import flet_instance as ft
from pages.common_controls.states import States

def main(page: ft.Page):
    from router import show_view

    States.states_page.append(page)

    # Load Custom Fonts for use in the app
    page.fonts = {
        "handlee": "./assets/fonts/Handlee-Regular.ttf",
        "poppins": "./assets/fonts/Poppins-Regular.ttf",
    }

    page.theme = ft.Theme(
        font_family="Arial",
    )

    page.window.min_width = 1200
    page.window.min_height = 400

    page.bgcolor = "#F4F5F7"
    page.padding = 0

    # on load
    show_view(page, "inicio")

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")