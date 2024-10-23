import flet as ft

from app.rotas import registro_rotas

def main(page:ft.Page):

    #inicia a função de caminho das rotas do sistema assim que o aplicativo inicia
    registro_rotas(page)
    page.title="Fazenda Horticultura"
    page.window.width = 412
    page.window.height = 917

    #chama a tela de login
    page.go("/")
    page.update

ft.app(target=main)