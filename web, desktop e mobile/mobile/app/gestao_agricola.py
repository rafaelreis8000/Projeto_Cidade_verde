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

    btn_cultura=ft.Container(
        #define os parâmetros visuais do botão como altura, largura, cor e borda
        width=310,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        padding=20,
        on_click=lambda _:page.go("/cultura"),
        #adiciona uma imagem e um texto dentro do botão
        content=ft.Row(
            [
                ft.Image("app/assets\Ícone Cultura.svg"),
                ft.Text("CULTURA"),
            ],
            #centraliza imagem e texto
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    btn_plantio=ft.Container(
        #define os parâmetros visuais do botão como altura, largura, cor e borda
        width=310,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        padding=20,
        on_click=lambda _:page.go("/plantio"),
        #adiciona uma imagem e um texto dentro do botão
        content=ft.Row(
            [
                ft.Image("app/assets\Ícone Plantio.svg"),
                ft.Text("   PLANTIO"),
            ],
            #centraliza imagem e texto
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    btn_colheita=ft.Container(
        #define os parâmetros visuais do botão como altura, largura, cor e borda
        width=310,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        padding=20,
        on_click=lambda _:page.go("/colheita"),
        #adiciona uma imagem e um texto dentro do botão
        content=ft.Row(
            [
                ft.Image("app/assets\Ícone Colheita.svg"),
                ft.Text("COLHEITA"),
            ],
            #centraliza imagem e texto
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    ###############################################################################
    ###############################################################################

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            col={"xs":12,"sm":6,"md":4},
            controls=[
                appbar,
                ft.Container(
                    content=ft.Row(
                        [
                            btn_cultura
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),

                ft.Container(
                    content=ft.Row(
                        [
                            btn_plantio
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),

                ft.Container(
                    content=ft.Row(
                        [
                            btn_colheita
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                )
            ]
        )
    )
    
    return tela