import flet as ft

def g_agricola(page:ft.Page):

    icone_retornar=ft.Container(
        on_click=lambda _:page.go("/home"),
        content=ft.Image(
            "app/assets\Ícone retornar.svg",
            width=20,
            height=20
        )
    )

    titulo_gestao_agricola=ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Text("GESTÃO AGRÍCOLA",size=25)
    )

    appbar=ft.Container(
        expand=True,
        height=50,
        bgcolor="#2A383E",
        padding=10,
        content=ft.Row(
            [
                icone_retornar,
                titulo_gestao_agricola
            ],
        )
    )

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            col={"xs": 12, "sm": 6, "md": 4},
            controls=[appbar]
        )
    )
    
    return tela