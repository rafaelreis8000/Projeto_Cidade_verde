import flet as ft
from app.login import login


def registar_rotas(page: ft.Page):
    page.views.clear()

    if page.route == "/":
        page.views.append(ft.View(route="/", controls=[login(page)]))