import flet as ft

def g_insumos(page:ft.Page):

    icone_retornar=ft.Container(
        on_click=lambda _:page.go("/home"),
        content=ft.Image(
            "app/assets\Ícone retornar.svg",
            width=20,
            height=20
        )
    )

    titulo_gestao_insumos=ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Text("GESTÃO INSUMOS",size=25)
    )

    appbar=ft.Container(
        expand=True,
        height=50,
        bgcolor="#2A383E",
        padding=10,
        content=ft.Row(
            [
                icone_retornar,
                titulo_gestao_insumos
            ],
        )
    )

    btn_insumos=ft.Container(
        #define os parâmetros visuais do botão como altura, largura, cor e borda
        width=310,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        padding=20,
        on_click=lambda _:page.go("/insumos"),
        #adiciona uma imagem e um texto dentro do botão
        content=ft.Row(
            [
                ft.Image("app/assets\Ícone Insumos.svg"),
                ft.Text("INSUMOS"),
            ],
            #centraliza imagem e texto
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    btn_fornecedores=ft.Container(
        #define os parâmetros visuais do botão como altura, largura, cor e borda
        width=310,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        padding=20,
        on_click=lambda _:page.go("/fornecedores"),
        #adiciona uma imagem e um texto dentro do botão
        content=ft.Row(
            [
                ft.Image("app/assets\Ícone Fornecedores.svg"),
                ft.Text("FORNECEDORES"),
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
                            btn_insumos
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),

                ft.Container(
                    content=ft.Row(
                        [
                            btn_fornecedores
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                )
            ]
        )
    )
    
    return tela