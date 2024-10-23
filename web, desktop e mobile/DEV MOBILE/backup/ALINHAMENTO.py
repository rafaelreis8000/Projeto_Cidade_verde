import flet as ft

def login(page: ft.Page):

    btn_1=ft.Container(
        content=ft.Text("BOTAO 1"),
        width=100,
        height=100,
        bgcolor="#2A383E",
        padding=10
    )

    btn_2=ft.Container(
        content=ft.Text("BOTAO 2"),
        width=100,
        height=100,
        bgcolor="#2A383E",
        padding=10
    )

    btn_3=ft.Container(
        content=ft.Text("BOTAO 3"),
        width=100,
        height=100,
        bgcolor="#2A383E",
        padding=10
    )

    btn_4=ft.Container(
        content=ft.Text("BOTAO 4"),
        width=100,
        height=100,
        bgcolor="#2A383E",
        padding=10
    )

    btn_5=ft.Container(
        content=ft.Text("BOTAO 5"),
        width=100,
        height=100,
        bgcolor="#2A383E",
        padding=10
    )

    horizontal=ft.Container(
        content=ft.Row(
            controls=[btn_1,btn_2,btn_3]
        )
    )

    tela=ft.Container(
        expand=True,
        content=ft.Column(
            controls=[horizontal,
                      btn_4,
                      btn_5,
                      ]
        )
    )

    #manda exibir tudo que estiver no container
    return tela