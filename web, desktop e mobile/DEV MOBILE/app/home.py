import flet as ft

def home(page:ft.Page):

    #botão de dashboard. Leva para a página de mesmo nome
    btn_dash=ft.Container(
        #define os parâmetros visuais do botão como altura, largura, cor e borda
        width=310,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        padding=20,
        on_click=lambda _:page.go("/dashboard"),
        #adiciona uma imagem e um texto dentro do botão
        content=ft.Row(
            [
                ft.Image("app/assets\Ícone Dashboard.svg"),
                ft.Text("DASHBOARD"),
            ],
            #centraliza imagem e texto
            alignment=ft.MainAxisAlignment.CENTER,
            wrap=True
        ),
        #alinha os elementos de imagem e texto no centro do botão
        alignment=ft.alignment.center
    )

    btn_gestao_agricola=ft.Container(
        width=150,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        on_click=lambda _:page.go("/g_agricola"),
        content=ft.Column(
            [
                ft.Image("app/assets\Ícone Plantinha.svg",width=50,height=50,fit=ft.ImageFit.CONTAIN),
                ft.Text("Gestão Agrícola",size=10,text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens dentro da coluna
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza na horizontal
            wrap=True
        ),
        alignment=ft.alignment.center
    )

    btn_gestao_insumos=ft.Container(
        width=150,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        on_click=lambda _:page.go("/g_insumos"),
        content=ft.Column(
            [
                ft.Image("app/assets\Ícone Trator.svg",width=50,height=50,fit=ft.ImageFit.CONTAIN),
                ft.Text("Gestão Insumos",size=10,text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            wrap=True
        ),
        alignment=ft.alignment.center
    )

    btn_vendas=ft.Container(
        width=150,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        on_click=lambda _:page.go("/vendas"),
        content=ft.Column(
            [
                ft.Image("app/assets\Ícone Financeiro.svg",width=50,height=50,fit=ft.ImageFit.CONTAIN),
                ft.Text("Vendas",size=10,text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            wrap=True
        ),
        alignment=ft.alignment.center
    )

    btn_relatorios=ft.Container(
        width=150,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        on_click=lambda _:page.go("/relatorios"),
        content=ft.Column(
            [
                ft.Image("app/assets\Ícone Prancheta.svg",width=50,height=50,fit=ft.ImageFit.CONTAIN),
                ft.Text("Relatórios",size=10,text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            wrap=True
        ),
        alignment=ft.alignment.center
    )
    
    btn_sair=ft.Container(
        width=310,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        on_click=lambda _:page.go("/"),
        content=ft.Column(
            [
                ft.Image("app/assets\Ícone Sair.svg",width=50,height=50,fit=ft.ImageFit.CONTAIN),
                ft.Text("Logout",size=10,text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            wrap=True
        ),
        alignment=ft.alignment.center
    )

    ###############################################################################

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            #delimita a quantidade de colunas que os elementos da tela podem ocupar
            col={"xs": 12, "sm": 6, "md": 4},
            controls=[
                ft.Container(
                    content=ft.Text("DASHBOARD",size=40),
                    alignment=ft.alignment.center
                ),

                ft.Container(
                    content=btn_dash,
                    alignment=ft.alignment.center
                ),

                #container da primeira linha de botões(gestão agrícola e de insumos)
                ft.Container(
                    content=ft.Row(
                        [
                            btn_gestao_agricola,
                            btn_gestao_insumos
                        ],
                        #alinha os dois botões para que fiquem ao centro da tela, mesmo redimensionando a janela
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),

                ft.Container(
                    content=ft.Row(
                        [
                            btn_vendas,
                            btn_relatorios
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),

                ft.Container(
                    content=btn_sair,
                    alignment=ft.alignment.center
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    return tela