import flet as ft

def home(page:ft.Page):


    #Pop-up de alerta. Ao clicar em fazer logoff, uma confirmação é chamada
    alerta_logout=ft.AlertDialog(
        modal=True,
        bgcolor="#2A383E",
        title=ft.Text("CONFIRMAR LOGOUT"),
        content=ft.Text("Você realmente deseja fazer Logoff do aplicativo?"),
        actions=[
            ft.TextButton("Sim", on_click=lambda _:page.go("/")),
            ft.TextButton("Não", on_click=lambda e:page.close(alerta_logout)),
        ]
    )

    ###############################################################################
    ###############################################################################

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
        )
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
        )
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
        )
    )

    btn_pedidos=ft.Container(
        width=150,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        on_click=lambda _:page.go("/pedidos"),
        content=ft.Column(
            [
                ft.Image("app/assets\Ícone Financeiro.svg",width=50,height=50,fit=ft.ImageFit.CONTAIN),
                ft.Text("Pedidos",size=10,text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
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
        )
    )
    
    btn_logout=ft.Container(
        width=310,
        height=100,
        bgcolor="#2A383E",
        border=ft.border.all(10,"#222D32"),
        border_radius=10,
        on_click=lambda e:page.open(alerta_logout),
        content=ft.Column(
            [
                ft.Image("app/assets\Ícone Sair.svg",width=50,height=50,fit=ft.ImageFit.CONTAIN),
                ft.Text("Logout",size=10,text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center
    )

    ###############################################################################
    ###############################################################################

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            #delimita a quantidade de colunas que os elementos da tela podem ocupar
            col={"xs":12,"sm":6,"md":4},
            controls=[
                ft.Container(
                    content=ft.Text("HOME",size=40),
                    alignment=ft.alignment.center
                ),

                ft.Container(
                    content=btn_dash,
                    alignment=ft.alignment.center #esse alinhamento impede que o botão se estique para as bordas da tela e o mantém corretamente orientado
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
                            btn_pedidos,
                            btn_relatorios
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),

                ft.Container(
                    content=btn_logout,
                    alignment=ft.alignment.center
                )
            ]
        )
    )

    return tela