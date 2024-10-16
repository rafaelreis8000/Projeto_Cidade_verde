import flet as ft
from app.rotas import registro_rotas


#função principal, onde carrega as funções que o código precisa rodar
def main(page: ft.Page):

    #carrega a função registrar rotas, onde todos os caminhos do projeto são checados
    registro_rotas(page)
    page.window_width = 412
    page.window_height = 917
    page.window_bgcolor = "#1D3331"
    #manda ir para o endereço de rota /
    page.go("/")
    page.update

ft.app(target=main)