import flet as ft

from app.login import login
from app.home import home
from app.dashboard import dashboard
from app.gestao_agricola import g_agricola
from app.gestao_insumos import g_insumos
from app.vendas import vendas
from app.relatorios import relatorios

#função que realiza o caminho das telas do sistema
def registro_rotas(page:ft.Page):
    def mudar_rota(route):
        #limpa a tela para começar a checar as rotas
        page.views.clear()

        #leva para a tela de login
        if page.route=="/":
            page.views.append(ft.View(route="/",controls=[login(page)]))

        elif page.route=="/home":
            page.views.append(ft.View(route="/home",controls=[home(page)]))
        
        elif page.route=="/dashboard":
            page.views.append(ft.View(route="/dashboard",controls=[dashboard(page)]))

        elif page.route=="/g_agricola":
            page.views.append(ft.View(route="/g_agricola",controls=[g_agricola(page)]))

        elif page.route=="/g_insumos":
            page.views.append(ft.View(route="/g_insumos",controls=[g_insumos(page)]))

        elif page.route=="/vendas":
            page.views.append(ft.View(route="/vendas",controls=[vendas(page)]))

        elif page.route=="/relatorios":
            page.views.append(ft.View(route="/relatorios",controls=[relatorios(page)]))

        page.update()

    page.on_route_change=mudar_rota