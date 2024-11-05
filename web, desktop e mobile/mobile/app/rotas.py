import flet as ft

from app.login import login
from app.home import home
from app.dashboard import dashboard
from app.gestao_agricola import g_agricola
from app.gestao_insumos import g_insumos
from app.pedidos import vendas
from app.relatorios import relatorios
from app.colheita import colheita
from app.plantio import plantio
from app.cultura import cultura
from app.fornecedores import fornecedores
from app.insumos import insumos

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

        elif page.route=="/pedidos":
            page.views.append(ft.View(route="/pedidos",controls=[vendas(page)]))

        elif page.route=="/relatorios":
            page.views.append(ft.View(route="/relatorios",controls=[relatorios(page)]))

        elif page.route=="/colheita":
            page.views.append(ft.View(route="/colheita",controls=[colheita(page)]))

        elif page.route=="/plantio":
            page.views.append(ft.View(route="/plantio",controls=[plantio(page)]))

        elif page.route=="/cultura":
            page.views.append(ft.View(route="/cultura",controls=[cultura(page)]))

        elif page.route=="/fornecedores":
            page.views.append(ft.View(route="/fornecedores",controls=[fornecedores(page)]))

        elif page.route=="/insumos":
            page.views.append(ft.View(route="/insumos",controls=[insumos(page)]))

        page.update()

    page.on_route_change=mudar_rota