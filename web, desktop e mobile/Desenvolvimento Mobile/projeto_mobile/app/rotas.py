import flet as ft

#importa os arquivos
from app.login import login
from app.home import home
from app.dashboard import dash
from app.gestao_agricola import gestao_agricola
from app.gestao_insumos import gestao_insumos


def registro_rotas(page: ft.Page):
    def mudar_rotas(route):
        #limpa a tela para que comece a checagem dos caminhos
        page.views.clear()

        #leva para a tela de login
        if page.route == "/":
            page.views.append(ft.View(route="/", controls=[login(page)]))

        #leva para a tela home do sistema
        elif page.route == "/home":
            page.views.append(ft.View(route="/home", controls=[home(page)]))

        elif page.route == "/Dashboard":
            page.views.append(ft.View(route="/Dashboard", controls=[dash(page)]))

        elif page.route == "/g_Agricola":
            page.views.append(ft.View(route="/g_Agricola", controls=[gestao_agricola(page)]))

        elif page.route == "/g_Insumos":
            page.views.append(ft.View(route="/g_Insumos", controls=[gestao_insumos(page)]))

        #garante que o conteúdo mais recente esteja aparecendo na tela
        page.update()

    #sempre que houver uma mudança de rotas, ele chama a checagem
    page.on_route_change = mudar_rotas