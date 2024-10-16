import flet as ft
from app.login import login


def registro_rotas(page: ft.Page):
    def mudar_rotas(route):
        #limpa a tela para que comece a checagem dos caminhos
        page.views.clear()

        #leva para a tela de login
        if page.route == "/":
            page.views.append(ft.View(route="/", controls=[login(page)]))

        #garante que o conteúdo mais recente esteja aparecendo na tela
        page.update()

    #sempre que houver uma mudança de rotas, ele chama a checagem
    page.on_route_change = mudar_rotas