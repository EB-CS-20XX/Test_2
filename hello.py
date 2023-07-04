import flet as ft

def main (page: ft.Page):
    page.add(ft.Text("Hello Sam"))

ft.app(target=main, port=80, view=ft.WEB_BROWSER)