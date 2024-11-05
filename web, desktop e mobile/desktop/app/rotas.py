import flet as ft

from app.login import TelaLogin
from app.home import TelaHome #chama a classe tela home

def registro_rotas(page:ft.Page):
    def mudar_rotas(route):

        page.views.clear()

        if page.route=="/":
            obj_login=TelaLogin(page)
            page.views.append(ft.View(route="/",controls=[obj_login.login()]))

        elif page.route=="/home":
            obj_home=TelaHome(page)
            page.views.append(ft.View(route="/home",controls=[obj_home.home()]))

        page.update()

    page.on_route_change=mudar_rotas