import flet as ft
from app.rotas import registar_rotas

def main(page: ft.Page):
    registar_rotas(page)

    page.go("/")
    page.update

ft.app(target=main)