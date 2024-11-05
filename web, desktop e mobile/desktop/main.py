import flet as ft

from app.rotas import registro_rotas

def main(page:ft.Page):

    registro_rotas(page)
    page.title="Fazenda Horticultura"
    page.window.width=1280
    page.window.height=720
    page.window_min_width=1280
    page.window_min_height=720

    page.go("/")
    page.update

ft.app(target=main)